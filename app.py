import streamlit as st
# =========================================================
# 🎨 SCHOOL AI - MODERN UI THEME
# =========================================================

st.set_page_config(
    page_title="SchoolAI",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
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





# =========================================================
# SETUP
# =========================================================

load_dotenv()

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
                  "user_id", "user_name", "role", "messages"):
        st.session_state[field] = [] if field == "messages" else (
            False if field == "logged_in" else None if field == "user_id" else ""
        )
    st.session_state.current_page = "Dashboard"


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
# LOGIN PAGE
# =========================================================

def login_page():
    st.markdown("""
    <style>
    [data-testid="stSidebar"], [data-testid="collapsedControl"] {display: none;}
    .stApp {background: radial-gradient(circle at 12% 10%, #dbeafe 0, transparent 34%),
            radial-gradient(circle at 90% 85%, #ccfbf1 0, transparent 31%), #f4f7fc;}
    .block-container {max-width: 1160px; padding-top: 6vh; padding-bottom: 2rem;}
    .school-hero {min-height: 485px; padding: 42px 38px; border-radius: 26px;
        background: linear-gradient(145deg, #0f172a, #172554 55%, #1d4ed8);
        box-shadow: 0 22px 50px rgba(23,37,84,.22); color: white;
        position: relative; overflow: hidden;}
    .school-hero:after {content: ""; position: absolute; width: 290px; height: 290px;
        border-radius: 50%; right: -110px; top: -90px; border: 48px solid rgba(255,255,255,.06);}
    .hero-brand {font-size: 18px; font-weight: 800; letter-spacing: .03em; color: #bfdbfe;}
    .hero-icon {font-size: 57px; margin: 56px 0 8px;}
    .hero-title {font-size: clamp(32px, 3.5vw, 47px); line-height: 1.14;
        letter-spacing: -.035em; font-weight: 850; max-width: 450px;}
    .hero-copy {font-size: 17px; line-height: 1.65; color: #dbeafe; max-width: 425px; margin-top: 18px;}
    .hero-tags {margin-top: 38px; display: flex; flex-wrap: wrap; gap: 9px;}
    .hero-tags span {background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.17);
        padding: 8px 12px; border-radius: 100px; font-size: 13px; color: #eff6ff;}
    .login-intro {margin: 32px 0 24px;}
    .login-eyebrow {color: #2563eb; font-size: 13px; font-weight: 800; letter-spacing: .11em;}
    .login-heading {font-size: 35px; font-weight: 850; color: #0f172a; margin: 9px 0 7px;}
    .login-detail {font-size: 15px; color: #64748b; line-height: 1.6;}
    .login-foot {text-align: center; color: #64748b; font-size: 13px; margin-top: 32px;}
    @media (max-width: 768px) {
        .block-container {padding-top: 1rem;}
        .school-hero {min-height: 0; padding: 26px;}
        .hero-icon {margin: 18px 0 4px; font-size: 40px;}
        .hero-title {font-size: 30px;}
        .hero-tags {margin-top: 18px;}
        .login-intro {margin: 18px 0;}
    }
    </style>
    """, unsafe_allow_html=True)

    hero, form = st.columns([1.12, 1], gap="large", vertical_alignment="center")
    with hero:
        st.markdown("""
        <div class="school-hero">
            <div class="hero-brand">✦ SCHOOL AI</div>
            <div class="hero-icon">🏫</div>
            <div class="hero-title">A smarter way to care for every student.</div>
            <div class="hero-copy">Attendance records, class insights and student information in one simple school workspace.</div>
            <div class="hero-tags"><span>✓ Attendance</span><span>▥ Analytics</span><span>✦ AI Assistant</span></div>
        </div>
        """, unsafe_allow_html=True)

    with form:
        st.markdown("""
        <div class="login-intro">
            <div class="login-eyebrow">WELCOME BACK</div>
            <div class="login-heading">Sign in to School AI</div>
            <div class="login-detail">Enter your school account details to open your dashboard.</div>
        </div>
        """, unsafe_allow_html=True)
        with st.container(border=True):
            username = st.text_input("Username", placeholder="Your username", key="login_username")
            password = st.text_input("Password", type="password", placeholder="Your password", key="login_password")
            login_clicked = st.button("Sign in →", type="primary", use_container_width=True)

            if login_clicked:
                now = time.time()

                if now < st.session_state.locked_until:
                    remaining = int(
                        st.session_state.locked_until - now
                    )
                    minutes = remaining // 60
                    seconds = remaining % 60

                    st.error(
                        f"🔒 Too many failed attempts. "
                        f"Try again in {minutes}m {seconds}s."
                    )
                    return

                db = SessionLocal()
                user = db.query(User).filter(    
                    User.username == username.strip()
                    ).first()
                valid_login = False
                if user:
                    valid_login = verify_password(
                    password,
                    user.password_hash
                 )
                db.close()   

                if valid_login: 
                    st.session_state.just_logged_out = False
                    st.session_state.logged_in = True
                    st.session_state.school_code = user.school_code
                    st.session_state.school_name = user.school_code
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
                            "school_name": user.school_code,
                            "username": user.username,
                            "user_id": user.user_id,
                            "user_name": user.name,
                            "role": user.role,
                        }
                    st.query_params[SESSION_PARAM] = token

                    st.success("✅ Login successful!")
                    st.rerun()

                else:
                    st.session_state.failed_attempts += 1

                    attempts_left = (
                        MAX_LOGIN_ATTEMPTS
                        - st.session_state.failed_attempts
                    )

                    if attempts_left <= 0:
                        st.session_state.locked_until = (
                            time.time() + LOCKOUT_SECONDS
                        )

                        st.error(
                            "🔒 Too many failed password attempts. "
                            "Login is locked for 5 minutes."
                        )
                    else:
                        st.error(
                            f"❌ Invalid username or password. "
                            f"{attempts_left} attempt(s) remaining."
                        )

    st.markdown('<div class="login-foot">🎓 School AI Assistant · Secure school access</div>', unsafe_allow_html=True)


