import streamlit as st
# =========================================================
# 🎨 SCHOOL AI - MODERN UI THEME
# =========================================================

st.set_page_config(
    page_title="SchoolAI",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="auto"
)

st.markdown("""
<style>

/* ================================
   SCHOOL AI - PREMIUM UI
================================ */

.stApp {
    background: #f6f8fc;
}

/* Main content */
.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* ================================
   SIDEBAR
================================ */

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827 0%, #172554 100%);
    border-right: 1px solid rgba(255,255,255,0.08);
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1.5rem;
}

[data-testid="stSidebar"] * {
    color: #f8fafc;
}

/* Sidebar headings */
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: white !important;
    font-weight: 700;
}

/* Sidebar buttons */
[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,0.12);
    background: rgba(255,255,255,0.08);
    color: white;
    font-weight: 600;
    transition: 0.2s;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(255,255,255,0.16);
    border-color: rgba(255,255,255,0.25);
}

/* Sidebar success box */
[data-testid="stSidebar"] [data-testid="stAlert"] {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 12px;
}

/* ================================
   HEADER
================================ */

h1 {
    font-size: 2.4rem !important;
    font-weight: 800 !important;
    letter-spacing: -1px;
}

h2 {
    font-weight: 750 !important;
}

h3 {
    font-weight: 700 !important;
}

/* ================================
   METRIC CARDS
================================ */

[data-testid="stMetric"] {
    background: white;
    padding: 22px 20px;
    border-radius: 18px;
    border: 1px solid #e6eaf0;
    box-shadow: 0 5px 18px rgba(15,23,42,0.06);
    transition: transform 0.2s, box-shadow 0.2s;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(15,23,42,0.10);
}

[data-testid="stMetricLabel"] {
    font-weight: 600;
    color: #64748b;
}

[data-testid="stMetricValue"] {
    font-size: 2rem;
    font-weight: 800;
    color: #0f172a;
}

/* ================================
   CARDS / CONTAINERS
================================ */

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    background: white;
    box-shadow: 0 5px 18px rgba(15,23,42,0.05);
}

/* ================================
   BUTTONS
================================ */

.stButton > button {
    border-radius: 10px;
    min-height: 42px;
    font-weight: 650;
    border: 1px solid #dbe2ea;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 5px 14px rgba(15,23,42,0.10);
}

/* ================================
   INPUTS
================================ */

.stTextInput input,
.stTextArea textarea {
    border-radius: 10px;
    border: 1px solid #dbe2ea;
    background: white;
}

[data-baseweb="select"] > div {
    border-radius: 10px;
}

/* ================================
   TABLE
================================ */

[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid #e5e7eb;
    box-shadow: 0 4px 14px rgba(15,23,42,0.04);
}

/* ================================
   ALERTS
================================ */

[data-testid="stAlert"] {
    border-radius: 12px;
}

/* ================================
   DIVIDERS
================================ */

hr {
    border: none;
    border-top: 1px solid #e5e7eb;
    margin: 1.5rem 0;
}

/* ================================
   CHART AREA
================================ */

[data-testid="stVegaLiteChart"],
[data-testid="stArrowVegaLiteChart"] {
    background: white;
    border-radius: 16px;
    padding: 12px;
    border: 1px solid #e5e7eb;
}

/* ================================
   FILE UPLOADER
================================ */

[data-testid="stFileUploader"] {
    border-radius: 14px;
}

/* ================================
   CHAT
================================ */

[data-testid="stChatMessage"] {
    border-radius: 14px;
    margin-bottom: 8px;
}

/* ================================
   LOGIN PAGE
================================ */

.login-title {
    text-align: center;
    font-size: 46px;
    font-weight: 800;
    color: #172554;
    margin-top: 45px;
}

.login-subtitle {
    text-align: center;
    font-size: 18px;
    color: #64748b;
    margin-bottom: 30px;
}

/* ================================
   MOBILE
================================ */

@media (max-width: 768px) {

    .block-container {
        padding: 1rem;
    }

    h1 {
        font-size: 1.8rem !important;
    }

    [data-testid="stMetric"] {
        padding: 15px;
    }

}



/* ================================
   MOBILE-FIRST RESPONSIVE UPGRADE
================================ */

/* Comfortable touch targets */
.stButton > button,
.stDownloadButton > button,
.stLinkButton > a {
    min-height: 46px !important;
}

/* Prevent long labels / values from breaking the page */
[data-testid="stMetricValue"],
[data-testid="stMetricLabel"],
.stCaption,
p, label {
    overflow-wrap: anywhere;
}

/* Tables stay usable on narrow screens */
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    max-width: 100% !important;
    overflow-x: auto !important;
}

/* Inputs are touch friendly */
.stTextInput input,
.stTextArea textarea,
.stNumberInput input,
[data-baseweb="select"] > div {
    min-height: 44px;
    font-size: 16px !important;
}

@media (max-width: 900px) {
    .block-container {
        max-width: 100% !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
    }

    h1 {
        font-size: 1.85rem !important;
        line-height: 1.2 !important;
    }

    h2 {
        font-size: 1.45rem !important;
    }

    h3 {
        font-size: 1.18rem !important;
    }

    [data-testid="stMetric"] {
        padding: 14px 13px !important;
        border-radius: 14px !important;
    }

    [data-testid="stMetricValue"] {
        font-size: 1.55rem !important;
    }

    /* Keep sidebar compact and mobile-friendly */
    [data-testid="stSidebar"] {
        min-width: min(84vw, 330px) !important;
        max-width: min(84vw, 330px) !important;
    }

    [data-testid="stSidebar"] .stButton > button {
        min-height: 46px !important;
    }

    /* Login hero should not dominate small screens */
    .school-hero {
        min-height: 0 !important;
        padding: 24px 20px !important;
        border-radius: 20px !important;
    }

    .hero-icon {
        margin: 18px 0 8px !important;
        font-size: 44px !important;
    }

    .hero-title {
        font-size: 29px !important;
    }

    .hero-copy {
        font-size: 14px !important;
        line-height: 1.55 !important;
    }

    .hero-tags {
        margin-top: 18px !important;
        gap: 7px !important;
    }

    .hero-tags span {
        padding: 7px 10px !important;
        font-size: 12px !important;
    }

    .login-heading {
        font-size: 29px !important;
    }

    [data-testid="stTabs"] {
        padding: 8px 8px 12px !important;
        border-radius: 18px !important;
    }

    /* Make buttons easier to tap */
    .stButton > button,
    .stDownloadButton > button,
    .stLinkButton > a {
        width: 100% !important;
        min-height: 48px !important;
        font-size: 15px !important;
    }
}

@media (max-width: 600px) {
    .block-container {
        padding-left: .75rem !important;
        padding-right: .75rem !important;
    }

    h1 {
        font-size: 1.65rem !important;
    }

    /* Dashboard cards / containers become tighter */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 14px !important;
    }

    /* Horizontal scrolling for wide report/admin tables */
    [data-testid="stDataFrame"] > div {
        max-width: 100% !important;
        overflow-x: auto !important;
    }

    /* Avoid clipped select boxes and long filenames */
    [data-baseweb="select"] {
        max-width: 100% !important;
    }

    [data-testid="stFileUploader"] {
        max-width: 100% !important;
    }

    .dash-hero {
        padding: 20px 18px !important;
        border-radius: 18px !important;
    }

    .dash-title {
        font-size: 26px !important;
    }

    .dash-subtitle {
        font-size: 14px !important;
    }
}
</style>
""", unsafe_allow_html=True)
import time
import secrets
from html import escape
from threading import Lock
from datetime import date, datetime, timedelta
from pathlib import Path
import pandas as pd

import bcrypt
from dotenv import load_dotenv

from sqlalchemy import func, case, Table, Column, String, Integer, Date, DateTime, Text, MetaData, select

from agents import Agent, Runner
from agents.decorators import tool

from database import SessionLocal, Student, Attendance, User
import os
import json
import hmac
import hashlib
import base64
import re
from urllib.parse import urlencode
from urllib.request import Request, urlopen





# =========================================================
# SETUP
# =========================================================

load_dotenv()

# =========================================================
# AUDIT LOG
# =========================================================
audit_metadata = MetaData()
audit_logs = Table(
    "audit_logs", audit_metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("school_code", String(100), nullable=True),
    Column("username", String(100), nullable=False),
    Column("role", String(50), nullable=False),
    Column("action", String(100), nullable=False),
    Column("entity_type", String(100), nullable=True),
    Column("entity_id", String(100), nullable=True),
    Column("details", Text, nullable=True),
    Column("created_at", DateTime, nullable=False),
)

def ensure_audit_log_table(db):
    audit_metadata.create_all(db.get_bind(), tables=[audit_logs], checkfirst=True)

def write_audit_log(action, details="", entity_type="", entity_id="", school_code=None, username=None, role=None):
    """Write a non-blocking audit record. Audit failures must never break the main action."""
    db = SessionLocal()
    try:
        ensure_audit_log_table(db)
        db.execute(audit_logs.insert().values(
            school_code=(school_code if school_code is not None else st.session_state.get("school_code", "")) or "",
            username=(username if username is not None else st.session_state.get("username", "")) or "system",
            role=(role if role is not None else st.session_state.get("role", "")) or "system",
            action=str(action),
            entity_type=str(entity_type or ""),
            entity_id=str(entity_id or ""),
            details=str(details or ""),
            created_at=datetime.utcnow(),
        ))
        db.commit()
    except Exception:
        db.rollback()
    finally:
        db.close()

def load_audit_logs(school_code=None, limit=500):
    db = SessionLocal()
    try:
        ensure_audit_log_table(db)
        query = select(audit_logs)
        if school_code is not None:
            query = query.where(audit_logs.c.school_code == str(school_code))
        return db.execute(
            query.order_by(audit_logs.c.created_at.desc()).limit(int(limit))
        ).mappings().all()
    finally:
        db.close()

# =========================================================
# PARENT ACCOUNTS
# =========================================================
# Parent logins are stored separately from staff accounts so a parent can
# only be linked to one student record and never receives teacher/principal
# permissions by mistake.
parent_metadata = MetaData()
parent_accounts = Table(
    "parent_accounts", parent_metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", String(100), unique=True, nullable=False),
    Column("name", String(200), nullable=False),
    Column("username", String(100), unique=True, nullable=False),
    Column("password_hash", String(300), nullable=False),
    Column("school_code", String(100), nullable=False),
    Column("student_id", Integer, nullable=False),
    Column("phone", String(30), nullable=True),
    Column("created_at", DateTime, nullable=False),
)

def ensure_parent_accounts_table(db):
    parent_metadata.create_all(db.get_bind(), tables=[parent_accounts], checkfirst=True)

def find_parent_account(db, username):
    ensure_parent_accounts_table(db)
    return db.execute(
        select(parent_accounts).where(
            func.lower(parent_accounts.c.username) == str(username or "").strip().lower()
        )
    ).mappings().first()


# =========================================================
# SCHOOL CALENDAR / HOLIDAYS
# =========================================================
calendar_metadata = MetaData()
school_calendar = Table(
    "school_calendar", calendar_metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("school_code", String(100), nullable=False),
    Column("event_date", Date, nullable=False),
    Column("title", String(200), nullable=False),
    Column("event_type", String(40), nullable=False),
    Column("description", Text, nullable=True),
    Column("created_at", DateTime, nullable=False),
)


def ensure_school_calendar_table(db):
    calendar_metadata.create_all(db.get_bind(), tables=[school_calendar], checkfirst=True)


def load_school_calendar(school_code, start_date=None, end_date=None):
    db = SessionLocal()
    try:
        ensure_school_calendar_table(db)
        query = select(school_calendar).where(
            school_calendar.c.school_code == str(school_code)
        )
        if start_date is not None:
            query = query.where(school_calendar.c.event_date >= start_date)
        if end_date is not None:
            query = query.where(school_calendar.c.event_date <= end_date)
        return db.execute(
            query.order_by(school_calendar.c.event_date, school_calendar.c.title)
        ).mappings().all()
    finally:
        db.close()


def get_holiday_for_date(school_code, target_date):
    db = SessionLocal()
    try:
        ensure_school_calendar_table(db)
        return db.execute(
            select(school_calendar).where(
                school_calendar.c.school_code == str(school_code),
                school_calendar.c.event_date == target_date,
                func.lower(school_calendar.c.event_type) == "holiday",
            ).order_by(school_calendar.c.id).limit(1)
        ).mappings().first()
    finally:
        db.close()


# =========================================================
# STUDENT MARKS / RESULT MODULE
# =========================================================
result_metadata = MetaData()
student_results = Table(
    "student_results", result_metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("school_code", String(100), nullable=False),
    Column("student_id", Integer, nullable=False),
    Column("academic_year", String(30), nullable=False),
    Column("exam_name", String(120), nullable=False),
    Column("subject_name", String(120), nullable=False),
    Column("max_marks", Integer, nullable=False),
    Column("marks_obtained", Integer, nullable=False),
    Column("remarks", String(250), nullable=True),
    Column("updated_by", String(120), nullable=True),
    Column("updated_at", DateTime, nullable=False),
)


def ensure_student_results_table(db):
    result_metadata.create_all(db.get_bind(), tables=[student_results], checkfirst=True)


def load_student_results(school_code, student_id=None, academic_year=None, exam_name=None):
    db = SessionLocal()
    try:
        ensure_student_results_table(db)
        query = select(student_results).where(
            student_results.c.school_code == str(school_code)
        )
        if student_id is not None:
            query = query.where(student_results.c.student_id == int(student_id))
        if academic_year:
            query = query.where(student_results.c.academic_year == str(academic_year))
        if exam_name:
            query = query.where(student_results.c.exam_name == str(exam_name))
        return db.execute(
            query.order_by(
                student_results.c.academic_year.desc(),
                student_results.c.exam_name,
                student_results.c.subject_name,
            )
        ).mappings().all()
    finally:
        db.close()


def result_summary(rows):
    total_max = sum(int(row["max_marks"] or 0) for row in rows)
    total_obtained = sum(int(row["marks_obtained"] or 0) for row in rows)
    percentage = (total_obtained / total_max * 100) if total_max else 0.0
    return total_obtained, total_max, percentage


def build_student_report_card_pdf(school_name, school_code, student, academic_year, exam_name, rows):
    from io import BytesIO
    try:
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_CENTER
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import mm
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    except ImportError as exc:
        raise RuntimeError("ReportLab is not installed. Run: python -m pip install reportlab") from exc

    total_obtained, total_max, percentage = result_summary(rows)
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=A4, rightMargin=15 * mm, leftMargin=15 * mm,
        topMargin=14 * mm, bottomMargin=14 * mm,
        title=f"Report Card - {student.name} - {exam_name}",
        author=str(school_name or school_code),
    )
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "ResultTitle", parent=styles["Title"], alignment=TA_CENTER,
        fontSize=18, leading=22, spaceAfter=4
    )
    sub_style = ParagraphStyle(
        "ResultSub", parent=styles["Normal"], alignment=TA_CENTER,
        fontSize=10, leading=13, textColor=colors.HexColor("#475569")
    )
    story = [
        Paragraph(str(school_name or "School AI"), title_style),
        Paragraph("Student Report Card", sub_style),
        Paragraph(f"Academic Year: {academic_year} &nbsp;&nbsp; | &nbsp;&nbsp; Exam: {exam_name}", sub_style),
        Spacer(1, 6 * mm),
    ]

    details = Table([
        ["Student", str(student.name), "Class", f"{student.class_name}{student.division or ''}"],
        ["School Code", str(school_code), "Generated", datetime.now().strftime("%d %b %Y")],
    ], colWidths=[28 * mm, 62 * mm, 28 * mm, 62 * mm])
    details.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#EFF6FF")),
        ("BACKGROUND", (2, 0), (2, -1), colors.HexColor("#EFF6FF")),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME", (2, 0), (2, -1), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.extend([details, Spacer(1, 7 * mm)])

    table_data = [["Sr.", "Subject", "Marks", "Out of", "%", "Remarks"]]
    for idx, row in enumerate(rows, 1):
        max_marks = int(row["max_marks"] or 0)
        obtained = int(row["marks_obtained"] or 0)
        pct = (obtained / max_marks * 100) if max_marks else 0
        table_data.append([
            str(idx), str(row["subject_name"]), str(obtained), str(max_marks),
            f"{pct:.1f}%", str(row.get("remarks") or ""),
        ])
    table_data.append(["", "TOTAL", str(total_obtained), str(total_max), f"{percentage:.1f}%", ""])

    marks_table = Table(table_data, repeatRows=1, colWidths=[12 * mm, 55 * mm, 25 * mm, 25 * mm, 25 * mm, 48 * mm])
    marks_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1D4ED8")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
        ("BACKGROUND", (0, -1), (-1, -1), colors.HexColor("#F1F5F9")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
        ("ALIGN", (2, 1), (4, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.extend([marks_table, Spacer(1, 7 * mm)])
    story.append(Paragraph(
        f"Overall: <b>{total_obtained} / {total_max}</b> &nbsp;&nbsp; | &nbsp;&nbsp; Percentage: <b>{percentage:.1f}%</b>",
        styles["Heading3"],
    ))
    story.append(Spacer(1, 14 * mm))
    signatures = Table([["Class Teacher Signature", "Principal Signature", "Parent Signature"]], colWidths=[60 * mm, 60 * mm, 60 * mm])
    signatures.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("TOPPADDING", (0, 0), (-1, -1), 18),
        ("LINEABOVE", (0, 0), (-1, 0), 0.5, colors.HexColor("#94A3B8")),
    ]))
    story.append(signatures)
    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()


# =========================================================
# SUPER ADMIN + MULTI-SCHOOL MANAGEMENT
# =========================================================
admin_metadata = MetaData()
schools = Table(
    "schools", admin_metadata,
    Column("school_code", String(100), primary_key=True),
    Column("school_name", String(250), nullable=False),
    Column("status", String(20), nullable=False, default="active"),
    Column("created_at", DateTime, nullable=False),
)


def ensure_admin_tables(db):
    admin_metadata.create_all(db.get_bind(), tables=[schools], checkfirst=True)


def sync_existing_schools(db):
    """Backfill the schools table from existing users/students/parents."""
    ensure_admin_tables(db)
    codes = set()
    try:
        codes.update(str(row[0]).strip() for row in db.query(User.school_code).distinct().all() if row[0])
    except Exception:
        pass
    try:
        codes.update(str(row[0]).strip() for row in db.query(Student.school_code).distinct().all() if row[0])
    except Exception:
        pass
    try:
        ensure_parent_accounts_table(db)
        codes.update(
            str(row[0]).strip()
            for row in db.execute(select(parent_accounts.c.school_code).distinct()).all()
            if row[0]
        )
    except Exception:
        pass

    for code in sorted(codes):
        existing = db.execute(select(schools).where(schools.c.school_code == code)).mappings().first()
        if not existing:
            db.execute(schools.insert().values(
                school_code=code,
                school_name=code,
                status="active",
                created_at=datetime.utcnow(),
            ))
    db.commit()


def get_school_name(school_code):
    if not school_code:
        return "School AI"
    db = SessionLocal()
    try:
        ensure_admin_tables(db)
        row = db.execute(select(schools).where(
            schools.c.school_code == str(school_code)
        )).mappings().first()
        return row["school_name"] if row else str(school_code)
    finally:
        db.close()


def school_is_active(db, school_code):
    """Missing legacy school rows remain active for backwards compatibility."""
    ensure_admin_tables(db)
    row = db.execute(select(schools).where(
        schools.c.school_code == str(school_code)
    )).mappings().first()
    if not row:
        return True
    return str(row["status"] or "active").strip().lower() == "active"


def super_admin_credentials_valid(username, password):
    expected_user = os.getenv("SUPER_ADMIN_USERNAME", "").strip()
    expected_password = os.getenv("SUPER_ADMIN_PASSWORD", "")
    if not expected_user or not expected_password:
        return False
    return (
        hmac.compare_digest(str(username or "").strip().lower(), expected_user.lower())
        and hmac.compare_digest(str(password or ""), expected_password)
    )


def create_super_admin_session(username):
    st.session_state.just_logged_out = False
    st.session_state.logged_in = True
    st.session_state.school_code = ""
    st.session_state.school_name = "School AI Platform"
    st.session_state.username = str(username).strip()
    st.session_state.user_id = "super-admin"
    st.session_state.user_name = "Super Admin"
    st.session_state.role = "super_admin"
    st.session_state.parent_student_id = None
    st.session_state.current_page = "Dashboard"
    st.session_state.failed_attempts = 0
    st.session_state.locked_until = 0.0

    token = secrets.token_urlsafe(32)
    store = session_store()
    with store["lock"]:
        store["sessions"][token] = {
            "expires_at": time.time() + SESSION_SECONDS,
            "school_code": "",
            "school_name": "School AI Platform",
            "username": str(username).strip(),
            "user_id": "super-admin",
            "user_name": "Super Admin",
            "role": "super_admin",
            "parent_student_id": None,
        }
    st.query_params[SESSION_PARAM] = token

# =========================================================
# LOGIN COOKIE
# =========================================================


MAX_LOGIN_ATTEMPTS = 5
LOCKOUT_SECONDS = 300  # 5 minutes
SESSION_SECONDS = 15 * 60
SESSION_PARAM = "school_session"


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "logged_in": False,
    "just_logged_out": False,
    "user_name": "",
    "failed_attempts": 0,
    "current_page": "Dashboard",
    "locked_until": 0.0,
    "messages": [],
    "school_code": "",
    "school_name": "",
    "username": "",
    "role": "",
    "user_id": None,
    "parent_student_id": None,
    "reset_stage": "",
    "reset_account_type": "",
    "reset_user_id": "",
    "reset_username": "",
    "reset_phone": "",
    "reset_otp_hash": "",
    "reset_otp_expires_at": 0.0,
    "reset_otp_attempts": 0,
    "reset_otp_last_sent_at": 0.0,
    "reset_otp_test_value": "",
    "password_reset_success": "",
    "otp_pending": False,
    "otp_user_id": None,
    "otp_hash": "",
    "otp_expires_at": 0.0,
    "otp_attempts": 0,
    "otp_last_sent_at": 0.0,
    "otp_phone": "",
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# Sessions live on the server; the URL carries only an opaque random ID.
# The shared cache survives browser refresh while this app process is running.
@st.cache_resource
def session_store():
    return {"sessions": {}, "lock": Lock()}


