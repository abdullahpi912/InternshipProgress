import os
import mysql.connector
from mysql.connector import Error


def get_connection():
    """Open a new MySQL connection using credentials from environment variables."""
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "Abdullah@2007"),
        database=os.environ.get("DB_NAME", "student_management"),
    )


def fetch_all_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, email, course FROM students ORDER BY id")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def insert_student(name, email, course):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, email, course) VALUES (%s, %s, %s)",
        (name, email, course),
    )
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return {"id": new_id, "name": name, "email": email, "course": course}