# =========================================================
# CHECK LOGIN
# =========================================================

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


@st.fragment(run_every="10s")
def session_countdown():
    current = session_record(st.query_params.get(SESSION_PARAM))
    if not current:
        clear_login()
        st.rerun(scope="app")
    remaining = max(0, int(current["expires_at"] - time.time()))
    st.caption(f"⏱️ Session ends in {remaining // 60:02d}:{remaining % 60:02d}")





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

if st.sidebar.button("🔎 Student Search", use_container_width=True):
    st.session_state.current_page = "Search"
    st.rerun()

if st.sidebar.button("🤖 AI Assistant", use_container_width=True):
    st.session_state.current_page = "AI"
    st.rerun()

if str(st.session_state.role).strip().lower() == "principal":
    if st.sidebar.button("🔐 Login Protection", use_container_width=True):
        st.session_state.current_page = "Security"
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
    clear_login()
    st.rerun()


# Every feature is a separate view with a direct route home.
PAGE_LABELS = {
    "Dashboard": "🏠 Dashboard",
    "Attendance": "✅ Student Attendance",
    "Parent Messages": "📨 Parent Messages",
    "Analytics": "📊 Attendance Analytics",
    "Search": "🔎 Student Search",
    "AI": "🤖 AI Assistant",
    "Security": "🔐 Login Protection",
}
if (st.session_state.current_page not in PAGE_LABELS or
        (st.session_state.current_page == "Security" and
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
        ("🔎", "Student Search", "Find a student and view their attendance details.", "Search"),
        ("🤖", "AI Assistant", "Ask questions about student attendance.", "AI"),
    ]
    if str(st.session_state.role).strip().lower() == "principal":
        feature_pages.append(("🔐", "Login Protection", "View your school account security settings.", "Security"))
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
                 "Class teacher": teacher_map.get((class_name, division), "Not assigned"),
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
                            db.delete(student)
                            db.commit()
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
                st.markdown("#### 👩‍🏫 Assign class teacher")
                with st.form("class_teacher_form"):
                    new_teacher = st.text_input("Class teacher name", value=teacher_name,
                                                placeholder="Enter teacher's full name")
                    save_teacher = st.form_submit_button("💾 Save teacher name", type="primary")
                if save_teacher:
                    if not new_teacher.strip():
                        st.error("Enter a teacher name.")
                    else:
                        db = SessionLocal()
                        try:
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
                                ).values(teacher_name=new_teacher.strip()))
                            else:
                                db.execute(teacher_assignments.insert().values(
                                    school_code=st.session_state.school_code,
                                    class_name=class_name,
                                    division=division_name,
                                    teacher_name=new_teacher.strip(),
                                ))
                            db.commit()
                            class_teachers[selected_group] = new_teacher.strip()
                            st.success(f"Teacher {new_teacher.strip()} saved for Class {class_name}{division_name}.")
                        except Exception as exc:
                            db.rollback()
                            st.error(f"Could not save teacher: {exc}")
                        finally:
                            db.close()
            else:
                st.info(f"👩‍🏫 Class teacher: {teacher_name or 'Not assigned yet'}")

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
                save_attendance = st.form_submit_button("💾 Save class attendance", type="primary")
            if save_attendance:
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
                            old_record.status = status
                        else:
                            db.add(Attendance(student_id=student_id, date=attendance_date, status=status))
                            student.total_days = int(student.total_days or 0) + 1
                            if status == "present":
                                student.present_days = int(student.present_days or 0) + 1
                    db.commit()
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
    st.caption("Based on the latest three dates with recorded attendance for each class. "
               "Review the attendance and phone number before sending. WhatsApp opens a draft; you press Send.")
    try:
        from urllib.parse import quote
        import re
        absence_candidates = get_three_day_absences(st.session_state.school_code)
        if not absence_candidates:
            st.info("No students with three recorded class days absent in a row.")
        for candidate in absence_candidates:
            label = (f"{candidate['name']} · Class {candidate['class']}"
                     f"{candidate['division'] or ''} · Last recorded {candidate['dates'][-1]:%d %b %Y}")
            with st.expander(label):
                st.write("Absent dates: " + ", ".join(d.strftime("%d %b %Y")
                                                   for d in candidate["dates"]))
                phone = candidate["parent_contact"].strip()
                if not re.fullmatch(r"\+[1-9]\d{7,14}", phone):
                    st.warning("Add or correct this parent's number before contacting them.")
                    continue
                message = (f"Dear parent, {candidate['name']} has been absent for three "
                           "recorded school days. Please contact Mahatma Gandhi English School.")
                st.code(message, language=None)
                whatsapp_url = f"https://wa.me/{phone[1:]}?text={quote(message)}"
                st.link_button("💬 Open WhatsApp message", whatsapp_url)
    except Exception as exc:
        st.error(f"Could not prepare parent contact list: {exc}")


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
