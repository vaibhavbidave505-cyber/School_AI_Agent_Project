import getpass
import re
import uuid

import bcrypt

from database import SessionLocal, User


def ask_nonempty(label):
    while True:
        value = input(label).strip()
        if value:
            return value
        print("This field is required.")


def ask_phone():
    while True:
        phone = input("Mobile (+91XXXXXXXXXX): ").strip()
        if re.fullmatch(r"\+[1-9]\d{7,14}", phone):
            return phone
        print("Use international format, for example +919876543210")


def main():
    print("\nCreate / update Principal account\n")
    name = ask_nonempty("Principal name: ")
    username = ask_nonempty("Username: ")
    phone = ask_phone()
    school_code = input("School code [SCHOOL001]: ").strip() or "SCHOOL001"

    while True:
        password = getpass.getpass("Password (minimum 8 characters): ")
        confirm = getpass.getpass("Confirm password: ")
        if len(password) < 8:
            print("Password must be at least 8 characters.")
            continue
        if password != confirm:
            print("Passwords do not match.")
            continue
        break

    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    db = SessionLocal()
    try:
        user = db.query(User).filter(User.username == username).first()
        if user:
            user.name = name
            user.password_hash = password_hash
            user.role = "principal"
            user.school_code = school_code
            user.phone = phone
            user.phone_verified = 1
            action = "updated"
        else:
            user = User(
                user_id=f"principal-{uuid.uuid4().hex[:12]}",
                name=name,
                username=username,
                password_hash=password_hash,
                role="principal",
                school_code=school_code,
                phone=phone,
                phone_verified=1,
            )
            db.add(user)
            action = "created"
        db.commit()
        print(f"\n✅ Principal account {action} successfully.")
        print(f"Username: {username}")
        print(f"Phone: {phone}")
        print("Password is stored only as a bcrypt hash.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
