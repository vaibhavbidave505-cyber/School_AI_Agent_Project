import streamlit as st
import pandas as pd
import time
from pathlib import Path
from dotenv import load_dotenv
from agents import Agent, Runner
from agents.decorators import tool

# =========================================================
# SETUP
# =========================================================

load_dotenv()

st.set_page_config(
    page_title="School AI Assistant",
    page_icon="🎓",
    layout="wide"
)

# =========================================================
# DEMO SCHOOL LOGIN
# NOTE: This is a demo login. For production, use a database
# and hashed passwords.
# =========================================================

SCHOOLS = {
    "SCHOOL001": {
        "school_name": "Sunrise Public School",
        "username": "admin",
        "password": "admin123"
    },
    "SCHOOL002": {
        "school_name": "Green Valley School",
        "username": "admin",
        "password": "admin123"
    },
    "SCHOOL003": {
        "school_name": "Bright Future Academy",
        "username": "admin",
        "password": "admin123"
    }
}

# =========================================================
# LOGIN SECURITY
# =========================================================

MAX_LOGIN_ATTEMPTS = 5
LOCKOUT_SECONDS = 300  # 5 minutes

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "locked_until" not in st.session_state:
    st.session_state.locked_until = 0.0

# =========================================================
# LOGIN PAGE
# =========================================================

