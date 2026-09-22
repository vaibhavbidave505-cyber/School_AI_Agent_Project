import streamlit as st
import time
from datetime import date
from pathlib import Path

import bcrypt
from dotenv import load_dotenv
from sqlalchemy import func

from agents import Agent, Runner
from agents.decorators import tool

from database import SessionLocal, Student, Attendance, User



# =========================================================
# SETUP
# =========================================================

load_dotenv()

st.set_page_config(
    page_title="School AI Assistant",
    page_icon="🎓",
    layout="wide"
)

MAX_LOGIN_ATTEMPTS = 5
LOCKOUT_SECONDS = 300  # 5 minutes


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "logged_in": False,
    "failed_attempts": 0,
    "locked_until": 0.0,
    "messages": [],
    "school_code": "",
    "school_name": "",
    "username": "",
}

for key, value in defaults.items():
    if key not in st.session_state:
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
                    st.session_state.logged_in = True
                    st.session_state.school_code = SCHOOL_CODE
                    st.session_state.school_code = user.school_code
                    st.session_state.username = username.strip()

                    st.session_state.failed_attempts = 0
                    st.session_state.locked_until = 0.0

                    st.session_state.user_id = user.user_id
                    st.session_state.user_name = user.name
                    st.session_state.role = user.role

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

            st.divider()

            st.caption(
                "Login credentials are read from environment variables "
                "and are not stored in the source code."
            )

    st.divider()

    st.caption(
        "🎓 School AI Assistant • Secure School Attendance Platform"
    )


# =========================================================
# CHECK LOGIN
# =========================================================

