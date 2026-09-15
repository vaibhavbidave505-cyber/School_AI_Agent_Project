from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
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
    parent_contact = Column(String)

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

print("✅ School database created successfully!")