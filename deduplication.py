import hashlib
import sqlite3

from database import get_connection


def generate_hash(name, email):
    normalized_data = (
        name.strip().lower() + "|" + email.strip().lower()
    )

    return hashlib.sha256(
        normalized_data.encode("utf-8")
    ).hexdigest()


def validate_data(name, email):
    name = name.strip()
    email = email.strip().lower()

    if not name:
        return False, "Name cannot be empty."

    if not email:
        return False, "Email cannot be empty."

    if "@" not in email or "." not in email.split("@")[-1]:
        return False, "Invalid email address."

    return True, "Data validated successfully."


def add_record(name, email):
    name = name.strip()
    email = email.strip().lower()

    is_valid, message = validate_data(name, email)

    if not is_valid:
        return "INVALID", message

    data_hash = generate_hash(name, email)

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT id FROM records WHERE data_hash = ?",
            (data_hash,)
        )

        if cursor.fetchone():
            return "DUPLICATE", "This record already exists."

        cursor.execute(
            """
            INSERT INTO records (name, email, data_hash)
            VALUES (?, ?, ?)
            """,
            (name, email, data_hash)
        )

        conn.commit()
        return "SUCCESS", "Unique record added successfully."

    except sqlite3.IntegrityError:
        return "DUPLICATE", "Duplicate record detected."

    finally:
        conn.close()
