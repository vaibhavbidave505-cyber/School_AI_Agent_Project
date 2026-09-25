from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, text
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///school.db"

engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    class_name = Column(String, nullable=False)
    division = Column(String, nullable=False)
    gender = Column(String)
    parent_contact = Column(String)
    school_code = Column(String, nullable=False, default="SCHOOL001")
    total_days = Column(Integer, default=0)
    present_days = Column(Integer, default=0)


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)  # principal / teacher
    school_code = Column(String, nullable=False)
    phone = Column(String)
    phone_verified = Column(Integer, nullable=False, default=0)


Base.metadata.create_all(engine)


def _ensure_user_columns():
    """Safely add OTP-related columns to an existing SQLite users table."""
    with engine.begin() as conn:
        columns = {row[1] for row in conn.execute(text("PRAGMA table_info(users)"))}
        if "phone" not in columns:
            conn.execute(text("ALTER TABLE users ADD COLUMN phone VARCHAR"))
        if "phone_verified" not in columns:
            conn.execute(text("ALTER TABLE users ADD COLUMN phone_verified INTEGER NOT NULL DEFAULT 0"))


_ensure_user_columns()
SessionLocal = sessionmaker(bind=engine)

print("✅ School database created / checked successfully!")
