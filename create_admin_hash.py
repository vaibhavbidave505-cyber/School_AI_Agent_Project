import os
import bcrypt

username = input("Admin username [admin]: ").strip() or "admin"
password = input("Admin password: ")

password_hash = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
).decode("utf-8")

print("\nAdd these values to your .env file:\n")
print(f"ADMIN_USERNAME={username}")
print(f"ADMIN_PASSWORD_HASH={password_hash}")
print("SCHOOL_CODE=SCHOOL001")
print("SCHOOL_NAME=School AI Academy")
