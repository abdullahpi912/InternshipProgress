import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from mysql.connector import Error as MySQLError
from dotenv import load_dotenv

from db import fetch_all_students, insert_student

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route("/api/students", methods=["GET"])
def get_students():
    try:
        students = fetch_all_students()
        return jsonify({"success": True, "data": students})
    except MySQLError:
        return jsonify({"success": False, "message": "Unable to connect to database"}), 500


@app.route("/api/students", methods=["POST"])
def create_student():
    body = request.get_json(silent=True) or {}
    name = (body.get("name") or "").strip()
    email = (body.get("email") or "").strip()
    course = (body.get("course") or "").strip()

    # Field validation
    if not name or not email or not course:
        return jsonify({"success": False, "message": "Name, email and course are all required"}), 400

    try:
        student = insert_student(name, email, course)
        return jsonify({"success": True, "message": "Student added successfully", "data": student}), 201
    except MySQLError as e:
        # MySQL error 1062 = duplicate entry (email is UNIQUE)
        if e.errno == 1062:
            return jsonify({"success": False, "message": "A student with this email already exists"}), 409
        return jsonify({"success": False, "message": "Unable to save student"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
