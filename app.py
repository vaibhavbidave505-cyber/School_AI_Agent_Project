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
import re
from urllib.parse import urlencode
from urllib.request import Request, urlopen





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
                  "user_id", "user_name", "role", "messages"):
        st.session_state[field] = [] if field == "messages" else (
            False if field == "logged_in" else None if field == "user_id" else ""
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
    body = f"Your School AI login OTP is {otp}. It expires in 5 minutes. Do not share it."
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


def create_authenticated_session(user):
    """Create the 15-minute application session after authentication is complete."""
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
            <div class="login-detail">Choose Sign in for existing accounts or Principal Registration to create a secured principal account.</div>
        </div>
        """, unsafe_allow_html=True)

        signin_tab, register_tab = st.tabs(["🔐 Sign in", "📝 Principal Registration"])

        with signin_tab:
            with st.container(border=True):
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

                    db = SessionLocal()
                    try:
                        user = db.query(User).filter(User.username == username.strip()).first()
                        valid_login = bool(user) and verify_password(password, user.password_hash)
                    finally:
                        db.close()

                    if valid_login:
                        if str(user.role).strip().lower() == "principal":
                            try:
                                start_principal_otp(user)
                                st.rerun()
                            except Exception as exc:
                                st.error(f"Could not send OTP: {exc}")
                        else:
                            create_authenticated_session(user)
                            st.success("✅ Login successful!")
                            st.rerun()
                    else:
                        st.session_state.failed_attempts += 1
                        attempts_left = MAX_LOGIN_ATTEMPTS - st.session_state.failed_attempts
                        if attempts_left <= 0:
                            st.session_state.locked_until = time.time() + LOCKOUT_SECONDS
                            st.error("🔒 Too many failed password attempts. Login is locked for 5 minutes.")
                        else:
                            st.error(f"❌ Invalid username or password. {attempts_left} attempt(s) remaining.")

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
