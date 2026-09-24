"""Send one SMS per three-day absence streak after attendance is saved."""

import base64
import json
import os
import re
from datetime import date, datetime
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from sqlalchemy import Column, Date, DateTime, Integer, MetaData, String, Table, UniqueConstraint, func, select

from database import SessionLocal, Student, Attendance

metadata = MetaData()
alert_log = Table(
    "parent_absence_alerts", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("school_code", String(100), nullable=False),
    Column("student_id", Integer, nullable=False),
    Column("streak_start", Date, nullable=False),
    Column("sent_at", DateTime, nullable=False),
    Column("provider_message_id", String(100)),
    UniqueConstraint("school_code", "student_id", "streak_start", name="uq_parent_absence_streak"),
)


def sms_is_configured():
    return all(os.getenv(k) for k in ("TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN", "TWILIO_FROM_NUMBER"))


def send_sms(number, body):
    """Submit an SMS to Twilio; success means accepted, not handset delivery."""
    sid = os.environ["TWILIO_ACCOUNT_SID"]
    token = os.environ["TWILIO_AUTH_TOKEN"]
    sender = os.environ["TWILIO_FROM_NUMBER"]
    auth = base64.b64encode(f"{sid}:{token}".encode()).decode()
    request = Request(
        f"https://api.twilio.com/2010-04-01/Accounts/{sid}/Messages.json",
        data=urlencode({"To": number, "From": sender, "Body": body}).encode(),
        headers={"Authorization": f"Basic {auth}", "Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    with urlopen(request, timeout=15) as response:
        return json.load(response)["sid"]


def check_absences_and_send(school_code, class_name, division, attendance_date):
    """Check three most recent recorded class days; call only after class attendance is saved."""
    if not sms_is_configured():
        return {"sent": 0, "skipped": "SMS credentials are not configured"}
    db = SessionLocal()
    sent = 0
    errors = []
    try:
        metadata.create_all(db.get_bind(), tables=[alert_log], checkfirst=True)
        dates = [row[0] for row in db.query(Attendance.date).join(Student, Student.id == Attendance.student_id).filter(
            Student.school_code == school_code, Student.class_name == class_name,
            Student.division == division, Attendance.date <= attendance_date,
        ).distinct().order_by(Attendance.date.desc()).limit(3).all()]
        if len(dates) < 3 or dates[0] != attendance_date:
            return {"sent": 0, "skipped": "Fewer than three recorded class days"}
        start = dates[-1]
        students = db.query(Student).filter(
            Student.school_code == school_code, Student.class_name == class_name,
            Student.division == division,
        ).all()
        for student in students:
            number = (student.parent_contact or "").strip()
            if not re.fullmatch(r"\+[1-9]\d{7,14}", number):
                continue
            statuses = dict(db.query(Attendance.date, Attendance.status).filter(
                Attendance.student_id == student.id, Attendance.date.in_(dates),
            ).all())
            if len(statuses) != 3 or any(str(statuses[d]).lower() != "absent" for d in dates):
                continue
            # Do not send repeatedly on every later absent day in the same streak.
            earlier_absence = db.query(Attendance.id).filter(
                Attendance.student_id == student.id, Attendance.date < start,
                func.lower(Attendance.status) == "absent",
            ).order_by(Attendance.date.desc()).first()
            if earlier_absence:
                previous = db.query(Attendance.status).filter(
                    Attendance.student_id == student.id, Attendance.date < start,
                ).order_by(Attendance.date.desc()).first()
                if previous and str(previous[0]).lower() == "absent":
                    continue
            already_sent = db.execute(select(alert_log.c.id).where(
                alert_log.c.school_code == school_code,
                alert_log.c.student_id == student.id,
                alert_log.c.streak_start == start,
            )).first()
            if already_sent:
                continue
            message = (f"Dear parent, {student.name} has been absent for three consecutive "
                       "recorded school days. Please contact the school. - Mahatma Gandhi English School")
            try:
                message_id = send_sms(number, message)
                db.execute(alert_log.insert().values(
                    school_code=school_code, student_id=student.id,
                    streak_start=start, sent_at=datetime.utcnow(), provider_message_id=message_id,
                ))
                db.commit()
                sent += 1
            except Exception as exc:
                db.rollback()
                errors.append(f"Student ID {student.id}: {exc}")
        return {"sent": sent, "errors": errors}
    finally:
        db.close()
