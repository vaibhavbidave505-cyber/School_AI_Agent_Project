import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, inspect, text
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()


def _normalize_database_url(url: str) -> str:
    url = (url or "").strip()

    if not url:
        return "sqlite:///school.db"

    if url.startswith("postgres://"):
        return "postgresql+psycopg2://" + url[len("postgres://"):]

    if url.startswith("postgresql://") and "+psycopg2" not in url:
        return "postgresql+psycopg2://" + url[len("postgresql://"):]

    return url


DATABASE_URL = _normalize_database_url(
    os.getenv("DATABASE_URL", "sqlite:///school.db")
)

engine_kwargs = {
    "echo": False,
    "pool_pre_ping": True,
}

if DATABASE_URL.startswith("sqlite"):
    engine_kwargs["connect_args"] = {"check_same_thread": False}
else:
    # Reuse PostgreSQL connections so Neon is not reconnected for every query.
    # A moderately sized local pool prevents the previous 5+3 QueuePool timeout.
    engine_kwargs.update({
        "pool_recycle": 300,
        "pool_size": 10,
        "max_overflow": 10,
        "pool_timeout": 30,
        "pool_use_lifo": True,
        "use_native_hstore": False,
        "connect_args": {
            "connect_timeout": 8,
            "keepalives": 1,
            "keepalives_idle": 30,
            "keepalives_interval": 10,
            "keepalives_count": 3,
        },
    })

engine = create_engine(DATABASE_URL, **engine_kwargs)
Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    class_name = Column(String, nullable=False)
    division = Column(String, nullable=False)
    gender = Column(String)
    parent_contact = Column(String)
    school_code = Column(String, nullable=False, default="SCHOOL001", index=True)
    total_days = Column(Integer, default=0)
    present_days = Column(Integer, default=0)


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), index=True)
    date = Column(Date, nullable=False, index=True)
    status = Column(String, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)  # principal / teacher
    school_code = Column(String, nullable=False, index=True)
    phone = Column(String)
    phone_verified = Column(Integer, nullable=False, default=0)


# Production fast-start mode.
# The cloud database is already migrated, so normal app startup should not
# perform remote CREATE TABLE / schema-inspection calls.  Set
# RUN_DB_SCHEMA_CHECKS=1 only when intentionally initializing/upgrading schema.
RUN_DB_SCHEMA_CHECKS = os.getenv("RUN_DB_SCHEMA_CHECKS", "0").strip().lower() in (
    "1", "true", "yes", "on"
)

if RUN_DB_SCHEMA_CHECKS:
    Base.metadata.create_all(engine)


def _ensure_user_columns():
    """
    Backward-compatible schema check for both SQLite and PostgreSQL.
    """
    inspector = inspect(engine)

    if "users" not in inspector.get_table_names():
        return

    columns = {col["name"] for col in inspector.get_columns("users")}

    with engine.begin() as conn:
        if "phone" not in columns:
            conn.execute(text("ALTER TABLE users ADD COLUMN phone VARCHAR"))

        if "phone_verified" not in columns:
            conn.execute(
                text(
                    "ALTER TABLE users "
                    "ADD COLUMN phone_verified INTEGER NOT NULL DEFAULT 0"
                )
            )


if RUN_DB_SCHEMA_CHECKS:
    _ensure_user_columns()

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)

db_name = "PostgreSQL" if engine.dialect.name == "postgresql" else "SQLite"
print(f"✅ School database connected / checked successfully! ({db_name})")