def login_page():

    st.markdown(
        """
        <style>
        .login-title {
            text-align: center;
            font-size: 42px;
            font-weight: 800;
            margin-top: 60px;
        }
        .login-subtitle {
            text-align: center;
            font-size: 18px;
            margin-bottom: 35px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="login-title">🎓 School AI Assistant</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="login-subtitle">Smart Attendance Management System</div>',
        unsafe_allow_html=True
    )

    left, center, right = st.columns([1, 1.5, 1])

    with center:

        with st.container(border=True):

            st.subheader("🔐 School Login")

            school_code = st.text_input(
                "🏫 School Code",
                placeholder="Example: SCHOOL001"
            )

            username = st.text_input(
                "👤 Username",
                placeholder="Enter username"
            )

            password = st.text_input(
                "🔑 Password",
                type="password",
                placeholder="Enter password"
            )

            login_clicked = st.button(
                "🚀 Login",
                type="primary",
                width="stretch"
            )

            if login_clicked:

                # Check whether the account is temporarily locked
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

                else:

                    code = school_code.strip().upper()

                    valid_login = (
                        code in SCHOOLS
                        and username.strip() == SCHOOLS[code]["username"]
                        and password == SCHOOLS[code]["password"]
                    )

                    if valid_login:

                        st.session_state.logged_in = True
                        st.session_state.school_code = code
                        st.session_state.school_name = SCHOOLS[code]["school_name"]
                        st.session_state.failed_attempts = 0
                        st.session_state.locked_until = 0.0

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
                                f"❌ Invalid School Code, username, or password. "
                                f"{attempts_left} attempt(s) remaining."
                            )

            st.divider()

            st.caption("Demo login:")
            st.code(
                "School Code: SCHOOL001\n"
                "Username: admin\n"
                "Password: admin123"
            )

    st.divider()

    st.caption(
        "🎓 School AI Assistant • Secure School Attendance Platform"
    )


# =========================================================
# CHECK LOGIN
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_page()
    st.stop()


# =========================================================
# LOAD ATTENDANCE DATA
# =========================================================

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "attendance.csv"

try:

    df = pd.read_csv(CSV_FILE)

    df.columns = df.columns.str.strip().str.lower()

    required_columns = {
        "name",
        "class",
        "total_days",
        "present_days"
    }

    missing = required_columns - set(df.columns)

    if missing:
        st.error(
            f"❌ Missing columns in attendance.csv: {', '.join(sorted(missing))}"
        )
        st.stop()

    df["name"] = df["name"].astype(str).str.strip()
    df["class"] = df["class"].astype(str).str.strip()

    df["total_days"] = pd.to_numeric(
        df["total_days"], errors="coerce"
    )

    df["present_days"] = pd.to_numeric(
        df["present_days"], errors="coerce"
    )

    df["attendance_percentage"] = (
        df["present_days"] / df["total_days"] * 100
    )

except Exception as e:

    st.error(f"❌ Could not load attendance.csv: {e}")
    st.stop()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("🎓 School AI")

    st.success(
        f"🏫 {st.session_state.school_name}"
    )

    st.caption(
        f"School Code: {st.session_state.school_code}"
    )

    st.divider()

    st.subheader("✨ Features")

    st.write("✅ Student Attendance")
    st.write("📊 Attendance Analytics")
    st.write("🔎 Student Search")
    st.write("🤖 AI Assistant")

    st.divider()

    st.info(
        f"👨‍🎓 Total Students: {len(df)}"
    )

    if st.button("🚪 Logout", width="stretch"):

        st.session_state.logged_in = False
        st.session_state.pop("school_code", None)
        st.session_state.pop("school_name", None)
        st.session_state.messages = []

        st.rerun()


# =========================================================
# HEADER
# =========================================================

st.title("🎓 School AI Assistant")

st.caption(
    f"Welcome to {st.session_state.school_name} 👋"
)

st.divider()


# =========================================================
# DASHBOARD METRICS
# =========================================================

st.subheader("📊 Attendance Overview")

total_students = len(df)

average_attendance = df[
    "attendance_percentage"
].mean()

total_present = int(
    df["present_days"].sum()
)

total_days = int(
    df["total_days"].sum()
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👨‍🎓 Students",
        total_students
    )

with col2:
    st.metric(
        "📊 Average Attendance",
        f"{average_attendance:.1f}%"
    )

with col3:
    st.metric(
        "✅ Present Days",
        total_present
    )

with col4:
    st.metric(
        "📅 Total Days",
        total_days
    )

st.divider()


# =========================================================
# STUDENT SEARCH
# =========================================================

st.subheader("🔎 Student Overview")

student_names = sorted(
    df["name"].tolist()
)

selected_student = st.selectbox(
    "Select Student",
    student_names
)

student = df[
    df["name"] == selected_student
].iloc[0]

attendance = float(
    student["attendance_percentage"]
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("### 👤 Student Details")

    st.info(
        f"""
**Student:** {student['name']}

**Class:** {student['class']}

**Total Days:** {int(student['total_days'])}

**Present Days:** {int(student['present_days'])}
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


# =========================================================
# ALL STUDENTS
# =========================================================

st.subheader("📋 All Students")

display_df = df[
    [
        "name",
        "class",
        "total_days",
        "present_days",
        "attendance_percentage"
    ]
].copy()

display_df.columns = [
    "Student",
    "Class",
    "Total Days",
    "Present Days",
    "Attendance %"
]

display_df["Attendance %"] = (
    display_df["Attendance %"].round(1)
)

st.dataframe(
    display_df,
    width="stretch",
    hide_index=True
)

st.divider()


# =========================================================
# AI TOOL
# =========================================================

@tool
def get_attendance(student_name: str) -> str:
    """Check a student's attendance."""

    search_name = student_name.strip().lower()

    result = df[
        df["name"].str.lower().str.strip()
        == search_name
    ]

    if result.empty:

        return (
            f"No attendance record found "
            f"for {student_name}."
        )

    row = result.iloc[0]

    percentage = (
        row["present_days"] /
        row["total_days"] * 100
    )

    return (
        f"Student: {row['name']}\n"
        f"Class: {row['class']}\n"
        f"Total Days: {int(row['total_days'])}\n"
        f"Present Days: {int(row['present_days'])}\n"
        f"Attendance: {percentage:.2f}%"
    )


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


# =========================================================
# AI CHAT
# =========================================================

st.subheader("🤖 Ask School AI")

st.caption(
    'Ask questions like: "What is Aarav\'s attendance?"'
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"]
        )

prompt = st.chat_input(
    "Ask about student attendance..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner(
            "🤖 Checking attendance..."
        ):

            try:

                result = Runner.run_sync(
                    agent,
                    prompt
                )

                response = result.final_output

            except Exception as e:

                response = f"⚠️ Error: {e}"

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🎓 School AI Assistant • "
    "Built with Python + Streamlit + OpenAI Agents"
)