if not st.session_state.logged_in:
    login_page()
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
    st.header("🎓 School AI")

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
if st.session_state.role == "principal":
    st.sidebar.divider()

    st.sidebar.subheader("📂 Upload Student CSV")

    uploaded_file = st.sidebar.file_uploader(
    "Choose CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    st.sidebar.success("✅ CSV file selected")

    if st.sidebar.button("📥 Import CSV to this School"):
        try:
            import pandas as pd

            df = pd.read_csv(uploaded_file)
            df.columns = df.columns.astype(str).str.strip().str.lower()

            required_columns = {
                "name",
                "class",
                "total_days",
                "present_days",
                "gender"
            }

            if not required_columns.issubset(df.columns):
                missing = required_columns - set(df.columns)
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
                   

                    if not name or not class_value:
                        continue

                    # Example: 8A → class_name = 8, division = A
                    if class_value[-1].isalpha():
                        class_name = class_value[:-1]
                        division = class_value[-1]
                    else:
                        class_name = class_value
                        division = ""

                    existing = db.query(Student).filter(
                        Student.name == name,
                        Student.school_code == st.session_state.school_code
                    ).first()

                    if existing:
                        existing.class_name = class_name
                        existing.division = division
                        existing.gender = gender
                        existing.total_days = int(row["total_days"])
                        existing.present_days = int(row["present_days"])
                        updated += 1
                    else:
                        student = Student(
                            name=name,
                            class_name=class_name,
                            division=division,
                            parent_contact="",
                            total_days=int(row["total_days"]),
                            present_days=int(row["present_days"]),
                            gender=gender,
                            school_code=st.session_state.school_code
                        )

                        db.add(student)
                        imported += 1

                db.commit()
                db.close()

                st.sidebar.success(
                    f"✅ Import complete! "
                    f"New: {imported}, Updated: {updated}"
                )

                st.rerun()

        except Exception as e:
            st.sidebar.error(f"❌ Import failed: {e}")

    

    st.subheader("✨ Features")
if st.session_state.role == "principal":
    st.write("✅ Student Attendance")
    st.write("📊 Attendance Analytics")
    st.write("🔎 Student Search")
    st.write("🤖 AI Assistant")
    st.write("🔐 Login Protection")

elif st.session_state.role == "teacher":
    st.write("✅ Student Attendance")
    st.write("🔎 Student Search")
    st.write("🤖 AI Assistant")

    st.divider()

    st.info(
        f"👨‍🎓 Total Students: {len(student_rows)}"
    )

    st.sidebar.divider()

if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.session_state.school_code = ""
    st.session_state.school_name = ""
    st.session_state.username = ""
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

total_students = len(student_rows)

average_attendance = (
    sum(x["attendance_percentage"] for x in student_rows)
    / total_students
    if total_students
    else 0
)

total_present = sum(
    x["present_days"] for x in student_rows
)

total_days = sum(
    x["total_days"] for x in student_rows
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👨‍🎓 Students", total_students)

with col2:
    st.metric(
        "📊 Average Attendance",
        f"{average_attendance:.1f}%"
    )

with col3:
    st.metric("✅ Present Days", total_present)

with col4:
    st.metric("📅 Total Days", total_days)


st.divider()
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
# STUDENT SEARCH
# =========================================================

st.subheader("🔎 Student Overview")

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

# =========================================================
# DELETE STUDENT - PRINCIPAL ONLY
# =========================================================

if st.session_state.role == "principal" and student_rows:
    st.divider()
    st.subheader("🗑️ Delete Student")

    delete_names = sorted(
        x["name"] for x in student_rows
    )

    delete_student_name = st.selectbox(
        "Select student to delete",
        delete_names,
        key="delete_student_select"
    )

    if st.button("🗑️ Delete Selected Student"):
        st.session_state.confirm_delete_student = delete_student_name

    if st.session_state.get("confirm_delete_student") == delete_student_name:
        st.warning(
            f"⚠️ Are you sure you want to permanently delete "
            f"**{delete_student_name}** and their attendance records?"
        )

        if st.button(
            "✅ Yes, Permanently Delete",
            key="confirm_delete_button"
        ):
            db = SessionLocal()

            try:
                student_to_delete = (
                    db.query(Student)
                    .filter(
                        Student.name == delete_student_name,
                        Student.school_code == st.session_state.school_code
                    )
                    .first()
                )

                if student_to_delete:
                    db.query(Attendance).filter(
                        Attendance.student_id == student_to_delete.id
                    ).delete(
                        synchronize_session=False
                    )

                    db.delete(student_to_delete)
                    db.commit()

                    st.session_state.pop(
                        "confirm_delete_student",
                        None
                    )

                    st.success(
                        f"✅ {delete_student_name} deleted successfully."
                    )

                    st.rerun()

            except Exception as e:
                db.rollback()
                st.error(f"❌ Delete failed: {e}")

            finally:
                db.close()

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
    {str(x["gender"]) for x in student_rows}
)

selected_gender = st.selectbox(
    "⚥ Select Gender",
    ["All"] + gender_options
)
if student_rows:
    display_rows = []

    filtered_students = [
        x for x in student_rows
        if search_name.lower() in x["name"].lower()
        and (
        selected_class == "All"
        or str(x["class"]) == selected_class
    )and (
    selected_division == "All"
    or str(x["division"]) == selected_division
) and (
    selected_gender == "All"
    or str(x.get("gender") or "") == selected_gender
)
    ]

    for x in filtered_students:
        display_rows.append({

        "Student": x["name"],
            "Gender": x["gender"],
            "Class": x["class"],
            "Division": x["division"],
            "Total Days": x["total_days"],
            "Present Days": x["present_days"],
            "Attendance %": round(x["attendance_percentage"], 1),
        })

    st.dataframe(
        display_rows,
        width="stretch",
        hide_index=True
    )


st.divider()
# Class-wise Attendance Chart
if display_rows:
    chart_data = {}

    for row in display_rows:
        class_name = row["Class"]
        chart_data[class_name] = row["Attendance %"]

    st.subheader("📊 Class-wise Attendance")
    st.bar_chart(chart_data)

st.divider()
# Attendance Summary
if display_rows:
    total_students = len(display_rows)
    total_days = sum(row["Total Days"] for row in display_rows)
    present_days = sum(row["Present Days"] for row in display_rows)

    overall_attendance = (
        (present_days / total_days) * 100
        if total_days > 0 else 0
    )

    st.subheader("📌 Attendance Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("👨‍🎓 Total Students", total_students)
    col2.metric("📅 Total Days", total_days)
    col3.metric("✅ Present Days", present_days)
    col4.metric("📊 Overall Attendance", f"{overall_attendance:.1f}%")

# Low Attendance Alert
low_attendance = [
    row for row in display_rows
    if row["Attendance %"] < 80
]

if low_attendance:
    st.warning(
        f"⚠️ {len(low_attendance)} student(s) have attendance below 80%."
    )
else:
    st.success("✅ All students have attendance of 80% or above.")
# Low Attendance Students
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
# Download Low Attendance Report
if low_attendance:
    import pandas as pd

    download_df = pd.DataFrame(low_rows)

    st.download_button(
        label="📥 Download Low Attendance Report",
        data=download_df.to_csv(index=False),
        file_name="low_attendance_report.csv",
        mime="text/csv"
    )    

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
                == student_name.strip().lower()
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


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🎓 School AI Assistant • "
    "Python + Streamlit + SQLAlchemy + OpenAI Agents"
)