def session_record(token):
    if not token or not isinstance(token, str):
        return None
    store = session_store()
    with store["lock"]:
        record = store["sessions"].get(token)
        if record and time.time() >= record["expires_at"]:
            del store["sessions"][token]
            return None
        return record


def clear_login():
    token = st.query_params.get(SESSION_PARAM)
    store = session_store()
    with store["lock"]:
        store["sessions"].pop(token, None)
    if SESSION_PARAM in st.query_params:
        del st.query_params[SESSION_PARAM]
    for field in ("logged_in", "school_code", "school_name", "username",
                  "user_id", "user_name", "role", "messages", "parent_student_id"):
        st.session_state[field] = [] if field == "messages" else (
            False if field == "logged_in" else None if field in ("user_id", "parent_student_id") else ""
        )
    st.session_state.current_page = "Dashboard"
    for key, value in {
        "otp_pending": False, "otp_user_id": None, "otp_hash": "",
        "otp_expires_at": 0.0, "otp_attempts": 0, "otp_last_sent_at": 0.0,
        "otp_phone": "", "otp_test_value": ""
    }.items():
        st.session_state[key] = value


# =========================================================
# PASSWORD HELPERS
# =========================================================

def verify_password(password: str, password_hash: str) -> bool:
    """Verify a bcrypt password hash."""
    try:
        return bcrypt.checkpw(
            password.encode("utf-8"),
            password_hash.encode("utf-8")
        )
    except (ValueError, TypeError):
        return False


# =========================================================
# DATABASE LOGIN
# NOTE:
# The uploaded database.py currently contains Student and
# Attendance tables, but it does NOT contain School/User
# authentication tables. Therefore this version uses a
# secure local admin credential from environment variables
# while student/attendance data comes from school.db.
# =========================================================

# Optional .env fallback.
import os

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD_HASH = os.getenv("ADMIN_PASSWORD_HASH", "")

SCHOOL_CODE = os.getenv("SCHOOL_CODE", "SCHOOL001")
SCHOOL_NAME = os.getenv("SCHOOL_NAME", "School AI Academy")


# =========================================================
# PRINCIPAL OTP HELPERS
# =========================================================

OTP_EXPIRY_SECONDS = 5 * 60
OTP_MAX_ATTEMPTS = 5
OTP_RESEND_SECONDS = 30


def otp_test_mode():
    return os.getenv("OTP_TEST_MODE", "0").strip().lower() in ("1", "true", "yes", "on")


def otp_sms_is_configured():
    return all(os.getenv(k) for k in (
        "TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN", "TWILIO_FROM_NUMBER"
    ))


