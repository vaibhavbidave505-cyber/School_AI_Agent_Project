import bcrypt
from database import SessionLocal, User


def create_user(user_id, name, username, password, role):
    db = SessionLocal()

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    user = User(
        user_id=user_id,
        name=name,
        username=username,
        password_hash=password_hash,
        role=role,
        school_code="SCHOOL001"
    )

    db.add(user)
    db.commit()
    db.close()

    print(f"✅ {role} created: {user_id}")


create_user(
    "PRI001",
    "Principal",
    "principal",
    "Principal@123",
    "principal"
)

create_user(
    "TCH001",
    "Teacher",
    "teacher",
    "Teacher@123",
    "teacher"
)

print("🎉 Principal and Teacher users created successfully!")