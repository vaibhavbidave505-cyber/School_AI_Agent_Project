import bcrypt
from database import SessionLocal, Base, engine
from sqlalchemy import Column, Integer, String

# Users table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)
    school_id = Column(String, nullable=False)


# Create table
Base.metadata.create_all(engine)


def create_user(name, username, password, role, school_id):
    db = SessionLocal()

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    user = User(
        name=name,
        username=username,
        password_hash=password_hash,
        role=role,
        school_id=school_id
    )

    db.add(user)
    db.commit()
    db.close()


def login_user(username, password):
    db = SessionLocal()

    user = db.query(User).filter(
        User.username == username
    ).first()

    if user:
        if bcrypt.checkpw(
            password.encode("utf-8"),
            user.password_hash.encode("utf-8")
        ):
            db.close()
            return user

    db.close()
    return None


if __name__ == "__main__":
    # Demo Principal account
    create_user(
        name="School Principal",
        username="principal",
        password="admin123",
        role="principal",
        school_id="SCHOOL001"
    )

    print("✅ Principal account created!")
    print("Username: principal")
    print("Password: admin123")