def send_otp_sms(number: str, otp: str):
    """Send OTP with Twilio. In OTP_TEST_MODE no external SMS is sent."""
    if otp_test_mode():
        return "TEST_MODE"

    if not otp_sms_is_configured():
        raise RuntimeError(
            "OTP SMS is not configured. Add TWILIO_ACCOUNT_SID, "
            "TWILIO_AUTH_TOKEN and TWILIO_FROM_NUMBER to .env, "
            "or use OTP_TEST_MODE=1 while testing."
        )

    sid = os.environ["TWILIO_ACCOUNT_SID"]
    token = os.environ["TWILIO_AUTH_TOKEN"]
    sender = os.environ["TWILIO_FROM_NUMBER"]
    auth = base64.b64encode(f"{sid}:{token}".encode()).decode()
    body = f"Your School AI verification OTP is {otp}. It expires in 5 minutes. Do not share it."
    request = Request(
        f"https://api.twilio.com/2010-04-01/Accounts/{sid}/Messages.json",
        data=urlencode({"To": number, "From": sender, "Body": body}).encode(),
        headers={"Authorization": f"Basic {auth}", "Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    with urlopen(request, timeout=15) as response:
        payload = json.load(response)
        return payload.get("sid", "SENT")


def hash_otp(otp: str) -> str:
    secret = os.getenv("OTP_HASH_SECRET", os.getenv("SESSION_SECRET", "change-this-secret"))
    return hmac.new(secret.encode("utf-8"), otp.encode("utf-8"), hashlib.sha256).hexdigest()


def clear_password_reset_state():
    """Clear temporary password-reset data from the Streamlit session."""
    for key, value in {
        "reset_stage": "",
        "reset_account_type": "",
        "reset_user_id": "",
        "reset_username": "",
        "reset_phone": "",
        "reset_otp_hash": "",
        "reset_otp_expires_at": 0.0,
        "reset_otp_attempts": 0,
        "reset_otp_last_sent_at": 0.0,
        "reset_otp_test_value": "",
    }.items():
        st.session_state[key] = value


def start_password_reset(username: str):
    """Find a staff/parent account, send an OTP, and begin password reset."""
    clean_username = str(username or "").strip()
    if not clean_username:
        raise RuntimeError("Enter your username.")

    db = SessionLocal()
    try:
        user = db.query(User).filter(
            func.lower(User.username) == clean_username.lower()
        ).first()

        account_type = "staff"
        account_user_id = ""
        account_username = ""
        phone = ""

        if user:
            account_user_id = str(user.user_id)
            account_username = str(user.username)
            phone = (getattr(user, "phone", "") or "").strip()
        else:
            parent = find_parent_account(db, clean_username)
            if not parent:
                raise RuntimeError("No account was found with this username.")
            account_type = "parent"
            account_user_id = str(parent["user_id"])
            account_username = str(parent["username"])
            phone = (parent.get("phone") or "").strip()

        if not re.fullmatch(r"\+[1-9]\d{7,14}", phone):
            raise RuntimeError(
                "This account does not have a valid registered mobile number. "
                "Please contact the principal to update the mobile number."
            )

        otp = f"{secrets.randbelow(1_000_000):06d}"
        send_otp_sms(phone, otp)

        st.session_state.reset_stage = "verify"
        st.session_state.reset_account_type = account_type
        st.session_state.reset_user_id = account_user_id
        st.session_state.reset_username = account_username
        st.session_state.reset_phone = phone
        st.session_state.reset_otp_hash = hash_otp(otp)
        st.session_state.reset_otp_expires_at = time.time() + OTP_EXPIRY_SECONDS
        st.session_state.reset_otp_attempts = 0
        st.session_state.reset_otp_last_sent_at = time.time()
        st.session_state.reset_otp_test_value = otp if otp_test_mode() else ""
    finally:
        db.close()


def resend_password_reset_otp():
    """Send a fresh reset OTP to the already-verified account phone."""
    phone = str(st.session_state.get("reset_phone") or "").strip()
    if not re.fullmatch(r"\+[1-9]\d{7,14}", phone):
        raise RuntimeError("Registered mobile number is unavailable.")

    otp = f"{secrets.randbelow(1_000_000):06d}"
    send_otp_sms(phone, otp)
    st.session_state.reset_otp_hash = hash_otp(otp)
    st.session_state.reset_otp_expires_at = time.time() + OTP_EXPIRY_SECONDS
    st.session_state.reset_otp_attempts = 0
    st.session_state.reset_otp_last_sent_at = time.time()
    st.session_state.reset_otp_test_value = otp if otp_test_mode() else ""


def update_reset_password(new_password: str):
    """Update the password only after reset OTP verification."""
    password_hash = bcrypt.hashpw(
        new_password.encode("utf-8"), bcrypt.gensalt()
    ).decode("utf-8")

    account_type = st.session_state.get("reset_account_type")
    reset_user_id = str(st.session_state.get("reset_user_id") or "")

    db = SessionLocal()
    try:
        if account_type == "parent":
            ensure_parent_accounts_table(db)
            result = db.execute(
                parent_accounts.update().where(
                    parent_accounts.c.user_id == reset_user_id
                ).values(password_hash=password_hash)
            )
            if not result.rowcount:
                raise RuntimeError("Parent account could not be found.")
        else:
            user = db.query(User).filter(User.user_id == reset_user_id).first()
            if not user:
                raise RuntimeError("User account could not be found.")
            user.password_hash = password_hash
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def create_authenticated_session(user):
    """Create the 15-minute application session after authentication is complete."""
    display_school_name = get_school_name(user.school_code)
    st.session_state.just_logged_out = False
    st.session_state.logged_in = True
    st.session_state.school_code = user.school_code
    st.session_state.school_name = display_school_name
    st.session_state.username = user.username
    st.session_state.user_id = user.user_id
    st.session_state.user_name = user.name
    st.session_state.role = user.role
    st.session_state.current_page = "Dashboard"
    st.session_state.failed_attempts = 0
    st.session_state.locked_until = 0.0

    token = secrets.token_urlsafe(32)
    store = session_store()
    with store["lock"]:
        store["sessions"][token] = {
            "expires_at": time.time() + SESSION_SECONDS,
            "school_code": user.school_code,
            "school_name": display_school_name,
            "username": user.username,
            "user_id": user.user_id,
            "user_name": user.name,
            "role": user.role,
        }
    st.query_params[SESSION_PARAM] = token


def create_parent_authenticated_session(parent):
    """Create a restricted session for one linked student."""
    display_school_name = get_school_name(parent["school_code"])
    st.session_state.just_logged_out = False
    st.session_state.logged_in = True
    st.session_state.school_code = parent["school_code"]
    st.session_state.school_name = display_school_name
    st.session_state.username = parent["username"]
    st.session_state.user_id = parent["user_id"]
    st.session_state.user_name = parent["name"]
    st.session_state.role = "parent"
    st.session_state.parent_student_id = int(parent["student_id"])
    st.session_state.current_page = "Dashboard"
    st.session_state.failed_attempts = 0
    st.session_state.locked_until = 0.0

    token = secrets.token_urlsafe(32)
    store = session_store()
    with store["lock"]:
        store["sessions"][token] = {
            "expires_at": time.time() + SESSION_SECONDS,
            "school_code": parent["school_code"],
            "school_name": display_school_name,
            "username": parent["username"],
            "user_id": parent["user_id"],
            "user_name": parent["name"],
            "role": "parent",
            "parent_student_id": int(parent["student_id"]),
        }
    st.query_params[SESSION_PARAM] = token


def start_principal_otp(user):
    phone = (getattr(user, "phone", "") or "").strip()
    if not re.fullmatch(r"\+[1-9]\d{7,14}", phone):
        raise RuntimeError(
            "Principal mobile number is missing or invalid. Use format +919876543210."
        )

    otp = f"{secrets.randbelow(1_000_000):06d}"
    send_otp_sms(phone, otp)
    st.session_state.otp_pending = True
    st.session_state.otp_user_id = user.user_id
    st.session_state.otp_hash = hash_otp(otp)
    st.session_state.otp_expires_at = time.time() + OTP_EXPIRY_SECONDS
    st.session_state.otp_attempts = 0
    st.session_state.otp_last_sent_at = time.time()
    st.session_state.otp_phone = phone
    if otp_test_mode():
        st.session_state.otp_test_value = otp


def clear_otp_state():
    for key, value in {
        "otp_pending": False,
        "otp_user_id": None,
        "otp_hash": "",
        "otp_expires_at": 0.0,
        "otp_attempts": 0,
        "otp_last_sent_at": 0.0,
        "otp_phone": "",
        "otp_test_value": "",
    }.items():
        st.session_state[key] = value


def masked_phone(phone: str) -> str:
    if len(phone) <= 6:
        return phone
    return phone[:3] + "******" + phone[-4:]


def render_otp_page():
    st.markdown("## 🔐 Principal OTP Verification")
    st.caption(f"OTP sent to {masked_phone(st.session_state.otp_phone)}")

    if otp_test_mode() and st.session_state.get("otp_test_value"):
        st.info(f"Testing OTP: {st.session_state.otp_test_value}")

    otp_input = st.text_input("Enter 6-digit OTP", max_chars=6, key="principal_otp_input")
    verify_col, resend_col, cancel_col = st.columns(3)

    if verify_col.button("Verify OTP", type="primary", use_container_width=True):
        if time.time() > st.session_state.otp_expires_at:
            st.error("OTP expired. Please resend a new OTP.")
        elif st.session_state.otp_attempts >= OTP_MAX_ATTEMPTS:
            st.error("Too many wrong OTP attempts. Please resend a new OTP.")
        elif not re.fullmatch(r"\d{6}", otp_input.strip()):
            st.error("Enter the 6-digit OTP.")
        elif not hmac.compare_digest(hash_otp(otp_input.strip()), st.session_state.otp_hash):
            st.session_state.otp_attempts += 1
            remaining = OTP_MAX_ATTEMPTS - st.session_state.otp_attempts
            st.error(f"Incorrect OTP. {remaining} attempt(s) remaining.")
        else:
            db = SessionLocal()
            try:
                user = db.query(User).filter(User.user_id == st.session_state.otp_user_id).first()
                if not user:
                    st.error("User account not found.")
                    return
                user.phone_verified = 1
                db.commit()
                clear_otp_state()
                create_authenticated_session(user)
                write_audit_log(
                    "LOGIN_SUCCESS", "Principal login completed with OTP.",
                    entity_type="user", entity_id=user.user_id,
                    school_code=user.school_code, username=user.username, role=user.role,
                )
                st.success("✅ OTP verified. Login successful!")
                st.rerun()
            finally:
                db.close()

    if resend_col.button("Resend OTP", use_container_width=True):
        wait = OTP_RESEND_SECONDS - int(time.time() - st.session_state.otp_last_sent_at)
        if wait > 0:
            st.warning(f"Please wait {wait} seconds before resending.")
        else:
            db = SessionLocal()
            try:
                user = db.query(User).filter(User.user_id == st.session_state.otp_user_id).first()
                if not user:
                    st.error("User account not found.")
                    return
                start_principal_otp(user)
                st.success("New OTP sent.")
                st.rerun()
            except Exception as exc:
                st.error(str(exc))
            finally:
                db.close()

    if cancel_col.button("Cancel", use_container_width=True):
        clear_otp_state()
        st.rerun()


# =========================================================
# LOGIN PAGE
# =========================================================

def login_page():
    st.markdown("""
    <style>
    [data-testid="stSidebar"], [data-testid="collapsedControl"] {display: none !important;}

    .stApp {
        background:
            radial-gradient(circle at 10% 12%, rgba(59,130,246,.26), transparent 28%),
            radial-gradient(circle at 88% 16%, rgba(168,85,247,.18), transparent 30%),
            radial-gradient(circle at 82% 88%, rgba(20,184,166,.20), transparent 28%),
            linear-gradient(135deg, #eef4ff 0%, #f8fbff 42%, #effcf8 100%);
        min-height: 100vh;
    }

    .stApp:before {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        background-image:
            linear-gradient(rgba(30,64,175,.035) 1px, transparent 1px),
            linear-gradient(90deg, rgba(30,64,175,.035) 1px, transparent 1px);
        background-size: 34px 34px;
        mask-image: linear-gradient(to bottom, rgba(0,0,0,.55), transparent 85%);
    }

    .block-container {
        max-width: 1180px;
        padding-top: 5vh;
        padding-bottom: 2rem;
    }

    .school-hero {
        min-height: 560px;
        padding: 48px 42px;
        border-radius: 32px;
        color: white;
        position: relative;
        overflow: hidden;
        background:
            radial-gradient(circle at 85% 15%, rgba(96,165,250,.42), transparent 27%),
            radial-gradient(circle at 12% 88%, rgba(45,212,191,.22), transparent 28%),
            linear-gradient(145deg, #0b1220 0%, #172554 48%, #1d4ed8 100%);
        box-shadow: 0 30px 70px rgba(23,37,84,.30);
        border: 1px solid rgba(255,255,255,.14);
    }

    .school-hero:before {
        content: "";
        position: absolute;
        width: 330px;
        height: 330px;
        border-radius: 50%;
        right: -135px;
        top: -110px;
        border: 52px solid rgba(255,255,255,.055);
    }

    .school-hero:after {
        content: "";
        position: absolute;
        width: 190px;
        height: 190px;
        border-radius: 50%;
        left: -85px;
        bottom: -95px;
        background: rgba(45,212,191,.10);
        border: 1px solid rgba(255,255,255,.10);
    }

    .hero-brand {
        position: relative;
        z-index: 2;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-size: 15px;
        font-weight: 850;
        letter-spacing: .11em;
        color: #dbeafe;
        background: rgba(255,255,255,.09);
        border: 1px solid rgba(255,255,255,.14);
        padding: 9px 13px;
        border-radius: 999px;
    }

    .hero-icon {
        position: relative;
        z-index: 2;
        font-size: 68px;
        margin: 58px 0 10px;
        filter: drop-shadow(0 10px 22px rgba(0,0,0,.18));
    }

    .hero-title {
        position: relative;
        z-index: 2;
        font-size: clamp(34px, 3.6vw, 50px);
        line-height: 1.12;
        letter-spacing: -.04em;
        font-weight: 900;
        max-width: 470px;
    }

    .hero-copy {
        position: relative;
        z-index: 2;
        font-size: 16px;
        line-height: 1.75;
        color: #dbeafe;
        max-width: 440px;
        margin-top: 19px;
    }

    .hero-tags {
        position: relative;
        z-index: 2;
        margin-top: 42px;
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }

    .hero-tags span {
        background: rgba(255,255,255,.10);
        border: 1px solid rgba(255,255,255,.16);
        padding: 9px 13px;
        border-radius: 999px;
        font-size: 13px;
        color: #eff6ff;
        backdrop-filter: blur(7px);
    }

    .login-intro {margin: 16px 0 20px;}
    .login-eyebrow {
        color: #2563eb;
        font-size: 12px;
        font-weight: 900;
        letter-spacing: .14em;
    }
    .login-heading {
        font-size: 38px;
        font-weight: 900;
        color: #0f172a;
        letter-spacing: -.035em;
        margin: 8px 0 8px;
    }
    .login-detail {
        font-size: 15px;
        color: #64748b;
        line-height: 1.65;
        max-width: 470px;
    }

    [data-testid="stTabs"] {
        background: rgba(255,255,255,.72);
        border: 1px solid rgba(148,163,184,.24);
        box-shadow: 0 24px 55px rgba(15,23,42,.12);
        border-radius: 24px;
        padding: 14px 14px 18px;
        backdrop-filter: blur(16px);
    }

    [data-baseweb="tab-list"] {
        gap: 8px;
        background: #eef2ff;
        padding: 6px;
        border-radius: 14px;
        margin-bottom: 14px;
    }

    [data-baseweb="tab"] {
        flex: 1;
        justify-content: center;
        min-height: 46px;
        border-radius: 10px !important;
        font-weight: 750 !important;
        color: #475569 !important;
    }

    [data-baseweb="tab"][aria-selected="true"] {
        background: white !important;
        color: #1d4ed8 !important;
        box-shadow: 0 5px 16px rgba(30,64,175,.12);
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 18px !important;
        border: 1px solid #e5e7eb !important;
        background: rgba(255,255,255,.78) !important;
        box-shadow: none !important;
    }

    .stTextInput input {
        min-height: 48px;
        border-radius: 12px !important;
        border: 1px solid #dbe2ea !important;
        background: rgba(255,255,255,.94) !important;
    }

    .stTextInput input:focus {
        border-color: #60a5fa !important;
        box-shadow: 0 0 0 3px rgba(59,130,246,.12) !important;
    }

    .stButton > button[kind="primary"] {
        min-height: 49px;
        border: 0 !important;
        border-radius: 12px !important;
        font-weight: 850 !important;
        background: linear-gradient(90deg, #2563eb, #4f46e5) !important;
        box-shadow: 0 10px 22px rgba(37,99,235,.25) !important;
        transition: transform .18s ease, box-shadow .18s ease;
    }

    .stButton > button[kind="primary"]:hover {
        transform: translateY(-1px);
        box-shadow: 0 14px 28px rgba(37,99,235,.30) !important;
    }

    .login-foot {
        text-align: center;
        color: #64748b;
        font-size: 12px;
        margin-top: 24px;
        letter-spacing: .02em;
    }

    @media (max-width: 768px) {
        .block-container {padding: 1rem .85rem 2rem;}
        .school-hero {min-height: 0; padding: 28px; border-radius: 24px;}
        .hero-icon {margin: 22px 0 8px; font-size: 46px;}
        .hero-title {font-size: 31px;}
        .hero-copy {font-size: 14px;}
        .hero-tags {margin-top: 22px;}
        .login-heading {font-size: 31px;}
        [data-testid="stTabs"] {border-radius: 20px; padding: 10px 10px 14px;}
    }
    </style>
    """, unsafe_allow_html=True)

    hero, form = st.columns([1.12, 1], gap="large", vertical_alignment="center")
    with hero:
        st.markdown("""
        <div class="school-hero">
            <div class="hero-brand">✦ SCHOOL AI · SECURE PORTAL</div>
            <div class="hero-icon">🏫</div>
            <div class="hero-title">Smart school access, built for everyday work.</div>
            <div class="hero-copy">Attendance, parent communication, analytics and AI support in one secure school workspace.</div>
            <div class="hero-tags"><span>✓ Attendance</span><span>📨 Parent Alerts</span><span>▥ Analytics</span><span>✦ AI Assistant</span></div>
        </div>
        """, unsafe_allow_html=True)

    with form:
        st.markdown("""
        <div class="login-intro">
            <div class="login-eyebrow">SECURE SCHOOL ACCESS</div>
            <div class="login-heading">Welcome to School AI</div>
            <div class="login-detail">Staff, parents and the platform Super Admin use Sign in. Principal Registration is only for an authorized school principal.</div>
        </div>
        """, unsafe_allow_html=True)

        signin_tab, forgot_tab, register_tab = st.tabs(["🔐 Sign in", "🔑 Forgot Password", "📝 Principal Registration"])

        with signin_tab:
            with st.container(border=True):
                reset_success = st.session_state.pop("password_reset_success", "")
                if reset_success:
                    st.success(reset_success)
                username = st.text_input("Username", placeholder="Your username", key="login_username")
                password = st.text_input("Password", type="password", placeholder="Your password", key="login_password")
                login_clicked = st.button("Sign in →", type="primary", use_container_width=True, key="login_submit")

                if login_clicked:
                    now = time.time()

                    if now < st.session_state.locked_until:
                        remaining = int(st.session_state.locked_until - now)
                        minutes = remaining // 60
                        seconds = remaining % 60
                        st.error(f"🔒 Too many failed attempts. Try again in {minutes}m {seconds}s.")
                        return

                    is_super_admin = super_admin_credentials_valid(username, password)
                    user = None
                    parent = None
                    account_active = True

                    db = SessionLocal()
                    try:
                        if not is_super_admin:
                            user = db.query(User).filter(
                                func.lower(User.username) == username.strip().lower()
                            ).first()
                            valid_login = bool(user) and verify_password(password, user.password_hash)
                            if not valid_login:
                                parent = find_parent_account(db, username)
                                valid_login = bool(parent) and verify_password(password, parent["password_hash"])
                            if valid_login:
                                account_school_code = user.school_code if user else parent["school_code"]
                                account_active = school_is_active(db, account_school_code)
                        else:
                            valid_login = True
                    finally:
                        db.close()

                    if valid_login and not account_active:
                        st.error("🏫 This school is currently inactive. Please contact the School AI administrator.")
                    elif valid_login:
                        if is_super_admin:
                            create_super_admin_session(username)
                            write_audit_log(
                                "LOGIN_SUCCESS", "Super Admin login successful.",
                                entity_type="user", entity_id="super-admin",
                                school_code="", username=username, role="super_admin",
                            )
                            st.success("✅ Super Admin login successful!")
                            st.rerun()
                        elif user and str(user.role).strip().lower() == "principal":
                            try:
                                start_principal_otp(user)
                                st.rerun()
                            except Exception as exc:
                                st.error(f"Could not send OTP: {exc}")
                        elif user:
                            create_authenticated_session(user)
                            write_audit_log(
                                "LOGIN_SUCCESS", "Staff login successful.",
                                entity_type="user", entity_id=user.user_id,
                                school_code=user.school_code, username=user.username, role=user.role,
                            )
                            st.success("✅ Login successful!")
                            st.rerun()
                        else:
                            create_parent_authenticated_session(parent)
                            write_audit_log(
                                "LOGIN_SUCCESS", "Parent login successful.",
                                entity_type="parent", entity_id=parent["user_id"],
                                school_code=parent["school_code"], username=parent["username"], role="parent",
                            )
                            st.success("✅ Parent login successful!")
                            st.rerun()
                    else:
                        st.session_state.failed_attempts += 1
                        attempts_left = MAX_LOGIN_ATTEMPTS - st.session_state.failed_attempts
                        if attempts_left <= 0:
                            st.session_state.locked_until = time.time() + LOCKOUT_SECONDS
                            st.error("🔒 Too many failed password attempts. Login is locked for 5 minutes.")
                        else:
                            st.error(f"❌ Invalid username or password. {attempts_left} attempt(s) remaining.")

        with forgot_tab:
            with st.container(border=True):
                st.markdown("#### 🔑 Reset your password")
                st.caption("Use your username. We will send an OTP to the registered mobile number.")

                reset_stage = st.session_state.get("reset_stage", "")

                if not reset_stage:
                    reset_username_input = st.text_input(
                        "Username",
                        placeholder="Enter your login username",
                        key="reset_username_input",
                    )
                    if st.button(
                        "Send Reset OTP →",
                        type="primary",
                        use_container_width=True,
                        key="send_reset_otp",
                    ):
                        try:
                            start_password_reset(reset_username_input)
                            st.success("OTP sent to your registered mobile number.")
                            st.rerun()
                        except Exception as exc:
                            st.error(str(exc))

                elif reset_stage == "verify":
                    st.info(
                        f"OTP sent to {masked_phone(st.session_state.reset_phone)} "
                        f"for @{st.session_state.reset_username}."
                    )
                    if otp_test_mode() and st.session_state.get("reset_otp_test_value"):
                        st.info(f"Testing OTP: {st.session_state.reset_otp_test_value}")

                    reset_otp_input = st.text_input(
                        "Enter 6-digit OTP",
                        max_chars=6,
                        key="reset_otp_input",
                    )
                    verify_col, resend_col = st.columns(2)

                    if verify_col.button(
                        "Verify OTP",
                        type="primary",
                        use_container_width=True,
                        key="verify_reset_otp",
                    ):
                        if time.time() > st.session_state.reset_otp_expires_at:
                            st.error("OTP expired. Please resend a new OTP.")
                        elif st.session_state.reset_otp_attempts >= OTP_MAX_ATTEMPTS:
                            st.error("Too many wrong OTP attempts. Please resend a new OTP.")
                        elif not re.fullmatch(r"\d{6}", reset_otp_input.strip()):
                            st.error("Enter the 6-digit OTP.")
                        elif not hmac.compare_digest(
                            hash_otp(reset_otp_input.strip()),
                            st.session_state.reset_otp_hash,
                        ):
                            st.session_state.reset_otp_attempts += 1
                            remaining = OTP_MAX_ATTEMPTS - st.session_state.reset_otp_attempts
                            st.error(f"Incorrect OTP. {remaining} attempt(s) remaining.")
                        else:
                            st.session_state.reset_stage = "new_password"
                            st.rerun()

                    if resend_col.button(
                        "Resend OTP",
                        use_container_width=True,
                        key="resend_reset_otp",
                    ):
                        wait = OTP_RESEND_SECONDS - int(
                            time.time() - st.session_state.reset_otp_last_sent_at
                        )
                        if wait > 0:
                            st.warning(f"Please wait {wait} seconds before resending.")
                        else:
                            try:
                                resend_password_reset_otp()
                                st.success("New OTP sent.")
                                st.rerun()
                            except Exception as exc:
                                st.error(str(exc))

                    if st.button("Cancel password reset", key="cancel_password_reset"):
                        clear_password_reset_state()
                        st.rerun()

                elif reset_stage == "new_password":
                    st.success("✅ OTP verified. Create your new password.")
                    st.caption(f"Account: @{st.session_state.reset_username}")
                    reset_new_password = st.text_input(
                        "New password",
                        type="password",
                        key="reset_new_password",
                    )
                    reset_confirm_password = st.text_input(
                        "Confirm new password",
                        type="password",
                        key="reset_confirm_password",
                    )
                    if st.button(
                        "Update Password",
                        type="primary",
                        use_container_width=True,
                        key="update_reset_password",
                    ):
                        if len(reset_new_password) < 8:
                            st.error("Password must be at least 8 characters.")
                        elif reset_new_password != reset_confirm_password:
                            st.error("Passwords do not match.")
                        else:
                            try:
                                update_reset_password(reset_new_password)
                                username_done = st.session_state.reset_username
                                clear_password_reset_state()
                                st.session_state.password_reset_success = (
                                    f"✅ Password updated for @{username_done}. You can sign in now."
                                )
                                st.rerun()
                            except Exception as exc:
                                st.error(f"Could not update password: {exc}")

        with register_tab:
            with st.container(border=True):
                st.caption("Only an authorized school principal should create this account.")
                reg_name = st.text_input("Principal full name", key="reg_name")
                reg_username = st.text_input("Create username", key="reg_username")
                reg_phone = st.text_input("Mobile number", placeholder="+919876543210", key="reg_phone")
                reg_school_code = st.text_input(
                    "School code",
                    value=os.getenv("SCHOOL_CODE", "SCHOOL001"),
                    key="reg_school_code",
                )
                reg_password = st.text_input("Create password", type="password", key="reg_password")
                reg_confirm = st.text_input("Confirm password", type="password", key="reg_confirm")
                reg_code = st.text_input("Principal registration code", type="password", key="reg_code")
                st.caption("The registration code is stored in .env as PRINCIPAL_REGISTRATION_CODE.")

                register_clicked = st.button(
                    "Create Principal Account →",
                    type="primary",
                    use_container_width=True,
                    key="register_principal_submit",
                )

                if register_clicked:
                    configured_code = os.getenv("PRINCIPAL_REGISTRATION_CODE", "").strip()
                    name = reg_name.strip()
                    new_username = reg_username.strip()
                    phone = reg_phone.strip()
                    school_code = reg_school_code.strip()

                    if not configured_code:
                        st.error("Principal registration is not enabled. Add PRINCIPAL_REGISTRATION_CODE to .env and restart the app.")
                    elif not hmac.compare_digest(reg_code.strip(), configured_code):
                        st.error("Invalid principal registration code.")
                    elif not name or not new_username or not school_code:
                        st.error("Name, username and school code are required.")
                    elif not re.fullmatch(r"[A-Za-z0-9_.-]{4,50}", new_username):
                        st.error("Username must be 4–50 characters and use only letters, numbers, dot, underscore or hyphen.")
                    elif not re.fullmatch(r"\+[1-9]\d{7,14}", phone):
                        st.error("Use mobile format like +919876543210.")
                    elif len(reg_password) < 8:
                        st.error("Password must be at least 8 characters.")
                    elif reg_password != reg_confirm:
                        st.error("Passwords do not match.")
                    else:
                        db = SessionLocal()
                        try:
                            existing = db.query(User).filter(
                                func.lower(User.username) == new_username.lower()
                            ).first()
                            if existing:
                                st.error("This username already exists. Choose another username.")
                            else:
                                password_hash = bcrypt.hashpw(
                                    reg_password.encode("utf-8"), bcrypt.gensalt()
                                ).decode("utf-8")
                                new_user = User(
                                    user_id=f"principal-{secrets.token_hex(6)}",
                                    name=name,
                                    username=new_username,
                                    password_hash=password_hash,
                                    role="principal",
                                    school_code=school_code,
                                    phone=phone,
                                    phone_verified=0,
                                )
                                db.add(new_user)
                                db.commit()
                                db.refresh(new_user)
                                try:
                                    start_principal_otp(new_user)
                                    st.success("✅ Account created. Verify the OTP to finish registration.")
                                    st.rerun()
                                except Exception as exc:
                                    st.warning(
                                        "Account was created, but OTP could not be sent. "
                                        f"You can sign in later after fixing OTP settings. Details: {exc}"
                                    )
                        except Exception as exc:
                            db.rollback()
                            st.error(f"Registration failed: {exc}")
                        finally:
                            db.close()

    st.markdown('<div class="login-foot">🎓 School AI Assistant · Secure school access</div>', unsafe_allow_html=True)


# =========================================================
# CHECK LOGIN
# =========================================================

if st.session_state.get("otp_pending"):
    render_otp_page()
    st.stop()

token = st.query_params.get(SESSION_PARAM)
active_session = session_record(token)
if not active_session:
    # Remove an expired or invalid token and show the login page.
    if token or st.session_state.logged_in:
        clear_login()
    login_page()
    st.stop()

st.session_state.logged_in = True
for field in ("school_code", "school_name", "username", "user_id", "user_name", "role"):
    st.session_state[field] = active_session[field]
st.session_state.parent_student_id = active_session.get("parent_student_id")


@st.fragment(run_every="10s")
def session_countdown():
    current = session_record(st.query_params.get(SESSION_PARAM))
    if not current:
        clear_login()
        st.rerun(scope="app")
    remaining = max(0, int(current["expires_at"] - time.time()))
    st.caption(f"⏱️ Session ends in {remaining // 60:02d}:{remaining % 60:02d}")


# =========================================================
# SUPER ADMIN PORTAL - MULTI-SCHOOL MANAGEMENT
# =========================================================
def render_super_admin_portal():
    with st.sidebar:
        st.markdown("### 🛡️ Super Admin")
        st.success("🌐 School AI Platform")
        st.caption(f"👤 {st.session_state.username}")
        session_countdown()
        if st.button("🚪 Logout", key="super_admin_logout", use_container_width=True):
            write_audit_log("LOGOUT", "Super Admin logged out.")
            clear_login()
            st.rerun()

    st.title("🛡️ Super Admin Dashboard")
    st.caption("Create and manage schools, principals, and school activation status from one place.")

    db = SessionLocal()
    try:
        sync_existing_schools(db)
        ensure_parent_accounts_table(db)
        school_rows = db.execute(select(schools).order_by(schools.c.school_name)).mappings().all()

        all_students = db.query(Student).all()
        all_users = db.query(User).all()
        parent_rows = db.execute(select(parent_accounts)).mappings().all()
    finally:
        db.close()

    active_count = sum(str(row["status"]).lower() == "active" for row in school_rows)
    teacher_count = sum(str(user.role or "").lower() == "teacher" for user in all_users)
    principal_count = sum(str(user.role or "").lower() == "principal" for user in all_users)

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("🏫 Schools", len(school_rows))
    c2.metric("✅ Active", active_count)
    c3.metric("👨‍🎓 Students", len(all_students))
    c4.metric("👩‍🏫 Teachers", teacher_count)
    c5.metric("👨‍👩‍👧 Parents", len(parent_rows))

    st.divider()
    st.subheader("➕ Create New School + Principal")
    st.caption("The Super Admin creates the school first, then its first principal login.")

    with st.form("super_admin_create_school"):
        left, right = st.columns(2)
        with left:
            new_school_name = st.text_input("School name", placeholder="ABC English School")
            new_school_code = st.text_input("School code", placeholder="SCHOOL002")
            principal_name = st.text_input("Principal full name", placeholder="Rahul Patil")
        with right:
            principal_username = st.text_input("Principal username", placeholder="abc_principal")
            principal_phone = st.text_input("Principal mobile", placeholder="+919876543210")
            principal_password = st.text_input("Temporary password", type="password")
        create_school = st.form_submit_button("Create School & Principal", type="primary", use_container_width=True)

    if create_school:
        school_name = new_school_name.strip()
        school_code = new_school_code.strip().upper()
        p_name = principal_name.strip()
        p_username = principal_username.strip()
        p_phone = principal_phone.strip()

        if not school_name or not school_code or not p_name or not p_username:
            st.error("School name, school code, principal name and username are required.")
        elif not re.fullmatch(r"[A-Z0-9_-]{3,30}", school_code):
            st.error("School code must be 3–30 characters using A-Z, 0-9, underscore or hyphen.")
        elif not re.fullmatch(r"[A-Za-z0-9_.-]{4,50}", p_username):
            st.error("Principal username must be 4–50 characters.")
        elif not re.fullmatch(r"\+[1-9]\d{7,14}", p_phone):
            st.error("Use principal mobile format like +919876543210.")
        elif len(principal_password) < 8:
            st.error("Temporary password must be at least 8 characters.")
        else:
            db = SessionLocal()
            try:
                ensure_admin_tables(db)
                school_exists = db.execute(select(schools).where(
                    schools.c.school_code == school_code
                )).first()
                username_exists = db.query(User).filter(
                    func.lower(User.username) == p_username.lower()
                ).first()
                parent_username_exists = find_parent_account(db, p_username)

                if school_exists:
                    st.error("This school code already exists.")
                elif username_exists or parent_username_exists:
                    st.error("This username already exists. Choose another username.")
                else:
                    db.execute(schools.insert().values(
                        school_code=school_code,
                        school_name=school_name,
                        status="active",
                        created_at=datetime.utcnow(),
                    ))
                    password_hash = bcrypt.hashpw(
                        principal_password.encode("utf-8"), bcrypt.gensalt()
                    ).decode("utf-8")
                    values = dict(
                        user_id=f"principal-{secrets.token_hex(6)}",
                        name=p_name,
                        username=p_username,
                        password_hash=password_hash,
                        role="principal",
                        school_code=school_code,
                    )
                    if hasattr(User, "phone"):
                        values["phone"] = p_phone
                    if hasattr(User, "phone_verified"):
                        values["phone_verified"] = 0
                    db.add(User(**values))
                    db.commit()
                    st.success(f"✅ {school_name} created with principal login @{p_username}.")
                    st.info("Share the temporary password securely. The principal can use Forgot Password later if needed.")
                    st.rerun()
            except Exception as exc:
                db.rollback()
                st.error(f"Could not create school: {exc}")
            finally:
                db.close()

    st.divider()
    st.subheader("🏫 Manage Schools")

    if not school_rows:
        st.info("No schools have been created yet.")
        return

    students_by_school = {}
    for student in all_students:
        students_by_school[str(student.school_code)] = students_by_school.get(str(student.school_code), 0) + 1
    teachers_by_school = {}
    principals_by_school = {}
    for user in all_users:
        code = str(user.school_code)
        role = str(user.role or "").lower()
        if role == "teacher":
            teachers_by_school[code] = teachers_by_school.get(code, 0) + 1
        elif role == "principal":
            principals_by_school[code] = principals_by_school.get(code, 0) + 1
    parents_by_school = {}
    for parent in parent_rows:
        code = str(parent["school_code"])
        parents_by_school[code] = parents_by_school.get(code, 0) + 1

    summary_rows = []
    for school in school_rows:
        code = school["school_code"]
        summary_rows.append({
            "School": school["school_name"],
            "Code": code,
            "Status": str(school["status"]).title(),
            "Principals": principals_by_school.get(code, 0),
            "Teachers": teachers_by_school.get(code, 0),
            "Students": students_by_school.get(code, 0),
            "Parents": parents_by_school.get(code, 0),
        })
    st.dataframe(summary_rows, hide_index=True, use_container_width=True)

    school_map = {row["school_code"]: row for row in school_rows}
    selected_code = st.selectbox(
        "Select school to manage",
        list(school_map.keys()),
        format_func=lambda code: f"{school_map[code]['school_name']} ({code})",
    )
    selected = school_map[selected_code]
    current_status = str(selected["status"] or "active").lower()

    st.write(f"**School:** {selected['school_name']}")
    st.write(f"**Code:** {selected_code}")
    st.write(f"**Status:** {'✅ Active' if current_status == 'active' else '⛔ Inactive'}")

    db = SessionLocal()
    try:
        principals = db.query(User).filter(
            User.school_code == selected_code,
            func.lower(User.role) == "principal",
        ).all()
    finally:
        db.close()
    if principals:
        st.caption("Principal(s): " + ", ".join(f"{p.name} (@{p.username})" for p in principals))
    else:
        st.warning("No principal account is linked to this school.")

    if current_status == "active":
        if st.button("⛔ Deactivate School", key="deactivate_school", use_container_width=True):
            db = SessionLocal()
            try:
                ensure_admin_tables(db)
                db.execute(schools.update().where(
                    schools.c.school_code == selected_code
                ).values(status="inactive"))
                db.commit()
                st.success("School deactivated. Its users cannot sign in until reactivated.")
                st.rerun()
            finally:
                db.close()
    else:
        if st.button("✅ Activate School", key="activate_school", type="primary", use_container_width=True):
            db = SessionLocal()
            try:
                ensure_admin_tables(db)
                db.execute(schools.update().where(
                    schools.c.school_code == selected_code
                ).values(status="active"))
                db.commit()
                st.success("School activated.")
                st.rerun()
            finally:
                db.close()


if str(st.session_state.role).strip().lower() == "super_admin":
    render_super_admin_portal()
    st.stop()


# =========================================================
# PARENT PORTAL - RESTRICTED TO ONE CHILD
# =========================================================
def render_parent_portal():
    student_id = st.session_state.get("parent_student_id")
    db = SessionLocal()
    try:
        student = db.query(Student).filter(
            Student.id == student_id,
            Student.school_code == st.session_state.school_code,
        ).first()
        if not student:
            st.error("The student linked to this parent account could not be found. Please contact the school.")
            return
        records = db.query(Attendance).filter(
            Attendance.student_id == student.id
        ).order_by(Attendance.date.desc()).all()
    finally:
        db.close()

    with st.sidebar:
        st.markdown("### 👨‍👩‍👧 Parent Portal")
        st.success(f"🏫 {st.session_state.school_name}")
        st.caption(f"👤 {st.session_state.user_name}")
        st.caption(f"🎓 {student.name} · Class {student.class_name}{student.division or ''}")
        session_countdown()
        if st.button("🚪 Logout", key="parent_logout", use_container_width=True):
            write_audit_log("LOGOUT", "Parent logged out.", entity_type="parent", entity_id=st.session_state.get("user_id"))
            clear_login()
            st.rerun()

    st.title("👨‍👩‍👧 Parent Dashboard")
    st.caption("This account can view only the linked child's attendance information.")

    total_days = int(student.total_days or 0)
    present_days = int(student.present_days or 0)
    absent_days = max(0, total_days - present_days)
    attendance_pct = (present_days / total_days * 100) if total_days else 0.0

    st.subheader(f"🎓 {student.name}")
    st.write(f"**Class:** {student.class_name}{student.division or ''}")
    cols = st.columns(4)
    cols[0].metric("📅 Total Days", total_days)
    cols[1].metric("✅ Present", present_days)
    cols[2].metric("❌ Absent", absent_days)
    cols[3].metric("📊 Attendance", f"{attendance_pct:.1f}%")

    if attendance_pct < 80 and total_days:
        st.warning("⚠️ Attendance is below 80%. Please contact the school if you need clarification.")
    elif total_days:
        st.success("✅ Attendance is 80% or above.")

    st.divider()
    st.subheader("🗓️ Recent Attendance")
    if records:
        recent = [
            {"Date": r.date.strftime("%d %b %Y"), "Status": str(r.status).title()}
            for r in records[:31]
        ]
        st.dataframe(recent, hide_index=True, use_container_width=True)
    else:
        st.info("No daily attendance records are available yet.")

    today = date.today()
    st.divider()
    st.subheader("📅 School Calendar")
    upcoming = load_school_calendar(
        st.session_state.school_code,
        start_date=date.today(),
        end_date=date.today() + timedelta(days=60),
    )
    if upcoming:
        st.dataframe([
            {
                "Date": row["event_date"].strftime("%d %b %Y"),
                "Type": row["event_type"],
                "Title": row["title"],
            }
            for row in upcoming[:10]
        ], hide_index=True, use_container_width=True)
    else:
        st.info("No upcoming school calendar entries in the next 60 days.")

    st.divider()
    st.subheader("📆 Monthly Summary")
    month_records = [r for r in records if r.date.year == today.year and r.date.month == today.month]
    month_present = sum(str(r.status).lower() == "present" for r in month_records)
    month_absent = sum(str(r.status).lower() == "absent" for r in month_records)
    month_total = len(month_records)
    month_pct = (month_present / month_total * 100) if month_total else 0.0
    mc = st.columns(3)
    mc[0].metric(today.strftime("%B %Y") + " Marked Days", month_total)
    mc[1].metric("Present", month_present)
    mc[2].metric("Attendance", f"{month_pct:.1f}%")
    if month_total:
        st.caption(f"Absent this month: {month_absent}")
    else:
        st.info("No attendance has been marked for this student this month.")

    st.divider()
    st.subheader("📝 Marks & Report Card")
    result_rows = load_student_results(st.session_state.school_code, student_id=student.id)
    if result_rows:
        exam_keys = []
        for row in result_rows:
            key = (row["academic_year"], row["exam_name"])
            if key not in exam_keys:
                exam_keys.append(key)
        selected_result_exam = st.selectbox(
            "Select report", exam_keys,
            format_func=lambda item: f"{item[0]} · {item[1]}",
            key="parent_result_exam_select",
        )
        selected_rows = [
            row for row in result_rows
            if (row["academic_year"], row["exam_name"]) == selected_result_exam
        ]
        total_obtained, total_max, result_pct = result_summary(selected_rows)
        st.dataframe([
            {
                "Subject": row["subject_name"],
                "Marks": int(row["marks_obtained"]),
                "Out of": int(row["max_marks"]),
                "%": round((int(row["marks_obtained"]) / int(row["max_marks"]) * 100), 1) if int(row["max_marks"]) else 0,
                "Remarks": row.get("remarks") or "",
            }
            for row in selected_rows
        ], hide_index=True, use_container_width=True)
        rc_cols = st.columns(3)
        rc_cols[0].metric("Total", total_obtained)
        rc_cols[1].metric("Out of", total_max)
        rc_cols[2].metric("Percentage", f"{result_pct:.1f}%")
        try:
            report_bytes = build_student_report_card_pdf(
                st.session_state.school_name, st.session_state.school_code, student,
                selected_result_exam[0], selected_result_exam[1], selected_rows,
            )
            safe_exam = re.sub(r"[^A-Za-z0-9_-]+", "_", selected_result_exam[1]).strip("_") or "exam"
            st.download_button(
                "📥 Download Report Card PDF",
                data=report_bytes,
                file_name=f"{student.name.replace(' ', '_')}_{safe_exam}_report_card.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="parent_report_card_download",
            )
        except Exception as exc:
            st.warning(f"Report card PDF is unavailable: {exc}")
    else:
        st.info("No marks/results have been published for this student yet.")


if str(st.session_state.role).strip().lower() == "parent":
    render_parent_portal()
    st.stop()


# =========================================================
# DATABASE HELPERS
# =========================================================

def load_attendance_from_db():
    db = SessionLocal()

    try:
        rows = (
            db.query(
                Student.id,
                Student.name,
                Student.class_name,
                Student.division,
                Attendance.date,
                Attendance.status
            )
            .join(
                Attendance,
                Attendance.student_id == Student.id
            )
           .filter(
                 Student.school_code
                 == st.session_state.school_code
             )
            .order_by(Student.name, Attendance.date)


            .all()
           

            
        )

        data = []

        for row in rows:
            data.append({
                "id": row.id,
                "name": row.name,
                "class": row.class_name,
                "division": row.division,
                "date": row.date,
                "status": row.status
            })

        return data

    finally:
        db.close()

def get_student_summary():
    db = SessionLocal()

    try:
        students = (
            db.query(Student)
            .filter(Student.school_code == st.session_state.school_code)
            .order_by(Student.name)
            .all()
        )

        result = []

        for student in students:
            total_days = student.total_days or 0
            present_days = student.present_days or 0

            percentage = (
                (present_days / total_days) * 100
                if total_days
                else 0
            )

            result.append({
                "id": student.id,
                "name": student.name,
                "class": student.class_name,
                "division": student.division,
                "gender": student.gender,
                "total_days": int(total_days),
                "present_days": int(present_days),
                "attendance_percentage": percentage,

            })

        return result

    finally:
        db.close()


# Teacher assignments are stored beside the existing school tables.
assignment_metadata = MetaData()
teacher_assignments = Table(
    "class_teacher_assignments", assignment_metadata,
    Column("school_code", String(100), primary_key=True),
    Column("class_name", String(100), primary_key=True),
    Column("division", String(100), primary_key=True),
    Column("teacher_name", String(200), nullable=False),
)


def load_teacher_assignments():
    db = SessionLocal()
    try:
        assignment_metadata.create_all(db.get_bind(), tables=[teacher_assignments], checkfirst=True)
        rows = db.execute(select(teacher_assignments).where(
            teacher_assignments.c.school_code == st.session_state.school_code
        )).mappings().all()
        return {(row["class_name"], row["division"]): row["teacher_name"] for row in rows}
    finally:
        db.close()


def load_teacher_accounts():
    """Return teacher accounts for the current school, keyed by username."""
    db = SessionLocal()
    try:
        teachers = db.query(User).filter(
            User.school_code == st.session_state.school_code,
            func.lower(User.role) == "teacher",
        ).order_by(User.name, User.username).all()
        return {
            teacher.username: {
                "user_id": teacher.user_id,
                "name": teacher.name,
                "username": teacher.username,
            }
            for teacher in teachers
        }
    finally:
        db.close()


def get_allowed_teacher_groups():
    """Return class/division groups the logged-in teacher may access."""
    if str(st.session_state.role).strip().lower() != "teacher":
        return None
    username = str(st.session_state.username or "").strip().lower()
    full_name = str(st.session_state.user_name or "").strip().lower()
    assignments = load_teacher_assignments()
    allowed = set()
    for group, assigned_value in assignments.items():
        assigned = str(assigned_value or "").strip().lower()
        # New assignments store username. Full-name matching keeps old assignments working.
        if assigned and assigned in {username, full_name}:
            allowed.add((str(group[0]), str(group[1] or "")))
    return allowed


def teacher_display_name(assignment_value):
    """Convert a stored teacher username to a friendly display name."""
    value = str(assignment_value or "").strip()
    if not value:
        return "Not assigned"
    accounts = load_teacher_accounts()
    account = accounts.get(value)
    if account:
        return f"{account['name']} (@{account['username']})"
    return value


def load_today_class_status(school_code, groups):
    """Return attendance progress for today's roster, scoped to this school."""
    db = SessionLocal()
    try:
        students = db.query(Student).filter(Student.school_code == school_code).all()
        student_ids = [student.id for student in students]
        records = db.query(Attendance).filter(
            Attendance.student_id.in_(student_ids), Attendance.date == date.today()
        ).all() if student_ids else []
        statuses = {record.student_id: str(record.status).lower() for record in records}
        by_group = {}
        for student in students:
            group = (str(student.class_name), str(student.division or ""))
            by_group.setdefault(group, []).append(student.id)
        return {
            group: {
                "students": len(by_group.get(group, [])),
                "marked": sum(sid in statuses for sid in by_group.get(group, [])),
                "absent": sum(statuses.get(sid) == "absent" for sid in by_group.get(group, [])),
            }
            for group in groups
        }
    finally:
        db.close()


def get_three_day_absences(school_code):
    """Find pupils absent on the latest three distinct recorded days of their class."""
    db = SessionLocal()
    try:
        groups = db.query(Student.class_name, Student.division).filter(
            Student.school_code == school_code
        ).distinct().all()
        candidates = []
        for class_name, division in groups:
            students = db.query(Student).filter(
                Student.school_code == school_code,
                Student.class_name == class_name,
                Student.division == division,
            ).all()
            if not students:
                continue
            ids = [student.id for student in students]
            days = [row[0] for row in db.query(Attendance.date).filter(
                Attendance.student_id.in_(ids),
            ).distinct().order_by(Attendance.date.desc()).limit(3).all()]
            if len(days) != 3:
                continue
            records = db.query(Attendance.student_id, Attendance.date, Attendance.status).filter(
                Attendance.student_id.in_(ids), Attendance.date.in_(days),
            ).all()
            statuses = {(student_id, day): str(status).lower()
                        for student_id, day, status in records}
            for student in students:
                if all(statuses.get((student.id, day)) == "absent" for day in days):
                    candidates.append({
                        "id": student.id,
                        "name": student.name,
                        "class": class_name,
                        "division": division,
                        "parent_contact": student.parent_contact or "",
                        "dates": sorted(days),
                    })
        return candidates
    finally:
        db.close()


# =========================================================
# SAFE PARENT ALERT AGENT
# =========================================================

def safe_parent_alert_agent(school_code):
    """
    Safe approval mode:
    - Reads attendance only
    - Finds 3-day absences
    - Creates message drafts
    - DOES NOT automatically send messages
    """

    candidates = get_three_day_absences(school_code)

    if str(st.session_state.role).strip().lower() == "teacher":
        allowed_groups = get_allowed_teacher_groups() or set()
        candidates = [
            student for student in candidates
            if (str(student["class"]), str(student["division"] or "")) in allowed_groups
        ]

    alerts = []

    for student in candidates:

        phone = (student.get("parent_contact") or "").strip()

        message = (
            f"Dear Parent, {student['name']} has been absent for "
            f"three consecutive recorded school days "
            f"({', '.join(d.strftime('%d %b %Y') for d in student['dates'])}). "
            f"Please contact Mahatma Gandhi English School."
        )

        alerts.append({
            "student_id": student["id"],
            "student_name": student["name"],
            "class": student["class"],
            "division": student["division"],
            "phone": phone,
            "message": message,
            "dates": student["dates"],
        })

    return alerts


# =========================================================
# MONTHLY PDF ATTENDANCE REPORT
# =========================================================

def build_monthly_attendance_pdf(school_code, school_name, year, month, groups):
    """Build a monthly attendance PDF for the requested class/division groups."""
    from io import BytesIO
    import calendar

    try:
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_CENTER
        from reportlab.lib.pagesizes import A4, landscape
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import mm
        from reportlab.platypus import (
            SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
        )
    except ImportError as exc:
        raise RuntimeError(
            "ReportLab is not installed. Run: python -m pip install reportlab"
        ) from exc

    month_start = date(int(year), int(month), 1)
    month_end = date(int(year), int(month), calendar.monthrange(int(year), int(month))[1])
    month_label = month_start.strftime("%B %Y")

    normalized_groups = {(str(c), str(d or "")) for c, d in groups}
    if not normalized_groups:
        raise RuntimeError("No class/division selected for the report.")

    db = SessionLocal()
    try:
        students = db.query(Student).filter(
            Student.school_code == school_code
        ).order_by(Student.class_name, Student.division, Student.name).all()
        students = [
            student for student in students
            if (str(student.class_name), str(student.division or "")) in normalized_groups
        ]

        student_ids = [student.id for student in students]
        records = []
        if student_ids:
            records = db.query(Attendance).filter(
                Attendance.student_id.in_(student_ids),
                Attendance.date >= month_start,
                Attendance.date <= month_end,
            ).all()
    finally:
        db.close()

    by_student = {}
    for record in records:
        status = str(record.status or "").strip().lower()
        bucket = by_student.setdefault(record.student_id, {"present": 0, "absent": 0, "marked": 0})
        if status in ("present", "absent"):
            bucket[status] += 1
            bucket["marked"] += 1

    students_by_group = {}
    for student in students:
        group = (str(student.class_name), str(student.division or ""))
        students_by_group.setdefault(group, []).append(student)

    teacher_map = load_teacher_assignments()
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=landscape(A4),
        rightMargin=12 * mm, leftMargin=12 * mm,
        topMargin=12 * mm, bottomMargin=12 * mm,
        title=f"Monthly Attendance Report - {month_label}",
        author=str(school_name or school_code),
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "ReportTitle", parent=styles["Title"], alignment=TA_CENTER,
        fontSize=18, leading=22, spaceAfter=5
    )
    subtitle_style = ParagraphStyle(
        "ReportSubTitle", parent=styles["Normal"], alignment=TA_CENTER,
        fontSize=10, leading=13, textColor=colors.HexColor("#475569")
    )
    section_style = ParagraphStyle(
        "SectionTitle", parent=styles["Heading2"], fontSize=13,
        leading=16, spaceBefore=8, spaceAfter=6
    )

    story = [
        Paragraph(str(school_name or "School AI"), title_style),
        Paragraph(f"Monthly Attendance Report - {month_label}", subtitle_style),
        Paragraph(
            f"School Code: {school_code} &nbsp;&nbsp; | &nbsp;&nbsp; Generated: {datetime.now():%d %b %Y %I:%M %p}",
            subtitle_style,
        ),
        Spacer(1, 6 * mm),
    ]

    total_students = len(students)
    total_present = sum(by_student.get(s.id, {}).get("present", 0) for s in students)
    total_absent = sum(by_student.get(s.id, {}).get("absent", 0) for s in students)
    total_marked = total_present + total_absent
    overall_pct = (total_present / total_marked * 100) if total_marked else 0

    summary_data = [
        ["Students", "Present Entries", "Absent Entries", "Attendance %"],
        [str(total_students), str(total_present), str(total_absent), f"{overall_pct:.1f}%" if total_marked else "N/A"],
    ]
    summary = Table(summary_data, colWidths=[55 * mm, 55 * mm, 55 * mm, 55 * mm])
    summary.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1D4ED8")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F8FAFC")),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.extend([summary, Spacer(1, 6 * mm)])

    sorted_groups = sorted(normalized_groups, key=lambda g: (g[0], g[1]))
    for index, group in enumerate(sorted_groups):
        group_students = students_by_group.get(group, [])
        class_name, division = group
        assigned_teacher = teacher_display_name(teacher_map.get(group, ""))
        story.append(Paragraph(
            f"Class {class_name}{division} - Teacher: {assigned_teacher}",
            section_style
        ))

        table_data = [["Sr.", "Student Name", "Present", "Absent", "Marked Days", "Attendance %", "Status"]]
        for sr, student in enumerate(group_students, start=1):
            stats = by_student.get(student.id, {"present": 0, "absent": 0, "marked": 0})
            marked = stats["marked"]
            pct = (stats["present"] / marked * 100) if marked else 0
            if not marked:
                status_label = "No records"
                pct_text = "N/A"
            elif pct < 80:
                status_label = "Below 80%"
                pct_text = f"{pct:.1f}%"
            else:
                status_label = "OK"
                pct_text = f"{pct:.1f}%"
            table_data.append([
                str(sr), str(student.name), str(stats["present"]), str(stats["absent"]),
                str(marked), pct_text, status_label
            ])

        if not group_students:
            table_data.append(["-", "No students found", "-", "-", "-", "-", "-"])

        report_table = Table(
            table_data,
            repeatRows=1,
            colWidths=[13 * mm, 72 * mm, 28 * mm, 28 * mm, 32 * mm, 35 * mm, 34 * mm],
        )
        style_commands = [
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0F172A")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 8.5),
            ("ALIGN", (0, 0), (0, -1), "CENTER"),
            ("ALIGN", (2, 1), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#CBD5E1")),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]
        for row_index in range(1, len(table_data)):
            if table_data[row_index][-1] == "Below 80%":
                style_commands.append(("TEXTCOLOR", (6, row_index), (6, row_index), colors.HexColor("#B91C1C")))
                style_commands.append(("FONTNAME", (6, row_index), (6, row_index), "Helvetica-Bold"))
        report_table.setStyle(TableStyle(style_commands))
        story.append(report_table)
        if index < len(sorted_groups) - 1:
            story.append(PageBreak())

    def add_page_number(canvas, doc_obj):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#64748B"))
        canvas.drawRightString(landscape(A4)[0] - 12 * mm, 7 * mm, f"Page {doc_obj.page}")
        canvas.restoreState()

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    buffer.seek(0)
    return buffer.getvalue()


lesson_plans = Table(
    "lesson_plans", assignment_metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("school_code", String(100), nullable=False),
    Column("created_by", String(200), nullable=False),
    Column("class_name", String(100), nullable=False),
    Column("subject", String(200), nullable=False),
    Column("topic", String(300), nullable=False),
    Column("teaching_date", Date, nullable=False),
    Column("periods", Integer, nullable=False),
    Column("plan_text", Text, nullable=False),
    Column("created_at", DateTime, nullable=False),
)


# =========================================================
# LOAD DATABASE DATA
# =========================================================

try:
    student_rows = get_student_summary()
    if str(st.session_state.role).strip().lower() == "teacher":
        allowed_groups = get_allowed_teacher_groups() or set()
        student_rows = [
            row for row in student_rows
            if (str(row["class"]), str(row["division"] or "")) in allowed_groups
        ]
    
except Exception as e:
    st.error(f"❌ Could not load school database: {e}")
    
    st.stop()


   


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.markdown(
    """
    <div style="
        font-size:26px;
        font-weight:800;
        color:white;
        margin-bottom:20px;
    ">
        🎓 School AI
    </div>
    """,
    unsafe_allow_html=True
)

    st.success(
        f"🏫 {st.session_state.school_name}"
    )

    st.caption(
        f"School Code: {st.session_state.school_code}"
    )

    st.caption(
        f"👤 Logged in as: {st.session_state.username}"
    )
    st.caption(
    f"🎭 Role: {st.session_state.role.title()}"
)
 # =========================================================
# ✨ SIDEBAR FEATURES
# =========================================================

st.sidebar.divider()

st.sidebar.markdown(
    """
    <div style="
        font-size:18px;
        font-weight:700;
        margin-bottom:12px;
        color:white;
    ">
        
    </div>
    """,
    unsafe_allow_html=True
)







# =========================================================
# ✨ FEATURES NAVIGATION
# =========================================================

st.sidebar.markdown("### ✨ Features")

if st.sidebar.button("🏠 Dashboard", use_container_width=True):
    st.session_state.current_page = "Dashboard"
    st.rerun()

if st.sidebar.button("✅ Student Attendance", use_container_width=True):
    st.session_state.current_page = "Attendance"
    st.rerun()

if st.sidebar.button("📨 Parent Messages", use_container_width=True):
    st.session_state.current_page = "Parent Messages"
    st.rerun()

if st.sidebar.button("📊 Attendance Analytics", use_container_width=True):
    st.session_state.current_page = "Analytics"
    st.rerun()

if st.sidebar.button("📄 Monthly PDF Report", use_container_width=True):
    st.session_state.current_page = "Monthly Report"
    st.rerun()

if st.sidebar.button("📅 Holiday & School Calendar", use_container_width=True):
    st.session_state.current_page = "Calendar"
    st.rerun()

if st.sidebar.button("📝 Student Marks & Results", use_container_width=True):
    st.session_state.current_page = "Results"
    st.rerun()

if st.sidebar.button("🔎 Student Search", use_container_width=True):
    st.session_state.current_page = "Search"
    st.rerun()

if st.sidebar.button("🤖 AI Assistant", use_container_width=True):
    st.session_state.current_page = "AI"
    st.rerun()

if str(st.session_state.role).strip().lower() == "principal":
    if st.sidebar.button("👩‍🏫 Teacher Management", use_container_width=True):
        st.session_state.current_page = "Teachers"
        st.rerun()
    if st.sidebar.button("👨‍👩‍👧 Parent Management", use_container_width=True):
        st.session_state.current_page = "Parents"
        st.rerun()
    if st.sidebar.button("🔐 Login Protection", use_container_width=True):
        st.session_state.current_page = "Security"
        st.rerun()
    if st.sidebar.button("🧾 Audit Log", use_container_width=True):
        st.session_state.current_page = "Audit"
        st.rerun()




# =========================================================
# 📁 UPLOAD STUDENT CSV
# =========================================================

st.sidebar.divider()

if str(st.session_state.role).strip().lower() == "principal":

    st.sidebar.subheader("📁 Upload Student CSV")

    uploaded_file = st.sidebar.file_uploader(
        "Choose CSV file",
        type=["csv"]
    )

    
    if st.sidebar.button("📥 Import CSV to this School"):

            try:
                import pandas as pd

                if uploaded_file is None:
                    st.sidebar.error("Choose a CSV file before importing.")
                    st.stop()

                df = pd.read_csv(uploaded_file)

                df.columns = (
                    df.columns
                    .astype(str)
                    .str.strip()
                    .str.lower()
                )

                required_columns = {
                    "name",
                    "class",
                    "total_days",
                    "present_days",
                    "gender"
                }

                if not required_columns.issubset(df.columns):

                    missing = (
                        required_columns
                        - set(df.columns)
                    )

                    st.sidebar.error(
                        f"❌ Missing columns: {', '.join(missing)}"
                    )

                else:

                    db = SessionLocal()

                    imported = 0
                    updated = 0

                    for _, row in df.iterrows():

                        name = str(row["name"]).strip()
                        class_value = str(row["class"]).strip()
                        gender = str(row["gender"]).strip()
                        parent_contact = str(row.get("parent_contact", "")).strip()
                        if parent_contact.lower() in ("nan", "none"):
                            parent_contact = ""

                        if not name or not class_value:
                            continue

                        # Prefer a separate division column; support older CSVs
                        # that put it at the end of class (for example, 4A).
                        csv_division = row.get("division", "")
                        csv_division = "" if pd.isna(csv_division) else str(csv_division).strip().upper()
                        if class_value[-1].isalpha() and class_value[:-1].strip().isdigit():
                            class_name = class_value[:-1].strip()
                            suffix_division = class_value[-1].upper()
                        else:
                            class_name = class_value
                            suffix_division = ""
                        division = csv_division or suffix_division

                        existing = (
                            db.query(Student)
                            .filter(
                                Student.name == name,
                                Student.school_code
                                == st.session_state.school_code
                            )
                            .first()
                        )

                        if existing:

                            existing.class_name = class_name
                            existing.division = division
                            existing.gender = gender
                            if parent_contact:
                                existing.parent_contact = parent_contact

                            existing.total_days = int(
                                row["total_days"]
                            )

                            existing.present_days = int(
                                row["present_days"]
                            )

                            updated += 1

                        else:

                            student = Student(
                                name=name,
                                class_name=class_name,
                                division=division,
                                parent_contact=parent_contact,
                                total_days=int(
                                    row["total_days"]
                                ),
                                present_days=int(
                                    row["present_days"]
                                ),
                                gender=gender,
                                school_code=(
                                    st.session_state.school_code
                                )
                            )

                            db.add(student)
                            imported += 1

                    db.commit()
                    db.close()

                    st.sidebar.success(
                        f"✅ Import complete! "
                        f"New: {imported}, "
                        f"Updated: {updated}"
                    )

                    st.rerun()

            except Exception as e:

                st.sidebar.error(
                    f"❌ Import failed: {e}"
                )
    

   
    st.divider()

    st.info(
        f"👨‍🎓 Total Students: {len(student_rows)}"
    )

    st.sidebar.divider()

session_countdown()

if st.sidebar.button("🚪 Logout"):
    write_audit_log("LOGOUT", "User logged out.", entity_type="user", entity_id=st.session_state.get("user_id"))
    clear_login()
    st.rerun()


# Every feature is a separate view with a direct route home.
PAGE_LABELS = {
    "Dashboard": "🏠 Dashboard",
    "Attendance": "✅ Student Attendance",
    "Parent Messages": "📨 Parent Messages",
    "Analytics": "📊 Attendance Analytics",
    "Monthly Report": "📄 Monthly PDF Report",
    "Calendar": "📅 Holiday & School Calendar",
    "Results": "📝 Student Marks & Results",
    "Search": "🔎 Student Search",
    "AI": "🤖 AI Assistant",
    "Teachers": "👩‍🏫 Teacher Management",
    "Parents": "👨‍👩‍👧 Parent Management",
    "Security": "🔐 Login Protection",
    "Audit": "🧾 Audit Log",
}
if (st.session_state.current_page not in PAGE_LABELS or
        (st.session_state.current_page in ("Security", "Teachers", "Parents", "Audit") and
         str(st.session_state.role).strip().lower() != "principal")):
    st.session_state.current_page = "Dashboard"

if st.session_state.current_page != "Dashboard":
    if st.button("← Back to Dashboard", key="back_to_dashboard"):
        st.session_state.current_page = "Dashboard"
        st.rerun()
    st.title(PAGE_LABELS[st.session_state.current_page])

if st.session_state.current_page == "Dashboard":
    st.markdown("""
    <style>
    .dash-hero {border-radius: 24px; padding: 32px 36px; color: white;
        background: radial-gradient(circle at 90% 0%, rgba(96,165,250,.5), transparent 32%),
                    linear-gradient(115deg, #0f172a 0%, #172554 58%, #2563eb 100%);
        box-shadow: 0 18px 36px rgba(23,37,84,.16); margin-bottom: 28px;}
    .dash-kicker {font-size: 12px; font-weight: 800; letter-spacing: .13em; color: #bfdbfe;}
    .dash-title {font-size: clamp(28px, 3vw, 40px); font-weight: 850;
        letter-spacing: -.03em; line-height: 1.2; margin: 12px 0 9px;}
    .dash-subtitle {font-size: 15px; color: #dbeafe; line-height: 1.6;}
    .dash-pill {display: inline-block; border-radius: 100px; margin-top: 22px;
        padding: 8px 13px; background: rgba(255,255,255,.13);
        border: 1px solid rgba(255,255,255,.22); font-size: 13px;}
    .dash-section {font-size: 22px; font-weight: 800; color: #0f172a; margin: 12px 0 3px;}
    .dash-hint {color: #64748b; font-size: 14px; margin-bottom: 16px;}
    .dash-card-icon {font-size: 30px; margin-bottom: 11px;}
    .dash-card-name {font-weight: 800; font-size: 17px; color: #172554; margin-bottom: 6px;}
    .dash-card-description {font-size: 13px; color: #64748b; line-height: 1.5; min-height: 42px;}
    .dash-section-space {height: 18px;}
    @media (max-width: 768px) {.dash-hero {padding: 24px;}}
    </style>
    """, unsafe_allow_html=True)

    display_name = escape(str(st.session_state.user_name or st.session_state.username or "Teacher"))
    today = date.today().strftime("%d %B %Y")
    st.markdown(f"""
    <div class="dash-hero">
        <div class="dash-kicker">✦ SCHOOL AI · DASHBOARD</div>
        <div class="dash-title">Welcome back, {display_name} 👋</div>
        <div class="dash-subtitle">Your school at a glance. Check attendance, explore insights and find students in a few clicks.</div>
        <div class="dash-pill">📅 {today}</div>
    </div>
    """, unsafe_allow_html=True)

    total_students = len(student_rows)
    total_present = sum(row["present_days"] for row in student_rows)
    total_days = sum(row["total_days"] for row in student_rows)
    average_attendance = (total_present / total_days * 100) if total_days else 0
    low_count = sum(1 for row in student_rows if row["attendance_percentage"] < 80)

    st.markdown('<div class="dash-section">📊 Attendance overview</div>', unsafe_allow_html=True)
    st.markdown('<div class="dash-hint">Key numbers from your school records</div>', unsafe_allow_html=True)
    metric_columns = st.columns(4)
    for column, label, value in zip(metric_columns,
                                    ["👨‍🎓 Students", "📈 Attendance rate", "✅ Present days", "⚠️ Below 80%"],
                                    [total_students, f"{average_attendance:.1f}%", total_present, low_count]):
        with column:
            st.metric(label, value)

    st.markdown('<div class="dash-section-space"></div><div class="dash-section">✨ Explore features</div>', unsafe_allow_html=True)
    st.markdown('<div class="dash-hint">Choose where you want to go</div>', unsafe_allow_html=True)
    feature_pages = [
        ("✅", "Student Attendance", "Browse attendance records and download reports.", "Attendance"),
        ("📊", "Attendance Analytics", "See class, gender and monthly attendance trends.", "Analytics"),
        ("📄", "Monthly PDF Report", "Generate a printable monthly attendance report.", "Monthly Report"),
        ("📅", "Holiday & School Calendar", "View holidays, exams, meetings and school events.", "Calendar"),
        ("📝", "Student Marks & Results", "Enter subject-wise marks and generate student report cards.", "Results"),
        ("🔎", "Student Search", "Find a student and view their attendance details.", "Search"),
        ("🤖", "AI Assistant", "Ask questions about student attendance.", "AI"),
    ]
    if str(st.session_state.role).strip().lower() == "principal":
        feature_pages.append(("👩‍🏫", "Teacher Management", "Create teacher logins and assign classes.", "Teachers"))
        feature_pages.append(("👨‍👩‍👧", "Parent Management", "Create parent logins linked to one student.", "Parents"))
        feature_pages.append(("🔐", "Login Protection", "View your school account security settings.", "Security"))
        feature_pages.append(("🧾", "Audit Log", "See logins, attendance changes, deletes and other important actions.", "Audit"))
    for row_start in range(0, len(feature_pages), 3):
        columns = st.columns(3)
        for column, (icon, name, description, page) in zip(columns, feature_pages[row_start:row_start + 3]):
            with column:
                with st.container(border=True):
                    st.markdown(
                        f'<div class="dash-card-icon">{icon}</div>'
                        f'<div class="dash-card-name">{name}</div>'
                        f'<div class="dash-card-description">{description}</div>',
                        unsafe_allow_html=True,
                    )
                    if st.button("Open feature →", key=f"feature_{page}", use_container_width=True):
                        st.session_state.current_page = page
                        st.rerun()

    if total_students:
        st.markdown('<div class="dash-section-space"></div><div class="dash-section">🏫 Class snapshot</div>', unsafe_allow_html=True)
        st.markdown('<div class="dash-hint">Average attendance by class</div>', unsafe_allow_html=True)
        class_totals = {}
        for row in student_rows:
            class_name = str(row["class"])
            present, days = class_totals.get(class_name, (0, 0))
            class_totals[class_name] = (present + row["present_days"], days + row["total_days"])
        class_rates = {name: round(present / days * 100, 1) if days else 0
                       for name, (present, days) in sorted(class_totals.items())}
        st.bar_chart(class_rates)
        try:
            teacher_map = load_teacher_assignments()
            groups = sorted({(str(row["class"]), str(row["division"] or "")) for row in student_rows})
            daily_status = load_today_class_status(st.session_state.school_code, groups)
            if str(st.session_state.role).strip().lower() == "principal":
                completed = sum(daily_status[group]["marked"] == daily_status[group]["students"] for group in groups)
                unassigned = sum(not teacher_map.get(group) for group in groups)
                today_absent = sum(daily_status[group]["absent"] for group in groups)
                today_cols = st.columns(3)
                today_cols[0].metric("Classes marked today", f"{completed}/{len(groups)}")
                today_cols[1].metric("Absent today", today_absent)
                today_cols[2].metric("Teachers to assign", unassigned)
                st.caption("Today's count includes only students whose attendance has been saved.")
            st.dataframe([
                {"Class": f"{class_name}{division}",
                 "Class teacher": teacher_display_name(teacher_map.get((class_name, division), "")),
                 "Students": daily_status[(class_name, division)]["students"],
                 "Marked today": f'{daily_status[(class_name, division)]["marked"]}/{daily_status[(class_name, division)]["students"]}',
                 "Absent today": daily_status[(class_name, division)]["absent"]}
                for class_name, division in groups
            ], hide_index=True, use_container_width=True)
            if str(st.session_state.role).strip().lower() == "principal":
                if st.button("Manage teachers and daily attendance →", key="dashboard_manage_attendance"):
                    st.session_state.current_page = "Attendance"
                    st.rerun()
        except Exception as exc:
            st.warning(f"Class teacher list unavailable: {exc}")
    else:
        st.info("No student records yet. Import a student CSV to get started.")

if st.session_state.current_page == "Calendar":
    import calendar as pycalendar

    st.subheader("📅 Holiday & School Calendar")
    st.caption(
        "Holidays block attendance for that date. Events, exams and meetings are informational and do not block attendance."
    )

    is_principal = str(st.session_state.role).strip().lower() == "principal"

    if is_principal:
        with st.container(border=True):
            st.markdown("#### ➕ Add calendar entry")
            with st.form("add_school_calendar_entry", clear_on_submit=True):
                left, right = st.columns(2)
                with left:
                    cal_date = st.date_input("Date", value=date.today(), key="calendar_add_date")
                    cal_type = st.selectbox(
                        "Type", ["Holiday", "Event", "Exam", "Meeting"], key="calendar_add_type"
                    )
                with right:
                    cal_title = st.text_input("Title", placeholder="Example: Gandhi Jayanti")
                    cal_description = st.text_area("Description (optional)", height=90)
                add_entry = st.form_submit_button("Add to School Calendar", type="primary", use_container_width=True)

            if add_entry:
                title = cal_title.strip()
                if not title:
                    st.error("Enter a title for the calendar entry.")
                else:
                    db = SessionLocal()
                    try:
                        ensure_school_calendar_table(db)
                        duplicate = db.execute(select(school_calendar).where(
                            school_calendar.c.school_code == st.session_state.school_code,
                            school_calendar.c.event_date == cal_date,
                            func.lower(school_calendar.c.title) == title.lower(),
                            func.lower(school_calendar.c.event_type) == cal_type.lower(),
                        )).first()
                        if duplicate:
                            st.warning("This calendar entry already exists for the selected date.")
                        else:
                            db.execute(school_calendar.insert().values(
                                school_code=st.session_state.school_code,
                                event_date=cal_date,
                                title=title,
                                event_type=cal_type,
                                description=cal_description.strip(),
                                created_at=datetime.utcnow(),
                            ))
                            db.commit()
                            write_audit_log(
                                "CALENDAR_CREATE", f"{cal_type}: {cal_title.strip()} on {cal_date}.",
                                entity_type="calendar", entity_id=str(cal_date),
                            )
                            st.success("✅ Calendar entry added.")
                            st.rerun()
                    except Exception as exc:
                        db.rollback()
                        st.error(f"Could not add calendar entry: {exc}")
                    finally:
                        db.close()

    today_cal = date.today()
    filter_col1, filter_col2 = st.columns(2)
    with filter_col1:
        calendar_year = st.selectbox(
            "Year", list(range(today_cal.year - 1, today_cal.year + 3)),
            index=1, key="calendar_filter_year"
        )
    with filter_col2:
        calendar_month = st.selectbox(
            "Month", list(range(1, 13)), index=today_cal.month - 1,
            format_func=lambda m: pycalendar.month_name[m], key="calendar_filter_month"
        )

    month_start = date(calendar_year, calendar_month, 1)
    month_end = date(calendar_year, calendar_month, pycalendar.monthrange(calendar_year, calendar_month)[1])
    entries = load_school_calendar(st.session_state.school_code, month_start, month_end)

    st.markdown(f"#### {pycalendar.month_name[calendar_month]} {calendar_year}")
    if entries:
        rows = [{
            "ID": row["id"],
            "Date": row["event_date"].strftime("%d %b %Y"),
            "Day": row["event_date"].strftime("%A"),
            "Type": row["event_type"],
            "Title": row["title"],
            "Description": row["description"] or "",
        } for row in entries]
        st.dataframe(rows, hide_index=True, use_container_width=True)

        if is_principal:
            with st.expander("🗑️ Remove calendar entry"):
                entry_map = {row["id"]: row for row in entries}
                delete_cal_id = st.selectbox(
                    "Select entry", list(entry_map.keys()),
                    format_func=lambda eid: (
                        f"{entry_map[eid]['event_date']:%d %b %Y} · "
                        f"{entry_map[eid]['event_type']} · {entry_map[eid]['title']}"
                    ),
                    key="delete_calendar_entry_select",
                )
                if st.button("Delete selected calendar entry", key="delete_calendar_entry_button"):
                    db = SessionLocal()
                    try:
                        ensure_school_calendar_table(db)
                        db.execute(school_calendar.delete().where(
                            school_calendar.c.id == int(delete_cal_id),
                            school_calendar.c.school_code == st.session_state.school_code,
                        ))
                        deleted_entry = entry_map.get(delete_cal_id)
                        db.commit()
                        write_audit_log(
                            "CALENDAR_DELETE",
                            (f"Deleted {deleted_entry['event_type']}: {deleted_entry['title']} on {deleted_entry['event_date']}." if deleted_entry else "Deleted calendar entry."),
                            entity_type="calendar", entity_id=delete_cal_id,
                        )
                        st.success("Calendar entry deleted.")
                        st.rerun()
                    except Exception as exc:
                        db.rollback()
                        st.error(f"Could not delete calendar entry: {exc}")
                    finally:
                        db.close()
    else:
        st.info("No holidays or events are saved for this month.")

    upcoming = load_school_calendar(
        st.session_state.school_code,
        start_date=date.today(),
        end_date=date.today() + timedelta(days=30),
    )
    st.divider()
    st.markdown("#### 🔔 Next 30 days")
    if upcoming:
        for row in upcoming[:8]:
            icon = "🏖️" if str(row["event_type"]).lower() == "holiday" else "📌"
            st.write(f"{icon} **{row['event_date']:%d %b %Y}** — {row['title']} ({row['event_type']})")
    else:
        st.caption("No upcoming entries in the next 30 days.")


if st.session_state.current_page == "Audit":
    st.subheader("🧾 Audit Log")
    st.caption("Principal-only history of important actions in this school. Newest records are shown first.")

    logs = load_audit_logs(st.session_state.school_code, limit=1000)
    if not logs:
        st.info("No audit records yet. New login, attendance, delete and management actions will appear here.")
    else:
        action_options = sorted({str(row["action"]) for row in logs})
        user_options = sorted({str(row["username"]) for row in logs})
        c1, c2 = st.columns(2)
        selected_action = c1.selectbox("Action", ["All"] + action_options, key="audit_action_filter")
        selected_user = c2.selectbox("User", ["All"] + user_options, key="audit_user_filter")
        filtered_logs = [
            row for row in logs
            if (selected_action == "All" or row["action"] == selected_action)
            and (selected_user == "All" or row["username"] == selected_user)
        ]
        display_rows = [{
            "Date & Time": row["created_at"].strftime("%d %b %Y %I:%M:%S %p") if row["created_at"] else "",
            "User": row["username"],
            "Role": str(row["role"]).title(),
            "Action": row["action"],
            "Type": row["entity_type"] or "-",
            "Record": row["entity_id"] or "-",
            "Details": row["details"] or "",
        } for row in filtered_logs]
        st.dataframe(display_rows, hide_index=True, use_container_width=True)
        if display_rows:
            audit_csv = pd.DataFrame(display_rows).to_csv(index=False).encode("utf-8")
            st.download_button(
                "📥 Download Audit Log CSV", audit_csv,
                file_name=f"audit_log_{st.session_state.school_code}_{date.today():%Y%m%d}.csv",
                mime="text/csv", use_container_width=True,
            )


if st.session_state.current_page == "Results":
    st.subheader("📝 Student Marks & Result Module")
    st.caption("Enter subject-wise marks, update corrections, preview totals and download a PDF report card.")

    if not student_rows:
        st.info("No students are available for your account. Principal can add students or assign a class to the teacher first.")
    else:
        current_year = date.today().year
        default_academic_year = f"{current_year}-{str(current_year + 1)[-2:]}"
        groups = sorted({(str(row["class"]), str(row["division"] or "")) for row in student_rows})

        entry_tab, upload_tab, report_tab = st.tabs(["✍️ Enter / Update Marks", "📤 Upload Marks CSV", "📄 Report Card"])

        with entry_tab:
            st.markdown("#### Subject-wise marks")
            col_a, col_b = st.columns(2)
            with col_a:
                result_group = st.selectbox(
                    "Class & division", groups,
                    format_func=lambda g: f"Class {g[0]}{g[1]}",
                    key="result_entry_group",
                )
            group_students = [
                row for row in student_rows
                if (str(row["class"]), str(row["division"] or "")) == result_group
            ]
            student_map = {int(row["id"]): row for row in group_students}
            with col_b:
                result_student_id = st.selectbox(
                    "Student", list(student_map.keys()),
                    format_func=lambda sid: student_map[sid]["name"],
                    key="result_entry_student",
                )

            with st.form("student_marks_entry_form"):
                f1, f2 = st.columns(2)
                with f1:
                    academic_year = st.text_input("Academic year", value=default_academic_year, placeholder="2026-27")
                    exam_name = st.text_input("Exam / Term", placeholder="Unit Test 1 / Semester 1")
                    subject_name = st.text_input("Subject", placeholder="Mathematics")
                with f2:
                    max_marks = st.number_input("Maximum marks", min_value=1, max_value=1000, value=100, step=1)
                    marks_obtained = st.number_input("Marks obtained", min_value=0, max_value=1000, value=0, step=1)
                    remarks = st.text_input("Remarks (optional)", placeholder="Good / Needs practice")
                save_marks = st.form_submit_button("Save / Update Marks", type="primary", use_container_width=True)

            if save_marks:
                year = academic_year.strip()
                exam = exam_name.strip()
                subject = subject_name.strip()
                if not year or not exam or not subject:
                    st.error("Academic year, exam/term and subject are required.")
                elif int(marks_obtained) > int(max_marks):
                    st.error("Marks obtained cannot be greater than maximum marks.")
                else:
                    db = SessionLocal()
                    try:
                        ensure_student_results_table(db)
                        existing = db.execute(select(student_results).where(
                            student_results.c.school_code == st.session_state.school_code,
                            student_results.c.student_id == int(result_student_id),
                            func.lower(student_results.c.academic_year) == year.lower(),
                            func.lower(student_results.c.exam_name) == exam.lower(),
                            func.lower(student_results.c.subject_name) == subject.lower(),
                        )).mappings().first()
                        values = dict(
                            school_code=st.session_state.school_code,
                            student_id=int(result_student_id),
                            academic_year=year,
                            exam_name=exam,
                            subject_name=subject,
                            max_marks=int(max_marks),
                            marks_obtained=int(marks_obtained),
                            remarks=remarks.strip(),
                            updated_by=st.session_state.username,
                            updated_at=datetime.utcnow(),
                        )
                        if existing:
                            db.execute(student_results.update().where(
                                student_results.c.id == int(existing["id"])
                            ).values(**values))
                            action = "updated"
                        else:
                            db.execute(student_results.insert().values(**values))
                            action = "saved"
                        db.commit()
                        write_audit_log(
                            "MARKS_UPDATE" if action == "updated" else "MARKS_CREATE",
                            f"{subject}: {int(marks_obtained)}/{int(max_marks)} for {student_map[int(result_student_id)]['name']} · {exam} · {year}",
                            entity_type="student_result", entity_id=(existing["id"] if existing else result_student_id),
                        )
                        st.success(f"✅ {subject} marks {action} for {student_map[int(result_student_id)]['name']}.")
                        st.rerun()
                    except Exception as exc:
                        db.rollback()
                        st.error(f"Could not save marks: {exc}")
                    finally:
                        db.close()

            selected_existing = load_student_results(
                st.session_state.school_code, student_id=int(result_student_id)
            )
            if selected_existing:
                st.markdown("#### Saved marks for this student")
                st.dataframe([
                    {
                        "Academic Year": row["academic_year"],
                        "Exam": row["exam_name"],
                        "Subject": row["subject_name"],
                        "Marks": int(row["marks_obtained"]),
                        "Out of": int(row["max_marks"]),
                        "%": round((int(row["marks_obtained"]) / int(row["max_marks"]) * 100), 1) if int(row["max_marks"]) else 0,
                        "Remarks": row.get("remarks") or "",
                        "Updated By": row.get("updated_by") or "",
                    }
                    for row in selected_existing
                ], hide_index=True, use_container_width=True)

                if str(st.session_state.role).strip().lower() == "principal":
                    with st.expander("🗑️ Delete a marks entry"):
                        row_map = {int(row["id"]): row for row in selected_existing}
                        delete_result_id = st.selectbox(
                            "Select entry", list(row_map.keys()),
                            format_func=lambda rid: (
                                f"{row_map[rid]['academic_year']} · {row_map[rid]['exam_name']} · "
                                f"{row_map[rid]['subject_name']} · {row_map[rid]['marks_obtained']}/{row_map[rid]['max_marks']}"
                            ),
                            key="delete_result_entry_select",
                        )
                        if st.button("Delete selected marks entry", key="delete_result_entry_button"):
                            db = SessionLocal()
                            try:
                                ensure_student_results_table(db)
                                db.execute(student_results.delete().where(
                                    student_results.c.id == int(delete_result_id),
                                    student_results.c.school_code == st.session_state.school_code,
                                ))
                                deleted_row = row_map.get(int(delete_result_id))
                                db.commit()
                                write_audit_log(
                                    "MARKS_DELETE",
                                    (f"Deleted {deleted_row['subject_name']} marks {deleted_row['marks_obtained']}/{deleted_row['max_marks']} "
                                     f"for exam {deleted_row['exam_name']}." if deleted_row else "Deleted marks entry."),
                                    entity_type="student_result", entity_id=delete_result_id,
                                )
                                st.success("Marks entry deleted.")
                                st.rerun()
                            except Exception as exc:
                                db.rollback()
                                st.error(f"Could not delete marks: {exc}")
                            finally:
                                db.close()

        with upload_tab:
            st.markdown("#### 📤 Upload marks from CSV")
            st.caption("Bulk upload subject-wise marks. Existing student/exam/subject entries are updated; new entries are created.")

            template_columns = [
                "student_name", "class", "division", "academic_year", "exam",
                "subject", "max_marks", "marks_obtained", "remarks"
            ]
            template_df = pd.DataFrame([
                {
                    "student_name": "Rohan Patil",
                    "class": "5",
                    "division": "A",
                    "academic_year": default_academic_year,
                    "exam": "Unit Test 1",
                    "subject": "Mathematics",
                    "max_marks": 50,
                    "marks_obtained": 42,
                    "remarks": "Good",
                },
                {
                    "student_name": "Rohan Patil",
                    "class": "5",
                    "division": "A",
                    "academic_year": default_academic_year,
                    "exam": "Unit Test 1",
                    "subject": "Science",
                    "max_marks": 50,
                    "marks_obtained": 45,
                    "remarks": "Very Good",
                },
            ])
            st.download_button(
                "📥 Download Marks CSV Template",
                data=template_df.to_csv(index=False).encode("utf-8"),
                file_name="student_marks_template.csv",
                mime="text/csv",
                use_container_width=True,
                key="download_marks_csv_template",
            )

            marks_csv = st.file_uploader(
                "Choose marks CSV file", type=["csv"], key="marks_csv_uploader"
            )

            if marks_csv is not None:
                try:
                    upload_df = pd.read_csv(marks_csv)
                    upload_df.columns = [str(c).strip().lower() for c in upload_df.columns]

                    required = {
                        "student_name", "class", "division", "academic_year",
                        "exam", "subject", "max_marks", "marks_obtained"
                    }
                    missing = sorted(required - set(upload_df.columns))

                    if missing:
                        st.error("Missing required column(s): " + ", ".join(missing))
                    elif upload_df.empty:
                        st.warning("The CSV file is empty.")
                    else:
                        if "remarks" not in upload_df.columns:
                            upload_df["remarks"] = ""

                        # Build a lookup only from students this logged-in account is allowed to access.
                        accessible_students = {}
                        for row in student_rows:
                            key = (
                                str(row["name"]).strip().casefold(),
                                str(row["class"]).strip().casefold(),
                                str(row["division"] or "").strip().casefold(),
                            )
                            accessible_students.setdefault(key, []).append(row)

                        preview_rows = []
                        valid_payloads = []

                        for idx, csv_row in upload_df.iterrows():
                            row_no = int(idx) + 2
                            name = str(csv_row.get("student_name", "")).strip()
                            class_name = str(csv_row.get("class", "")).strip()
                            division = str(csv_row.get("division", "")).strip()
                            year = str(csv_row.get("academic_year", "")).strip()
                            exam = str(csv_row.get("exam", "")).strip()
                            subject = str(csv_row.get("subject", "")).strip()
                            remarks_value = csv_row.get("remarks", "")
                            remarks_value = "" if pd.isna(remarks_value) else str(remarks_value).strip()

                            problems = []
                            matches = accessible_students.get((
                                name.casefold(), class_name.casefold(), division.casefold()
                            ), [])

                            if not name or not class_name or not year or not exam or not subject:
                                problems.append("Required text value is blank")
                            if not matches:
                                problems.append("Student not found / not allowed for this account")
                            elif len(matches) > 1:
                                problems.append("More than one matching student found")

                            try:
                                max_value = int(float(csv_row.get("max_marks")))
                                obtained_value = int(float(csv_row.get("marks_obtained")))
                                if max_value <= 0:
                                    problems.append("max_marks must be greater than 0")
                                if obtained_value < 0:
                                    problems.append("marks_obtained cannot be negative")
                                if obtained_value > max_value:
                                    problems.append("marks_obtained cannot exceed max_marks")
                            except (TypeError, ValueError):
                                max_value = 0
                                obtained_value = 0
                                problems.append("Marks must be numeric")

                            status = "✅ Valid" if not problems else "❌ " + "; ".join(problems)
                            preview_rows.append({
                                "Row": row_no, "Student": name, "Class": class_name,
                                "Division": division, "Year": year, "Exam": exam,
                                "Subject": subject, "Marks": f"{obtained_value}/{max_value}" if not problems or max_value else "-",
                                "Status": status,
                            })

                            if not problems:
                                valid_payloads.append({
                                    "row_no": row_no,
                                    "student_id": int(matches[0]["id"]),
                                    "student_name": matches[0]["name"],
                                    "academic_year": year,
                                    "exam_name": exam,
                                    "subject_name": subject,
                                    "max_marks": max_value,
                                    "marks_obtained": obtained_value,
                                    "remarks": remarks_value,
                                })

                        st.markdown("##### Preview & validation")
                        st.dataframe(preview_rows, hide_index=True, use_container_width=True)

                        invalid_count = len(preview_rows) - len(valid_payloads)
                        c1, c2, c3 = st.columns(3)
                        c1.metric("CSV Rows", len(preview_rows))
                        c2.metric("Valid", len(valid_payloads))
                        c3.metric("Invalid", invalid_count)

                        if invalid_count:
                            st.warning("Fix invalid rows and upload the CSV again. Only valid rows can be imported.")

                        allow_partial = st.checkbox(
                            "Import valid rows even if some rows are invalid",
                            value=False, key="marks_csv_allow_partial"
                        )
                        can_import = bool(valid_payloads) and (invalid_count == 0 or allow_partial)

                        if st.button(
                            "✅ Import Valid Marks",
                            type="primary", use_container_width=True,
                            disabled=not can_import, key="import_marks_csv_button",
                        ):
                            db = SessionLocal()
                            created = 0
                            updated = 0
                            try:
                                ensure_student_results_table(db)
                                for item in valid_payloads:
                                    existing = db.execute(select(student_results).where(
                                        student_results.c.school_code == st.session_state.school_code,
                                        student_results.c.student_id == int(item["student_id"]),
                                        func.lower(student_results.c.academic_year) == item["academic_year"].lower(),
                                        func.lower(student_results.c.exam_name) == item["exam_name"].lower(),
                                        func.lower(student_results.c.subject_name) == item["subject_name"].lower(),
                                    )).mappings().first()

                                    values = dict(
                                        school_code=st.session_state.school_code,
                                        student_id=int(item["student_id"]),
                                        academic_year=item["academic_year"],
                                        exam_name=item["exam_name"],
                                        subject_name=item["subject_name"],
                                        max_marks=int(item["max_marks"]),
                                        marks_obtained=int(item["marks_obtained"]),
                                        remarks=item["remarks"],
                                        updated_by=st.session_state.username,
                                        updated_at=datetime.utcnow(),
                                    )

                                    if existing:
                                        db.execute(student_results.update().where(
                                            student_results.c.id == int(existing["id"])
                                        ).values(**values))
                                        updated += 1
                                    else:
                                        db.execute(student_results.insert().values(**values))
                                        created += 1

                                db.commit()
                                write_audit_log(
                                    "MARKS_CSV_IMPORT",
                                    f"Marks CSV imported: {created} created, {updated} updated, {invalid_count} invalid row(s).",
                                    entity_type="student_result",
                                )
                                st.success(
                                    f"✅ Import complete — New: {created}, Updated: {updated}, "
                                    f"Skipped invalid: {invalid_count}."
                                )
                                st.rerun()
                            except Exception as exc:
                                db.rollback()
                                st.error(f"Marks CSV import failed: {exc}")
                            finally:
                                db.close()
                except Exception as exc:
                    st.error(f"Could not read CSV file: {exc}")


        with report_tab:
            st.markdown("#### Student report card")
            report_group = st.selectbox(
                "Class & division", groups,
                format_func=lambda g: f"Class {g[0]}{g[1]}",
                key="report_group",
            )
            report_students = [
                row for row in student_rows
                if (str(row["class"]), str(row["division"] or "")) == report_group
            ]
            report_student_map = {int(row["id"]): row for row in report_students}
            report_student_id = st.selectbox(
                "Student", list(report_student_map.keys()),
                format_func=lambda sid: report_student_map[sid]["name"],
                key="report_student",
            )
            all_rows = load_student_results(st.session_state.school_code, student_id=int(report_student_id))
            if not all_rows:
                st.info("No marks have been entered for this student yet.")
            else:
                report_keys = []
                for row in all_rows:
                    key = (row["academic_year"], row["exam_name"])
                    if key not in report_keys:
                        report_keys.append(key)
                selected_report = st.selectbox(
                    "Academic year & exam", report_keys,
                    format_func=lambda item: f"{item[0]} · {item[1]}",
                    key="report_exam_key",
                )
                rows = [
                    row for row in all_rows
                    if (row["academic_year"], row["exam_name"]) == selected_report
                ]
                total_obtained, total_max, percentage = result_summary(rows)
                metrics = st.columns(3)
                metrics[0].metric("Total Marks", total_obtained)
                metrics[1].metric("Out of", total_max)
                metrics[2].metric("Percentage", f"{percentage:.1f}%")
                st.dataframe([
                    {
                        "Subject": row["subject_name"],
                        "Marks": int(row["marks_obtained"]),
                        "Out of": int(row["max_marks"]),
                        "%": round((int(row["marks_obtained"]) / int(row["max_marks"]) * 100), 1) if int(row["max_marks"]) else 0,
                        "Remarks": row.get("remarks") or "",
                    }
                    for row in rows
                ], hide_index=True, use_container_width=True)

                db = SessionLocal()
                try:
                    student_obj = db.query(Student).filter(
                        Student.id == int(report_student_id),
                        Student.school_code == st.session_state.school_code,
                    ).first()
                    if not student_obj:
                        st.error("Student record could not be found.")
                    else:
                        pdf_bytes = build_student_report_card_pdf(
                            st.session_state.school_name, st.session_state.school_code,
                            student_obj, selected_report[0], selected_report[1], rows,
                        )
                        safe_exam = re.sub(r"[^A-Za-z0-9_-]+", "_", selected_report[1]).strip("_") or "exam"
                        st.download_button(
                            "📥 Download Report Card PDF",
                            data=pdf_bytes,
                            file_name=f"{student_obj.name.replace(' ', '_')}_{safe_exam}_report_card.pdf",
                            mime="application/pdf",
                            type="primary",
                            use_container_width=True,
                            key="staff_report_card_download",
                        )
                except Exception as exc:
                    st.error(f"Could not generate report card: {exc}")
                finally:
                    db.close()


if st.session_state.current_page == 'Analytics':
    # =========================================================
    # CLASS-WISE ATTENDANCE ANALYTICS
    # =========================================================

    st.divider()
    st.subheader("📊 Class-wise Attendance")

    if student_rows:

        class_data = {}

        for student in student_rows:
            class_name = student["class"]

            if class_name not in class_data:
                class_data[class_name] = {
                    "students": 0,
                    "present_days": 0,
                    "total_days": 0
                }

            class_data[class_name]["students"] += 1
            class_data[class_name]["present_days"] += student["present_days"]
            class_data[class_name]["total_days"] += student["total_days"]

        analytics_rows = []

        for class_name, data in sorted(class_data.items()):

            total_days = data["total_days"]
            present_days = data["present_days"]

            attendance = (
                (present_days / total_days) * 100
                if total_days > 0
                else 0
            )

            analytics_rows.append({
                "Class": class_name,
                "Students": data["students"],
                "Present Days": present_days,
                "Total Days": total_days,
                "Attendance %": round(attendance, 1)
            })

        st.dataframe(
            analytics_rows,
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info("No student data available.")

    # =========================================================
    # GENDER-WISE ATTENDANCE ANALYTICS
    # =========================================================

    st.subheader("⚥ Gender-wise Attendance")

    if student_rows:

        gender_data = {}

        for student in student_rows:
            gender = str(student.get("gender") or "Unknown")

            if gender not in gender_data:
                gender_data[gender] = {
                    "students": 0,
                    "present_days": 0,
                    "total_days": 0
                }

            gender_data[gender]["students"] += 1
            gender_data[gender]["present_days"] += student["present_days"]
            gender_data[gender]["total_days"] += student["total_days"]

        gender_rows = []

        for gender, data in sorted(gender_data.items()):

            attendance = (
                (data["present_days"] / data["total_days"]) * 100
                if data["total_days"] > 0
                else 0
            )

            gender_rows.append({
                "Gender": gender,
                "Students": data["students"],
                "Present Days": data["present_days"],
                "Total Days": data["total_days"],
                "Attendance %": round(attendance, 1)
            })

        st.dataframe(
            gender_rows,
            width="stretch",
            hide_index=True
        )

        gender_chart = {
            row["Gender"]: row["Attendance %"]
            for row in gender_rows
        }

        st.bar_chart(gender_chart)

    else:
        st.info("No student data available.")
    # =========================================================
    # MONTH SELECT + DAY-WISE ATTENDANCE TREND
    # =========================================================

    st.divider()
    st.subheader("📅 Month-wise / Day-wise Attendance Trend")

    db = SessionLocal()

    try:
        # Available months
            # Available months
        available_months = (
            db.query(
                func.strftime("%Y-%m", Attendance.date).label("month")
            )
            .join(
                Student,
                Attendance.student_id == Student.id
            )
            .filter(
                Student.school_code
                == st.session_state.school_code
            )
            .distinct()
            .order_by(
                func.strftime("%Y-%m", Attendance.date)
            )
            .all()
        )

        if available_months:

            month_values = [
                row.month
                for row in available_months
            ]

            # Month selection
            selected_month = st.selectbox(
                "Select Month",
                month_values
            )

            # Day-wise attendance for selected month
            daily_data = (
        db.query(
            Attendance.date,
            func.count(Attendance.id).label("total_days"),
            func.sum(
                case(
                    (
                        func.lower(Attendance.status) == "present",
                        1
                    ),
                    else_=0
                )
            ).label("present_days")
        )
        .join(
            Student,
            Attendance.student_id == Student.id
        )
        .filter(
            Student.school_code
            == st.session_state.school_code,
            func.strftime("%Y-%m", Attendance.date)
            == selected_month
        )
                .group_by(
                    Attendance.date
                )
                .order_by(
                    Attendance.date
                )
                .all()
            )

            if daily_data:

                day_rows = []

                for row in daily_data:

                    total = int(row.total_days or 0)
                    present = int(row.present_days or 0)

                    percentage = (
                        (present / total) * 100
                        if total > 0
                        else 0
                    )

                    day_rows.append({
                        "Date": row.date.strftime("%d-%m-%Y"),
                        "Present Days": present,
                        "Total Days": total,
                        "Attendance %": round(percentage, 1)
                    })

                # Table
                st.dataframe(
                    day_rows,
                    width="stretch",
                    hide_index=True
                )

                # Day-wise chart
                day_chart = {
                    row["Date"]: row["Attendance %"]
                    for row in day_rows
                }

                st.line_chart(day_chart)

            else:
                st.info(
                    f"No attendance records found for {selected_month}."
                )

        else:
            st.info("No attendance records available.")

    finally:
        db.close()
    # =========================================================
    # CLASS-WISE ATTENDANCE TREND
    # =========================================================

    st.divider()
    st.subheader("🏫 Class-wise Attendance Trend")

    db = SessionLocal()

    try:
        # Available classes
        classes = (
        db.query(Student.class_name)
        .filter(
            Student.school_code
            == st.session_state.school_code
        )
        .distinct()
        .order_by(Student.class_name)
        .all()
    )
        class_values = [row.class_name for row in classes if row.class_name]

        if class_values:

            selected_class = st.selectbox(
                "Select Class",
                class_values,
                key="class_trend_select"
            )

            # Available months for selected class
            months = (
                db.query(
                    func.strftime("%Y-%m", Attendance.date).label("month")
                )
                .join(
                    Student,
                    Attendance.student_id == Student.id
                )
                .filter(
                     Student.school_code
                    == st.session_state.school_code,
                    Student.class_name == selected_class
                )
                .distinct()
                .order_by(
                    func.strftime("%Y-%m", Attendance.date)
                )
                .all()
            )

            month_values = [row.month for row in months if row.month]

            if month_values:

                selected_month = st.selectbox(
                    "Select Month",
                    month_values,
                    key="class_month_trend_select"
                )

                # Day-wise attendance for selected class + month
                daily_data = (
                    db.query(
                        Attendance.date,
                        func.count(Attendance.id).label("total_days"),
                        func.sum(
                            case(
                                (
                                    func.lower(Attendance.status) == "present",
                                    1
                                ),
                                else_=0
                            )
                        ).label("present_days")
                    )
                    .join(
                        Student,
                        Attendance.student_id == Student.id
                    )
                    .filter(
                        Student.school_code
                        == st.session_state.school_code,
                        Student.class_name == selected_class,
                        func.strftime("%Y-%m", Attendance.date)
                        == selected_month
                        )
                    .group_by(
                        Attendance.date
                    )
                    .order_by(
                        Attendance.date
                    )
                    .all()
                )

                if daily_data:

                    trend_data = []

                    for row in daily_data:

                        total = int(row.total_days or 0)
                        present = int(row.present_days or 0)

                        percentage = (
                            (present / total) * 100
                            if total > 0
                            else 0
                        )

                        trend_data.append({
                            "Date": row.date.strftime("%d-%m-%Y"),
                            "Attendance %": round(percentage, 1)
                        })

                    # Table
                    st.dataframe(
                        trend_data,
                        width="stretch",
                        hide_index=True
                    )

                    # Line chart
                    chart_data = {
                        row["Date"]: row["Attendance %"]
                        for row in trend_data
                    }

                    st.line_chart(chart_data)

                else:
                    st.info(
                        "No attendance records found for this selection."
                    )

            else:
                st.info(
                    f"No attendance data available for Class {selected_class}."
                )

        else:
            st.info("No class data available.")

    finally:
        db.close()

if st.session_state.current_page == "Monthly Report":
    import calendar

    st.subheader("📄 Monthly Attendance PDF Report")
    st.caption(
        "Choose a month and class. The report uses attendance records saved for that month. "
        "Teachers can only generate reports for their assigned classes."
    )

    available_groups = sorted({
        (str(row["class"]), str(row["division"] or ""))
        for row in student_rows
    })

    if not available_groups:
        if str(st.session_state.role).strip().lower() == "teacher":
            st.warning("No assigned class is available for this teacher account.")
        else:
            st.info("No class/student data is available yet.")
    else:
        today_value = date.today()
        year_options = list(range(today_value.year - 2, today_value.year + 1))
        report_year = st.selectbox(
            "Year", year_options, index=len(year_options) - 1, key="monthly_report_year"
        )
        month_options = list(range(1, 13))
        report_month = st.selectbox(
            "Month", month_options, index=today_value.month - 1,
            format_func=lambda m: calendar.month_name[m], key="monthly_report_month"
        )

        scope_options = ["All available classes"] + available_groups
        report_scope = st.selectbox(
            "Class and division",
            scope_options,
            format_func=lambda value: (
                value if isinstance(value, str)
                else f"Class {value[0]}{value[1]}"
            ),
            key="monthly_report_scope",
        )

        selected_report_groups = (
            available_groups if report_scope == "All available classes" else [report_scope]
        )

        preview_rows = [
            row for row in student_rows
            if (str(row["class"]), str(row["division"] or "")) in set(selected_report_groups)
        ]
        st.info(
            f"Report scope: {calendar.month_name[report_month]} {report_year} · "
            f"{len(selected_report_groups)} class(es) · {len(preview_rows)} student(s)"
        )

        if st.button("Generate Monthly PDF", type="primary", use_container_width=True, key="generate_monthly_pdf"):
            try:
                pdf_bytes = build_monthly_attendance_pdf(
                    school_code=st.session_state.school_code,
                    school_name=st.session_state.school_name or os.getenv("SCHOOL_NAME", "School AI"),
                    year=report_year,
                    month=report_month,
                    groups=selected_report_groups,
                )
                st.session_state["monthly_pdf_bytes"] = pdf_bytes
                st.session_state["monthly_pdf_filename"] = (
                    f"attendance_{report_year}_{report_month:02d}.pdf"
                    if report_scope == "All available classes"
                    else f"attendance_class_{report_scope[0]}{report_scope[1]}_{report_year}_{report_month:02d}.pdf"
                )
                st.success("✅ Monthly attendance PDF is ready.")
            except Exception as exc:
                st.error(f"Could not generate PDF: {exc}")

        if st.session_state.get("monthly_pdf_bytes"):
            st.download_button(
                "📥 Download Monthly PDF",
                data=st.session_state["monthly_pdf_bytes"],
                file_name=st.session_state.get("monthly_pdf_filename", "monthly_attendance.pdf"),
                mime="application/pdf",
                type="primary",
                use_container_width=True,
                key="download_monthly_pdf",
            )


if st.session_state.current_page == 'Search':
    # =========================================================
    # STUDENT SEARCH
    # =========================================================

    st.subheader("🔎 Student Overview")
    display_rows = []
    if student_rows:
        student_names = sorted(
            x["name"] for x in student_rows
        )

        selected_student = st.selectbox(
            "Select Student",
            student_names
        )

        student = next(
            x for x in student_rows
            if x["name"] == selected_student
        )

        attendance = float(
            student["attendance_percentage"]
        )

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 👤 Student Details")

            st.info(
                f"""
    **Gender:** {student['gender']}            

    **Student:** {student['name']}

    **Class:** {student['class']}

    **Division:** {student['division']}

    **Total Days:** {student['total_days']}

    **Present Days:** {student['present_days']}
    """
            )

        with col2:
            st.markdown("### 📈 Attendance")

            st.metric(
                "Attendance Percentage",
                f"{attendance:.1f}%"
            )

            st.progress(
                min(max(attendance / 100, 0.0), 1.0)
            )

            if attendance >= 85:
                st.success("🟢 Excellent Attendance")
            elif attendance >= 75:
                st.warning("🟡 Good Attendance")
            else:
                st.error("🔴 Low Attendance - Needs Attention")


    st.divider()

if st.session_state.current_page == "Parents":
    st.subheader("👨‍👩‍👧 Parent Management")
    st.caption("Create a parent login and link it to exactly one student. Parents can only view that child's attendance.")

    db = SessionLocal()
    try:
        ensure_parent_accounts_table(db)
        school_students = db.query(Student).filter(
            Student.school_code == st.session_state.school_code
        ).order_by(Student.class_name, Student.division, Student.name).all()
        existing_parents = db.execute(
            select(parent_accounts).where(
                parent_accounts.c.school_code == st.session_state.school_code
            ).order_by(parent_accounts.c.name)
        ).mappings().all()
    finally:
        db.close()

    if not school_students:
        st.info("Add students first, then create a parent login.")
    else:
        student_map = {student.id: student for student in school_students}
        with st.container(border=True):
            st.markdown("#### ➕ Create Parent Login")
            with st.form("create_parent_account_form"):
                parent_name = st.text_input("Parent / guardian name", placeholder="Example: Rajesh Patil")
                parent_username = st.text_input("Parent username", placeholder="Example: rahul_parent")
                selected_student_id = st.selectbox(
                    "Link to student",
                    list(student_map.keys()),
                    format_func=lambda sid: (
                        f"{student_map[sid].name} · Class "
                        f"{student_map[sid].class_name}{student_map[sid].division or ''} · ID {sid}"
                    ),
                )
                linked_phone = (student_map[selected_student_id].parent_contact or "").strip()
                st.caption(f"Parent contact on student record: {linked_phone or 'Not added'}")
                parent_password = st.text_input("Temporary password", type="password")
                parent_confirm = st.text_input("Confirm password", type="password")
                create_parent = st.form_submit_button("Create Parent Account", type="primary")

            if create_parent:
                clean_name = parent_name.strip()
                clean_username = parent_username.strip()
                if not clean_name or not clean_username:
                    st.error("Parent name and username are required.")
                elif not re.fullmatch(r"[A-Za-z0-9_.-]{4,50}", clean_username):
                    st.error("Username must be 4–50 characters and use only letters, numbers, dot, underscore or hyphen.")
                elif len(parent_password) < 8:
                    st.error("Password must be at least 8 characters.")
                elif parent_password != parent_confirm:
                    st.error("Passwords do not match.")
                else:
                    db = SessionLocal()
                    try:
                        ensure_parent_accounts_table(db)
                        staff_exists = db.query(User).filter(
                            func.lower(User.username) == clean_username.lower()
                        ).first()
                        parent_exists = db.execute(
                            select(parent_accounts.c.id).where(
                                func.lower(parent_accounts.c.username) == clean_username.lower()
                            )
                        ).first()
                        linked_exists = db.execute(
                            select(parent_accounts.c.id).where(
                                parent_accounts.c.school_code == st.session_state.school_code,
                                parent_accounts.c.student_id == int(selected_student_id),
                            )
                        ).first()
                        if staff_exists or parent_exists:
                            st.error("This username is already in use. Choose another username.")
                        elif linked_exists:
                            st.error("This student already has a parent login. Delete or update the existing account first.")
                        else:
                            password_hash = bcrypt.hashpw(
                                parent_password.encode("utf-8"), bcrypt.gensalt()
                            ).decode("utf-8")
                            db.execute(parent_accounts.insert().values(
                                user_id=f"parent-{secrets.token_hex(6)}",
                                name=clean_name,
                                username=clean_username,
                                password_hash=password_hash,
                                school_code=st.session_state.school_code,
                                student_id=int(selected_student_id),
                                phone=linked_phone,
                                created_at=datetime.utcnow(),
                            ))
                            db.commit()
                            write_audit_log(
                                "PARENT_ACCOUNT_CREATE",
                                f"Created parent login {clean_username} for {student_map[selected_student_id].name}.",
                                entity_type="parent", entity_id=clean_username,
                            )
                            st.success(
                                f"✅ Parent login created for {student_map[selected_student_id].name}. "
                                f"Username: {clean_username}"
                            )
                            st.rerun()
                    except Exception as exc:
                        db.rollback()
                        st.error(f"Could not create parent account: {exc}")
                    finally:
                        db.close()

    st.divider()
    st.markdown("#### Existing Parent Accounts")
    if not existing_parents:
        st.info("No parent accounts created yet.")
    else:
        rows = []
        for account in existing_parents:
            student = next((s for s in school_students if s.id == account["student_id"]), None)
            rows.append({
                "Parent": account["name"],
                "Username": account["username"],
                "Student": student.name if student else f"Student ID {account['student_id']}",
                "Class": f"{student.class_name}{student.division or ''}" if student else "-",
                "Phone": account.get("phone") or "",
            })
        st.dataframe(rows, hide_index=True, use_container_width=True)

        delete_options = {
            account["id"]: f"{account['name']} (@{account['username']})"
            for account in existing_parents
        }
        with st.expander("🗑️ Delete parent login"):
            delete_parent_id = st.selectbox(
                "Select parent account",
                list(delete_options.keys()),
                format_func=lambda pid: delete_options[pid],
                key="delete_parent_account_select",
            )
            if st.button("Delete selected parent login", key="delete_parent_account_button"):
                db = SessionLocal()
                try:
                    ensure_parent_accounts_table(db)
                    db.execute(parent_accounts.delete().where(
                        parent_accounts.c.id == int(delete_parent_id),
                        parent_accounts.c.school_code == st.session_state.school_code,
                    ))
                    deleted_parent_label = delete_options.get(delete_parent_id, str(delete_parent_id))
                    db.commit()
                    write_audit_log(
                        "PARENT_ACCOUNT_DELETE", f"Deleted parent login {deleted_parent_label}.",
                        entity_type="parent", entity_id=delete_parent_id,
                    )
                    st.success("Parent login deleted.")
                    st.rerun()
                except Exception as exc:
                    db.rollback()
                    st.error(f"Could not delete parent login: {exc}")
                finally:
                    db.close()


if st.session_state.current_page == "Teachers":
    st.subheader("👩‍🏫 Teacher Management")
    st.caption("Create teacher login IDs first, then assign each teacher to a class and division.")

    teacher_accounts = load_teacher_accounts()

    left, right = st.columns(2, gap="large")
    with left:
        st.markdown("### ➕ Create Teacher Account")
        with st.form("create_teacher_account"):
            teacher_full_name = st.text_input("Teacher full name", placeholder="Rahul Sir")
            teacher_username = st.text_input("Login username", placeholder="rahul01")
            teacher_phone = st.text_input("Mobile number (optional)", placeholder="+919876543210")
            teacher_password = st.text_input("Temporary password", type="password")
            teacher_confirm = st.text_input("Confirm password", type="password")
            create_teacher = st.form_submit_button("Create Teacher Login", type="primary", use_container_width=True)

        if create_teacher:
            name = teacher_full_name.strip()
            username = teacher_username.strip()
            phone = teacher_phone.strip()
            if not name:
                st.error("Enter the teacher's full name.")
            elif not re.fullmatch(r"[A-Za-z0-9_.-]{4,50}", username):
                st.error("Username must be 4–50 characters and use letters, numbers, dot, underscore or hyphen.")
            elif phone and not re.fullmatch(r"\+[1-9]\d{7,14}", phone):
                st.error("Use mobile format like +919876543210, or leave it blank.")
            elif len(teacher_password) < 8:
                st.error("Password must be at least 8 characters.")
            elif teacher_password != teacher_confirm:
                st.error("Passwords do not match.")
            else:
                db = SessionLocal()
                try:
                    existing = db.query(User).filter(
                        func.lower(User.username) == username.lower()
                    ).first()
                    if existing:
                        st.error("This username already exists. Choose another username.")
                    else:
                        password_hash = bcrypt.hashpw(
                            teacher_password.encode("utf-8"), bcrypt.gensalt()
                        ).decode("utf-8")
                        values = dict(
                            user_id=f"teacher-{secrets.token_hex(6)}",
                            name=name,
                            username=username,
                            password_hash=password_hash,
                            role="teacher",
                            school_code=st.session_state.school_code,
                        )
                        # Current User model supports phone fields; keep this defensive for older databases.
                        if hasattr(User, "phone"):
                            values["phone"] = phone
                        if hasattr(User, "phone_verified"):
                            values["phone_verified"] = 0
                        db.add(User(**values))
                        db.commit()
                        write_audit_log(
                            "TEACHER_ACCOUNT_CREATE", f"Created teacher login {username} for {name}.",
                            entity_type="teacher", entity_id=username,
                        )
                        st.success(f"✅ Teacher login created: {username}")
                        st.info("Share the username and temporary password with the teacher securely. The password is not shown again.")
                        st.rerun()
                except Exception as exc:
                    db.rollback()
                    st.error(f"Could not create teacher account: {exc}")
                finally:
                    db.close()

    with right:
        st.markdown("### 🔗 Assign Teacher to Class")
        teacher_accounts = load_teacher_accounts()
        all_groups = sorted({(str(row["class"]), str(row["division"] or "")) for row in student_rows})
        if not teacher_accounts:
            st.info("Create a teacher account first.")
        elif not all_groups:
            st.info("Add students/classes first.")
        else:
            teacher_usernames = list(teacher_accounts.keys())
            with st.form("assign_teacher_account"):
                selected_teacher_username = st.selectbox(
                    "Teacher",
                    teacher_usernames,
                    format_func=lambda u: f"{teacher_accounts[u]['name']} (@{u})",
                )
                selected_teacher_group = st.selectbox(
                    "Class and division",
                    all_groups,
                    format_func=lambda g: f"Class {g[0]}{g[1]}",
                )
                assign_teacher = st.form_submit_button("Assign Teacher", type="primary", use_container_width=True)

            if assign_teacher:
                class_name, division_name = selected_teacher_group
                db = SessionLocal()
                try:
                    assignment_metadata.create_all(db.get_bind(), tables=[teacher_assignments], checkfirst=True)
                    existing = db.execute(select(teacher_assignments).where(
                        teacher_assignments.c.school_code == st.session_state.school_code,
                        teacher_assignments.c.class_name == class_name,
                        teacher_assignments.c.division == division_name,
                    )).first()
                    if existing:
                        db.execute(teacher_assignments.update().where(
                            teacher_assignments.c.school_code == st.session_state.school_code,
                            teacher_assignments.c.class_name == class_name,
                            teacher_assignments.c.division == division_name,
                        ).values(teacher_name=selected_teacher_username))
                    else:
                        db.execute(teacher_assignments.insert().values(
                            school_code=st.session_state.school_code,
                            class_name=class_name,
                            division=division_name,
                            teacher_name=selected_teacher_username,
                        ))
                    db.commit()
                    write_audit_log(
                        "TEACHER_ASSIGNMENT",
                        f"Assigned {selected_teacher_username} to Class {class_name}{division_name}.",
                        entity_type="class_assignment", entity_id=f"{class_name}{division_name}",
                    )
                    st.success(
                        f"✅ {teacher_accounts[selected_teacher_username]['name']} assigned to "
                        f"Class {class_name}{division_name}."
                    )
                    st.rerun()
                except Exception as exc:
                    db.rollback()
                    st.error(f"Could not assign teacher: {exc}")
                finally:
                    db.close()

    st.divider()
    st.markdown("### 📋 Teacher Accounts & Assignments")
    teacher_accounts = load_teacher_accounts()
    assignments = load_teacher_assignments()
    assignment_rows = []
    for (class_name, division), assigned_value in sorted(assignments.items()):
        account = teacher_accounts.get(str(assigned_value))
        assignment_rows.append({
            "Teacher": account["name"] if account else str(assigned_value),
            "Username": account["username"] if account else str(assigned_value),
            "Class": f"{class_name}{division}",
        })
    if assignment_rows:
        st.dataframe(assignment_rows, hide_index=True, use_container_width=True)
        with st.form("remove_teacher_assignment"):
            assignment_keys = list(sorted(assignments.keys()))
            remove_group = st.selectbox(
                "Remove class assignment",
                assignment_keys,
                format_func=lambda g: f"Class {g[0]}{g[1]} — {teacher_display_name(assignments[g])}",
            )
            remove_assignment = st.form_submit_button("Unassign Teacher")
        if remove_assignment:
            db = SessionLocal()
            try:
                db.execute(teacher_assignments.delete().where(
                    teacher_assignments.c.school_code == st.session_state.school_code,
                    teacher_assignments.c.class_name == remove_group[0],
                    teacher_assignments.c.division == remove_group[1],
                ))
                db.commit()
                write_audit_log(
                    "TEACHER_UNASSIGN",
                    f"Removed teacher assignment from Class {remove_group[0]}{remove_group[1]}.",
                    entity_type="class_assignment", entity_id=f"{remove_group[0]}{remove_group[1]}",
                )
                st.success(f"Teacher unassigned from Class {remove_group[0]}{remove_group[1]}.")
                st.rerun()
            except Exception as exc:
                db.rollback()
                st.error(f"Could not remove assignment: {exc}")
            finally:
                db.close()
    else:
        st.info("No teacher assignments yet.")

    if teacher_accounts:
        st.markdown("### 👤 Existing Teacher Logins")
        st.dataframe([
            {"Name": item["name"], "Username": username, "School": st.session_state.school_code}
            for username, item in teacher_accounts.items()
        ], hide_index=True, use_container_width=True)


if st.session_state.current_page == 'Attendance':
    is_principal = str(st.session_state.role).strip().lower() == "principal"
    if is_principal:
        st.subheader("🗑️ Delete Student")
        if not student_rows:
            st.info("No students available to delete.")
        else:
            student_by_id = {row["id"]: row for row in student_rows}
            delete_id = st.selectbox(
                "Select student to delete",
                sorted(student_by_id, key=lambda sid: (student_by_id[sid]["name"], sid)),
                format_func=lambda sid: (
                    f"{student_by_id[sid]['name']} · Class "
                    f"{student_by_id[sid]['class']}{student_by_id[sid]['division'] or ''} · ID {sid}"
                ),
                key="principal_delete_student",
            )
            if st.button("🗑️ Delete selected student", key="request_student_delete"):
                st.session_state.confirm_delete_student_id = delete_id
            if st.session_state.get("confirm_delete_student_id") == delete_id:
                st.warning(f"Permanently delete {student_by_id[delete_id]['name']} and their attendance records?")
                confirm, cancel = st.columns(2)
                if confirm.button("Yes, permanently delete", key="confirm_student_delete"):
                    db = SessionLocal()
                    try:
                        student = db.query(Student).filter(
                            Student.id == delete_id,
                            Student.school_code == st.session_state.school_code,
                        ).first()
                        if student is None:
                            st.error("Student no longer exists in this school.")
                        else:
                            db.query(Attendance).filter(Attendance.student_id == student.id).delete(
                                synchronize_session=False
                            )
                            deleted_student_name = student.name
                            db.delete(student)
                            db.commit()
                            write_audit_log(
                                "STUDENT_DELETE", f"Deleted student {deleted_student_name} and attendance records.",
                                entity_type="student", entity_id=delete_id,
                            )
                            st.session_state.pop("confirm_delete_student_id", None)
                            st.session_state.student_action_message = "Student deleted successfully."
                            st.rerun()
                    except Exception as exc:
                        db.rollback()
                        st.error(f"Delete failed: {exc}")
                    finally:
                        db.close()
                if cancel.button("Cancel", key="cancel_student_delete"):
                    st.session_state.pop("confirm_delete_student_id", None)
                    st.rerun()

            with st.expander("🗑️ Delete all students in this school"):
                st.warning(
                    f"This permanently removes all {len(student_rows)} students in "
                    "this school, their attendance records, and class teacher assignments. "
                    "This cannot be undone."
                )
                with st.form("delete_all_students_form"):
                    confirmation = st.text_input(
                        "Type DELETE ALL to confirm", key="delete_all_confirmation"
                    )
                    delete_everyone = st.form_submit_button(
                        "Permanently delete all students", type="primary"
                    )
                if delete_everyone:
                    if confirmation.strip() != "DELETE ALL":
                        st.error("Type DELETE ALL exactly to confirm.")
                    else:
                        db = SessionLocal()
                        try:
                            school_code = st.session_state.school_code
                            ids = [student_id for (student_id,) in db.query(Student.id).filter(
                                Student.school_code == school_code
                            ).all()]
                            if ids:
                                db.query(Attendance).filter(Attendance.student_id.in_(ids)).delete(
                                    synchronize_session=False
                                )
                                db.query(Student).filter(
                                    Student.school_code == school_code
                                ).delete(synchronize_session=False)
                            db.execute(teacher_assignments.delete().where(
                                teacher_assignments.c.school_code == school_code
                            ))
                            db.commit()
                            write_audit_log(
                                "STUDENTS_DELETE_ALL", f"Deleted {len(ids)} students, attendance records and class teacher assignments.",
                                entity_type="school", entity_id=school_code,
                            )
                            st.session_state.pop("confirm_delete_student_id", None)
                            st.session_state.student_action_message = (
                                f"Deleted {len(ids)} students and their school records."
                            )
                            st.rerun()
                        except Exception as exc:
                            db.rollback()
                            st.error(f"Could not delete students: {exc}")
                        finally:
                            db.close()
        st.divider()
    action_message = st.session_state.pop("student_action_message", None)
    if action_message:
        st.success(action_message)
    st.subheader("📝 Daily class attendance")
    st.caption("Choose a class and division, assign its teacher, then mark students present or absent.")
    try:
        class_teachers = load_teacher_assignments()
        class_groups = sorted({(str(row["class"]), str(row["division"] or "")) for row in student_rows})
        if not class_groups:
            st.info("Add students first using the CSV importer in the sidebar.")
        else:
            selected_group = st.selectbox(
                "Class and division",
                class_groups,
                format_func=lambda group: f"Class {group[0]}{group[1]}",
                key="mark_class_group",
            )
            class_name, division_name = selected_group
            teacher_name = class_teachers.get(selected_group, "")
            if is_principal:
                teacher_accounts = load_teacher_accounts()
                st.markdown("#### 👩‍🏫 Assigned class teacher")
                if teacher_name:
                    st.info(f"Current teacher: {teacher_display_name(teacher_name)}")
                else:
                    st.info("No teacher assigned yet.")
                if teacher_accounts:
                    st.caption("Use Teacher Management to create logins and change class assignments.")
                    if st.button("Open Teacher Management →", key=f"open_teacher_management_{class_name}_{division_name}"):
                        st.session_state.current_page = "Teachers"
                        st.rerun()
                else:
                    st.warning("No teacher login exists yet. Create one in Teacher Management.")
            else:
                st.info(f"👩‍🏫 Class teacher: {teacher_display_name(teacher_name)}")

            if is_principal:
                with st.expander("📱 Parent phone numbers for absence alerts"):
                    st.caption("Enter numbers in international format, for example +919876543210. "
                               "Optional CSV column: parent_contact. Check that each number belongs to the right parent.")
                    contact_rows = [{"ID": row["id"], "Student": row["name"],
                                     "Parent contact": ""} for row in student_rows
                                    if (str(row["class"]), str(row["division"] or "")) == selected_group]
                    db = SessionLocal()
                    try:
                        contacts = {s.id: s.parent_contact or "" for s in db.query(Student).filter(
                            Student.school_code == st.session_state.school_code,
                            Student.class_name == class_name, Student.division == division_name,
                        ).all()}
                    finally:
                        db.close()
                    for contact in contact_rows:
                        contact["Parent contact"] = contacts.get(contact["ID"], "")
                    with st.form(f"parent_contacts_{class_name}_{division_name}"):
                        contact_edits = st.data_editor(pd.DataFrame(contact_rows), hide_index=True,
                            disabled=["ID", "Student"], use_container_width=True,
                            key=f"parent_contact_editor_{class_name}_{division_name}")
                        save_contacts = st.form_submit_button("💾 Save parent numbers")
                    if save_contacts:
                        import re
                        entries = [(int(row["ID"]), str(row["Parent contact"]).strip())
                                   for _, row in contact_edits.iterrows()]
                        if any(number and not re.fullmatch(r"\+[1-9]\d{7,14}", number)
                               for _, number in entries):
                            st.error("Use international phone format such as +919876543210.")
                        else:
                            db = SessionLocal()
                            try:
                                for student_id, number in entries:
                                    student = db.query(Student).filter(
                                        Student.id == student_id,
                                        Student.school_code == st.session_state.school_code,
                                    ).first()
                                    if student:
                                        student.parent_contact = number
                                db.commit()
                                st.success("Parent numbers saved.")
                            except Exception as exc:
                                db.rollback()
                                st.error(f"Could not save parent numbers: {exc}")
                            finally:
                                db.close()

            attendance_date = st.date_input("Attendance date", value=date.today(),
                                            max_value=date.today(), key="mark_date")
            holiday_entry = get_holiday_for_date(st.session_state.school_code, attendance_date)
            if holiday_entry:
                st.error(
                    f"🏖️ {attendance_date:%d %b %Y} is marked as a school holiday: "
                    f"{holiday_entry['title']}. Attendance cannot be saved for this date."
                )
            else:
                day_entries = load_school_calendar(
                    st.session_state.school_code, attendance_date, attendance_date
                )
                non_holiday_entries = [
                    row for row in day_entries if str(row["event_type"]).lower() != "holiday"
                ]
                if non_holiday_entries:
                    st.info(
                        "📅 " + " · ".join(
                            f"{row['event_type']}: {row['title']}" for row in non_holiday_entries
                        )
                    )
            group_students = sorted(
                [row for row in student_rows if (str(row["class"]), str(row["division"] or "")) == selected_group],
                key=lambda row: (row["name"], row["id"]),
            )
            db = SessionLocal()
            try:
                student_ids = [row["id"] for row in group_students]
                existing_records = db.query(Attendance).filter(
                    Attendance.student_id.in_(student_ids), Attendance.date == attendance_date
                ).all()
                existing_by_student = {record.student_id: record for record in existing_records}
            finally:
                db.close()
            attendance_table = pd.DataFrame([
                {"ID": row["id"], "Student": row["name"],
                 "Present": existing_by_student[row["id"]].status.lower() == "present"
                 if row["id"] in existing_by_student else True}
                for row in group_students
            ])
            with st.form(f"daily_attendance_{class_name}_{division_name}_{attendance_date}"):
                edited_table = st.data_editor(
                    attendance_table, hide_index=True, use_container_width=True,
                    disabled=["ID", "Student"],
                    column_config={"Present": st.column_config.CheckboxColumn("Present", help="Uncheck for absent")},
                    key=f"daily_attendance_editor_{class_name}_{division_name}_{attendance_date}",
                )
                save_attendance = st.form_submit_button(
                    "💾 Save class attendance", type="primary", disabled=bool(holiday_entry)
                )
            if save_attendance:
                if get_holiday_for_date(st.session_state.school_code, attendance_date):
                    st.error("Attendance is blocked because this date is marked as a school holiday.")
                    st.stop()
                db = SessionLocal()
                try:
                    # Read fresh records inside the transaction to handle corrections.
                    current_students = {row.id: row for row in db.query(Student).filter(
                        Student.id.in_(student_ids),
                        Student.school_code == st.session_state.school_code,
                        Student.class_name == class_name,
                        Student.division == division_name,
                    ).all()}
                    current_records = {record.student_id: record for record in db.query(Attendance).filter(
                        Attendance.student_id.in_(list(current_students)),
                        Attendance.date == attendance_date,
                    ).all()}
                    created_count = 0
                    changed_count = 0
                    for _, row in edited_table.iterrows():
                        student_id = int(row["ID"])
                        student = current_students.get(student_id)
                        if student is None:
                            continue
                        status = "present" if bool(row["Present"]) else "absent"
                        old_record = current_records.get(student_id)
                        if old_record:
                            old_present = str(old_record.status).lower() == "present"
                            if old_present != (status == "present"):
                                student.present_days = max(0, int(student.present_days or 0) + (1 if status == "present" else -1))
                                changed_count += 1
                            old_record.status = status
                        else:
                            db.add(Attendance(student_id=student_id, date=attendance_date, status=status))
                            created_count += 1
                            student.total_days = int(student.total_days or 0) + 1
                            if status == "present":
                                student.present_days = int(student.present_days or 0) + 1
                    db.commit()
                    write_audit_log(
                        "ATTENDANCE_SAVE",
                        f"Class {class_name}{division_name} · {attendance_date} · new records: {created_count}, changed records: {changed_count}, students: {len(current_students)}.",
                        entity_type="attendance", entity_id=f"{class_name}{division_name}:{attendance_date}",
                    )
                    st.success(f"Attendance saved for Class {class_name}{division_name} on {attendance_date}.")
                    st.rerun()
                except Exception as exc:
                    db.rollback()
                    st.error(f"Could not save attendance: {exc}")
                finally:
                    db.close()
    except Exception as exc:
        st.error(f"Could not load class attendance: {exc}")
    st.divider()
    # =========================================================
    # ALL STUDENTS
    # =========================================================

    st.subheader("📋 All Students")

    search_name = st.text_input(
        "🔎 Search Student",
        placeholder="Enter student name"
    )

    class_options = sorted(
        {str(x["class"]) for x in student_rows}
    )

    selected_class = st.selectbox(
        "🏫 Select Class",
        ["All"] + class_options
    )

    division_options = sorted(
        {str(x["division"]) for x in student_rows}
    )

    selected_division = st.selectbox(
        "🏷️ Select Division",
        ["All"] + division_options
    )

    gender_options = sorted(
        {str(x.get("gender") or "") for x in student_rows}
    )

    selected_gender = st.selectbox(
        "⚥ Select Gender",
        ["All"] + gender_options
    )


    # =========================================================
    # FILTER STUDENTS
    # =========================================================

    # IMPORTANT:
    # Define this BEFORE using display_rows anywhere below.
    display_rows = []

    filtered_students = []

    if student_rows:

        filtered_students = [
            x
            for x in student_rows
            if (
                search_name.strip().lower()
                in x["name"].lower()
            )
            and (
                selected_class == "All"
                or str(x["class"]) == selected_class
            )
            and (
                selected_division == "All"
                or str(x["division"]) == selected_division
            )
            and (
                selected_gender == "All"
                or str(x.get("gender") or "") == selected_gender
            )
        ]

        for x in filtered_students:

            display_rows.append({
                "Student": x["name"],
                "Gender": x.get("gender") or "",
                "Class": x["class"],
                "Division": x["division"],
                "Total Days": x["total_days"],
                "Present Days": x["present_days"],
                "Attendance %": round(
                    x["attendance_percentage"],
                    1
                ),
            })


    # =========================================================
    # DISPLAY FILTERED STUDENTS
    # =========================================================

    if display_rows:

        st.dataframe(
            display_rows,
            width="stretch",
            hide_index=True
        )

    else:

        st.info("ℹ️ No students found for the selected filters.")


    # =========================================================
    # CLASS-WISE ATTENDANCE CHART
    # =========================================================

    st.divider()

    if display_rows:

        chart_data = {}

        for row in display_rows:

            class_name = row["Class"]

            if class_name not in chart_data:
                chart_data[class_name] = []

            chart_data[class_name].append(
                row["Attendance %"]
            )

        # Calculate average attendance for each class
        class_average = {}

        for class_name, values in chart_data.items():

            if values:
                class_average[class_name] = (
                    sum(values) / len(values)
                )

        st.subheader("📊 Class-wise Attendance")

        st.bar_chart(class_average)


    # =========================================================
    # ATTENDANCE SUMMARY
    # =========================================================

    st.divider()

    if display_rows:

        total_students = len(display_rows)

        total_days = sum(
            row["Total Days"]
            for row in display_rows
        )

        present_days = sum(
            row["Present Days"]
            for row in display_rows
        )

        overall_attendance = (
            (present_days / total_days) * 100
            if total_days > 0
            else 0
        )

        st.subheader("📌 Attendance Summary")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "👨‍🎓 Total Students",
            total_students
        )

        col2.metric(
            "📅 Total Days",
            total_days
        )

        col3.metric(
            "✅ Present Days",
            present_days
        )

        col4.metric(
            "📊 Overall Attendance",
            f"{overall_attendance:.1f}%"
        )


    # =========================================================
    # LOW ATTENDANCE ALERT
    # =========================================================

    low_attendance = [
        row
        for row in display_rows
        if row["Attendance %"] < 80
    ]

    if low_attendance:

        st.warning(
            f"⚠️ {len(low_attendance)} student(s) "
            "have attendance below 80%."
        )

    else:

        if display_rows:
            st.success(
                "✅ All students have attendance "
                "of 80% or above."
            )


    # =========================================================
    # LOW ATTENDANCE STUDENTS
    # =========================================================

    if low_attendance:

        st.subheader("⚠️ Low Attendance Students")

        low_rows = []

        for row in low_attendance:

            low_rows.append({
                "Student": row["Student"],
                "Class": row["Class"],
                "Division": row["Division"],
                "Attendance %": row["Attendance %"]
            })

        st.dataframe(
            low_rows,
            width="stretch",
            hide_index=True
        )


    # =========================================================
    # DOWNLOAD LOW ATTENDANCE REPORT
    # =========================================================

    if low_attendance:

        import pandas as pd

        download_df = pd.DataFrame(low_rows)

        st.download_button(
            label="📥 Download Low Attendance Report",
            data=download_df.to_csv(index=False),
            file_name="low_attendance_report.csv",
            mime="text/csv"
        )


if st.session_state.current_page == "Parent Messages":
    import re
    st.subheader("💬 Write a parent message")
    st.caption("Choose a student and review the message. WhatsApp opens a draft for you to send.")
    if student_rows:
        contact_student_by_id = {row["id"]: row for row in student_rows}
        contact_student_id = st.selectbox(
            "Student", sorted(contact_student_by_id),
            format_func=lambda sid: (f"{contact_student_by_id[sid]['name']} · Class "
                                     f"{contact_student_by_id[sid]['class']}"
                                     f"{contact_student_by_id[sid]['division'] or ''}"),
            key="message_student_id",
        )
        contact_db = SessionLocal()
        try:
            contact_student = contact_db.query(Student).filter(
                Student.id == contact_student_id,
                Student.school_code == st.session_state.school_code,
            ).first()
            parent_phone = (contact_student.parent_contact or "").strip() if contact_student else ""
        finally:
            contact_db.close()
        if not re.fullmatch(r"\+[1-9]\d{7,14}", parent_phone):
            st.warning("This student has no valid parent number. Add it in Student Attendance → Parent phone numbers.")
        else:
            st.caption(f"Parent contact: {parent_phone}")
            draft_text = st.text_area("Message", key=f"parent_message_{contact_student_id}",
                value=f"Dear parent, this is a message from Mahatma Gandhi English School about {contact_student.name}.")
            if draft_text.strip():
                from urllib.parse import quote
                st.link_button("💬 Open WhatsApp draft",
                               f"https://wa.me/{parent_phone[1:]}?text={quote(draft_text.strip())}")
            else:
                st.info("Write a message to enable the WhatsApp draft.")
    else:
        st.info("Import students to prepare parent messages.")
        st.divider()
    st.subheader("📨 Parents to contact: 3-day absence")
    st.caption(
        "Based on the latest three dates with recorded attendance for each class. "
        "Review the attendance and phone number before sending. "
        "WhatsApp opens a draft; you press Send."
    )

    try:
        from urllib.parse import quote
        import re

        absence_candidates = safe_parent_alert_agent(
            st.session_state.school_code
        )

        if not absence_candidates:
            st.success("✅ No pending 3-day absence alerts.")

        else:
            st.info(
                f"🤖 Agent found {len(absence_candidates)} parent alert(s). "
                "Review each message before opening WhatsApp."
            )

            for candidate in absence_candidates:

                label = (
                    f"🤖 {candidate['student_name']} · Class "
                    f"{candidate['class']}"
                    f"{candidate['division'] or ''}"
                )

                with st.expander(label):

                    st.write(
                        "📅 Absent dates: "
                        + ", ".join(
                            d.strftime("%d %b %Y")
                            for d in candidate["dates"]
                        )
                    )

                    phone = candidate["phone"]

                    if not re.fullmatch(
                        r"\+[1-9]\d{7,14}",
                        phone
                    ):
                        st.warning(
                            "⚠️ Parent mobile number missing or invalid."
                        )
                        continue

                    st.caption(f"📱 Parent: {phone}")

                    edited_message = st.text_area(
                        "✏️ Review / edit message",
                        value=candidate["message"],
                        key=f"agent_message_{candidate['student_id']}"
                    )

                    st.warning(
                        "🔐 Safe approval mode: "
                        "The agent cannot send this automatically."
                    )

                    if edited_message.strip():

                        whatsapp_url = (
                            f"https://wa.me/{phone[1:]}"
                            f"?text={quote(edited_message.strip())}"
                        )

                        st.link_button(
                            "✅ Approve & Open WhatsApp",
                            whatsapp_url,
                            use_container_width=True
                        )

    except Exception as exc:
        st.error(
            f"Could not prepare parent contact list: {exc}"
        )


if st.session_state.current_page == "Security" and str(st.session_state.role).strip().lower() == "principal":
    st.info("Login protection is enabled for this school account.")
    st.write(f"Maximum failed login attempts: {MAX_LOGIN_ATTEMPTS}")
    st.write(f"Lockout duration: {LOCKOUT_SECONDS // 60} minutes")
    st.write(f"Failed attempts in this session: {st.session_state.failed_attempts}")

# =========================================================
# AI TOOL
# =========================================================

@tool
def get_attendance(student_name: str) -> str:
    """Check a student's attendance from the school database."""

    db = SessionLocal()

    try:
        student = (
         db.query(Student)
        .filter(
        func.lower(Student.name)
        == student_name.strip().lower(),
        Student.school_code
        == st.session_state.school_code
    )
        .first()
)

        if not student:
            return (
                f"No attendance record found for "
                f"{student_name}."
            )

        total_days = (
            db.query(func.count(Attendance.id))
            .filter(Attendance.student_id == student.id)
            .scalar()
            or 0
        )

        present_days = (
            db.query(func.count(Attendance.id))
            .filter(
                Attendance.student_id == student.id,
                func.lower(Attendance.status) == "present"
            )
            .scalar()
            or 0
        )

        percentage = (
            (present_days / total_days) * 100
            if total_days
            else 0
        )

        return (
            f"Student: {student.name}\n"
            f"Class: {student.class_name}\n"
            f"Division: {student.division}\n"
            f"Total Days: {int(total_days)}\n"
            f"Present Days: {int(present_days)}\n"
            f"Attendance: {percentage:.2f}%"
        )

    finally:
        db.close()


# =========================================================
# AI AGENT
# =========================================================

agent = Agent(
    name="School AI Assistant",

    instructions="""
You are a helpful School AI Assistant.

You answer questions about student attendance.

When the user asks about a student's attendance,
always use the get_attendance tool.

Never invent attendance information.

If the student does not exist,
clearly say that no attendance record was found.

Keep answers short and easy to understand.
""",

    tools=[get_attendance]
)




def make_offline_lesson_plan(class_name, subject, topic, teaching_date, periods, minutes, extra):
    """Provide an editable lesson plan when paid AI generation is unavailable."""
    parts = [
        f"# Lesson Plan: {topic}",
        "**School:** Mahatma Gandhi English School  ",
        f"**Class:** {class_name}  **Subject:** {subject}  ",
        f"**Teaching date:** {teaching_date:%d %B %Y}  ",
        f"**Duration:** {periods} period(s), {minutes} minutes each",
        "\n## Learning objectives",
        f"- Explain the basic idea of {topic} in simple words.",
        f"- Identify at least two examples or uses of {topic}.",
        f"- Complete a short activity related to {topic}.",
        "\n## Required materials",
        f"Textbook or notes about {topic}, board, marker, and paper or exercise books.",
        "\n## Introduction",
        f"Ask students what they already know about {topic}. Show a familiar example "
        "and invite two students to share their ideas.",
        "\n## Teaching activities",
    ]
    for index in range(1, periods + 1):
        opening = max(3, round(minutes * .15))
        explanation = max(5, round(minutes * .35))
        practice = max(5, round(minutes * .35))
        closing = minutes - opening - explanation - practice
        if closing < 1:
            practice += closing - 1
            closing = 1
        parts.extend([
            f"### Period {index} ({minutes} minutes)",
            f"1. **Warm-up ({opening} min):** Review previous learning and ask one question about {topic}.",
            f"2. **Teacher explanation ({explanation} min):** Explain one key point of {topic} "
            "using a simple example. Write important words on the board.",
            f"3. **Student activity ({practice} min):** Students work individually or in pairs "
            "to write an example, draw a diagram, or demonstrate the idea. Discuss answers.",
            f"4. **Review ({closing} min):** Ask students to explain one thing they learned.",
        ])
    parts.extend([
        "\n## Assessment questions",
        f"1. What does {topic} mean?",
        f"2. Give two examples or uses of {topic}.",
        f"3. How would you explain {topic} to a classmate?",
        "\n## Homework",
        f"Write three things learned about {topic} and prepare one question for the next class.",
        "\n## Expected learning outcomes",
        f"Students can describe {topic}, give examples, and complete the class activity.",
    ])
    if extra:
        parts.extend(["\n## Teacher notes to incorporate", extra])
    parts.append("\n*Offline template: review and adapt the activities to your textbook and students.*")
    return "\n\n".join(parts)


if st.session_state.current_page == "AI":
    attendance_tab, lesson_tab = st.tabs(["🤖 Attendance Assistant", "📚 Lesson Plan Agent"])
    with attendance_tab:
        # =========================================================
        # AI CHAT
        # =========================================================

        st.subheader("🤖 Ask School AI")

        st.caption(
            'Ask questions like: "What is Aarav\'s attendance?"'
        )

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])


        prompt = st.chat_input(
            "Ask about student attendance..."
        )

        if prompt:
            st.session_state.messages.append({
                "role": "user",
                "content": prompt
            })

            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                with st.spinner("🤖 Checking attendance..."):
                    try:
                        result = Runner.run_sync(
                            agent,
                            prompt
                        )

                        response = result.final_output

                    except Exception as e:
                        response = f"⚠️ Error: {e}"

                st.markdown(response)

            st.session_state.messages.append({
                "role": "assistant",
                "content": response
            })

    with lesson_tab:
        st.caption("Mahatma Gandhi English School • Create, edit, save and download lesson plans")
        lesson_agent = Agent(
            name="Lesson Planning Assistant",
            instructions=(
                "You are a lesson planning assistant for Mahatma Gandhi English School. "
                "Create clear, practical lesson plans for school teachers in simple English. "
                "Use the supplied class, subject, topic, teaching date and number of periods exactly. "
                "Include learning objectives, required materials, a short introduction, "
                "step-by-step teaching activities with time, student activity, assessment "
                "questions, homework and expected learning outcomes. Use age-appropriate "
                "activities. Assume each period is 40 minutes unless the request specifies "
                "another duration; distribute the activities across all periods. Do not "
                "invent textbook page numbers or claim official curriculum alignment. "
                "If a chat request gives only a topic, ask for missing class, subject, "
                "teaching date and periods before writing the plan. Format as Markdown."
            ),
        )

        with st.form("lesson_plan_form"):
            col1, col2 = st.columns(2)
            with col1:
                lp_class = st.text_input("Class *", placeholder="e.g. 5")
                lp_subject = st.text_input("Subject *", placeholder="e.g. Computer")
                lp_topic = st.text_input("Topic *", placeholder="e.g. Introduction to MS Word")
            with col2:
                lp_date = st.date_input("Teaching date *", value=date.today())
                lp_periods = st.number_input("Number of periods *", min_value=1, max_value=20, value=2, step=1)
                lp_minutes = st.number_input("Minutes per period", min_value=20, max_value=120, value=40, step=5)
            extra = st.text_area("Additional instructions (optional)", placeholder="Learning level, available materials or activity ideas")
            generation_mode = st.radio("Generation mode", ["AI (uses API credits)", "Offline template (free)"],
                                       horizontal=True)
            generate_plan = st.form_submit_button("✨ Generate lesson plan", type="primary")

        if generate_plan:
            if not all([lp_class.strip(), lp_subject.strip(), lp_topic.strip()]):
                st.error("Please enter class, subject and topic.")
            else:
                request = (
                    f"Class: {lp_class.strip()}\nSubject: {lp_subject.strip()}\n"
                    f"Topic: {lp_topic.strip()}\nTeaching date: {lp_date.isoformat()}\n"
                    f"Number of periods: {int(lp_periods)}\nMinutes per period: {int(lp_minutes)}\n"
                    f"Additional instructions: {extra.strip() or 'None'}"
                )
                plan_text = None
                if generation_mode == "Offline template (free)":
                    plan_text = make_offline_lesson_plan(lp_class.strip(), lp_subject.strip(),
                                                        lp_topic.strip(), lp_date, int(lp_periods),
                                                        int(lp_minutes), extra.strip())
                else:
                    with st.spinner("Creating lesson plan..."):
                        try:
                            result = Runner.run_sync(lesson_agent, request)
                            plan_text = str(result.final_output)
                        except Exception as exc:
                            error_text = str(exc).lower()
                            if any(code in error_text for code in ("insufficient_quota", "credit_balance_exhausted", "no credits remaining")):
                                st.warning("OpenAI API credits are exhausted. Created an offline template instead. "
                                           "You can edit it below; AI generation needs API credits.")
                                plan_text = make_offline_lesson_plan(lp_class.strip(), lp_subject.strip(),
                                                                    lp_topic.strip(), lp_date, int(lp_periods),
                                                                    int(lp_minutes), extra.strip())
                            else:
                                st.error(f"Could not generate the lesson plan: {exc}")
                if plan_text:
                    st.session_state.lesson_draft = {
                        "class_name": lp_class.strip(), "subject": lp_subject.strip(),
                        "topic": lp_topic.strip(), "teaching_date": lp_date,
                        "periods": int(lp_periods), "text": plan_text,
                    }
                    st.session_state.pop("lesson_draft_editor", None)

        draft = st.session_state.get("lesson_draft")
        if draft:
            st.subheader("Review your lesson plan")
            edited_plan = st.text_area("Edit before saving", value=draft["text"], height=500, key="lesson_draft_editor")
            if edited_plan != draft["text"]:
                draft["text"] = edited_plan
            st.download_button("📥 Download as Markdown", data=edited_plan,
                               file_name=f"lesson_plan_{draft['teaching_date']:%Y%m%d}.md",
                               mime="text/markdown")
            if st.button("💾 Save lesson plan", type="primary"):
                if not edited_plan.strip():
                    st.error("The lesson plan is empty.")
                else:
                    db = SessionLocal()
                    try:
                        assignment_metadata.create_all(db.get_bind(), tables=[lesson_plans], checkfirst=True)
                        db.execute(lesson_plans.insert().values(
                            school_code=st.session_state.school_code,
                            created_by=st.session_state.username,
                            class_name=draft["class_name"], subject=draft["subject"],
                            topic=draft["topic"], teaching_date=draft["teaching_date"],
                            periods=draft["periods"], plan_text=edited_plan,
                            created_at=datetime.utcnow(),
                        ))
                        db.commit()
                        st.success("Lesson plan saved successfully.")
                    except Exception as exc:
                        db.rollback()
                        st.error(f"Could not save the lesson plan: {exc}")
                    finally:
                        db.close()

        st.divider()
        st.subheader("Saved lesson plans")
        db = SessionLocal()
        try:
            assignment_metadata.create_all(db.get_bind(), tables=[lesson_plans], checkfirst=True)
            saved = db.execute(select(lesson_plans).where(
                lesson_plans.c.school_code == st.session_state.school_code,
            ).order_by(lesson_plans.c.created_at.desc()).limit(50)).mappings().all()
            if not saved:
                st.info("No lesson plans saved yet.")
            for plan in saved:
                with st.expander(f"{plan['teaching_date']} • Class {plan['class_name']} • {plan['subject']} • {plan['topic']}"):
                    st.caption(f"Created by {plan['created_by']} • {plan['periods']} period(s)")
                    st.markdown(plan["plan_text"])
                    st.download_button("📥 Download", data=plan["plan_text"],
                                       file_name=f"lesson_plan_{plan['id']}.md", mime="text/markdown",
                                       key=f"download_lesson_{plan['id']}")
        except Exception as exc:
            st.error(f"Could not load saved lesson plans: {exc}")
        finally:
            db.close()

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🎓 School AI Assistant • "
    "Python + Streamlit + SQLAlchemy + OpenAI Agents"
)
