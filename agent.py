import csv


def load_attendance(filename):
    with open(filename, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def attendance_percentage(student):
    total_days = int(student["total_days"])
    present_days = int(student["present_days"])

    if total_days == 0:
        return 0

    return round((present_days / total_days) * 100, 1)


students = load_attendance("attendance.csv")

for student in students:
    student["attendance"] = attendance_percentage(student)


def show_low_attendance():
    print("\n--- LOW ATTENDANCE STUDENTS ---")

    found = False

    for student in students:
        if student["attendance"] < 75:
            found = True
            print(
                f"{student['name']} | "
                f"Class: {student['class']} | "
                f"Attendance: {student['attendance']}%"
            )

    if not found:
        print("No students found.")


def show_class(class_name):
    print(f"\n--- CLASS {class_name.upper()} ---")

    found = False

    for student in students:
        if student["class"].lower() == class_name.lower():
            found = True
            print(
                f"{student['name']} | "
                f"Attendance: {student['attendance']}%"
            )

    if not found:
        print("Class not found.")


def generate_parent_messages():
    print("\n--- PARENT MESSAGES ---")

    found = False

    for student in students:
        if student["attendance"] < 75:
            found = True

            message = (
                f"Dear Parent, your child {student['name']} "
                f"from class {student['class']} currently has "
                f"{student['attendance']}% attendance. "
                "Please ensure regular attendance."
            )

            print("\n" + message)

    if not found:
        print("No parent messages required.")


def show_dashboard():
    print("\n================================")
    print("       PRINCIPAL DASHBOARD")
    print("================================")

    total_students = len(students)

    if total_students == 0:
        print("No student data available.")
        return

    total_attendance = sum(
        student["attendance"] for student in students
    )

    average_attendance = round(
        total_attendance / total_students, 1
    )

    low_attendance_count = sum(
        1 for student in students
        if student["attendance"] < 75
    )

    lowest_student = min(
        students,
        key=lambda student: student["attendance"]
    )

    print(f"Total Students: {total_students}")
    print(f"Average Attendance: {average_attendance}%")
    print(f"Students Below 75%: {low_attendance_count}")

    print(
        f"Lowest Attendance: {lowest_student['name']} "
        f"({lowest_student['attendance']}%)"
    )

    print("\n--- ALL STUDENTS ---")

    for student in students:
        print(
            f"{student['name']} | "
            f"{student['class']} | "
            f"{student['attendance']}%"
        )


def run_agent():
    while True:
        print("\n================================")
        print("       SCHOOL AI AGENT")
        print("================================")

        print("1. Show low attendance")
        print("2. Show class")
        print("3. Generate parent messages")
        print("4. Show principal dashboard")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            show_low_attendance()

        elif choice == "2":
            class_name = input("Enter class name: ")
            show_class(class_name)

        elif choice == "3":
            generate_parent_messages()

        elif choice == "4":
            show_dashboard()

        elif choice == "5":
            print("\nSchool AI Agent stopped.")
            break

        else:
            print("\nInvalid choice. Please enter 1 to 5.")


run_agent()