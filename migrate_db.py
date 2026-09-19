import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

columns = {row[1] for row in cursor.execute("PRAGMA table_info(students)")}

if "total_days" not in columns:
    cursor.execute("ALTER TABLE students ADD COLUMN total_days INTEGER DEFAULT 0")

if "present_days" not in columns:
    cursor.execute("ALTER TABLE students ADD COLUMN present_days INTEGER DEFAULT 0")

if "school_code" not in columns:
    cursor.execute("ALTER TABLE students ADD COLUMN school_code TEXT NOT NULL DEFAULT 'SCHOOL001'")

conn.commit()
conn.close()

print("Migration complete")