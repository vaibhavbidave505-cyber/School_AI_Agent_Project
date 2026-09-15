import streamlit as st
from dotenv import load_dotenv
from agents import Agent, Runner
from agents.decorators import tool
import pandas as pd


load_dotenv()


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="School AI Agent",
    page_icon="🎓",
    layout="centered"
)


# -----------------------------
# Attendance Tool
# -----------------------------

@tool
def get_attendance(student_name: str) -> str:
    """Check a student's attendance from attendance.csv."""

    try:
        df = pd.read_csv("attendance.csv")

        # Clean column names
        df.columns = df.columns.str.strip().str.lower()

        # Clean student names
        df["name"] = df["name"].astype(str).str.strip()

        result = df[
            df["name"].str.lower() == student_name.strip().lower()
        ]

        if result.empty:
            return f"No attendance record found for {student_name}."

        row = result.iloc[0]

        total_days = int(row["total_days"])
        present_days = int(row["present_days"])

        percentage = (present_days / total_days) * 100

        return (
            f"Student: {row['name']}\n"
            f"Class: {row['class']}\n"
            f"Total Days: {total_days}\n"
            f"Present Days: {present_days}\n"
            f"Attendance: {percentage:.2f}%"
        )

    except Exception as e:
        return f"Attendance tool error: {e}"


# -----------------------------
# AI Agent
# -----------------------------

agent = Agent(
    name="School AI Agent",

    instructions="""
    You are a helpful School AI Assistant.

    You can help users with:
    - Student attendance
    - Basic school-related questions
    - Explaining information clearly

    When the user asks about a student's attendance,
    use the get_attendance tool.

    Do not invent attendance information.
    If attendance data is not available, clearly say so.
    """,

    tools=[get_attendance]
)


# -----------------------------
# UI
# -----------------------------

st.title("🎓 School AI Agent")

st.write(
    "Ask me about student attendance or school-related information."
)


# -----------------------------
# Chat history
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# User input
# -----------------------------

prompt = st.chat_input(
    "Ask something about the school..."
)


if prompt:

    # Display user message

    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    # Run AI Agent

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                result = Runner.run_sync(
                    agent,
                    prompt
                )

                response = result.final_output

            except Exception as e:

                response = f"⚠️ Error: {e}"

        st.markdown(response)


    # Save assistant response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )