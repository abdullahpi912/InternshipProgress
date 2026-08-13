import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

STUDENTS = [
    {"id": 1, "name": "Abdullah", "email": "abdullah@example.com", "course": "B.Tech AI & DS"},
    {"id": 2, "name": "Aisha", "email": "aisha@example.com", "course": "B.Tech CSE"},
    {"id": 3, "name": "Rahul", "email": "rahul@example.com", "course": "B.Tech IT"},
    {"id": 4, "name": "Priya", "email": "priya@example.com", "course": "B.Tech ECE"},
    {"id": 5, "name": "Mohammed", "email": "mohammed@example.com", "course": "B.Tech AI & DS"},
]


def empty_mode_enabled():
    return request.args.get("empty") == "true" or os.getenv("DAY43_EMPTY_DATA", "0") == "1"


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "Day 43 Flask API is running",
        "endpoints": {
            "get_students": "GET /api/students",
            "get_empty_students_for_testing": "GET /api/students?empty=true",
            "create_student": "POST /api/students",
        },
    })


@app.route("/api/students", methods=["GET"])
def get_students():
    if empty_mode_enabled():
        return jsonify([])
    return jsonify(STUDENTS)


@app.route("/api/students", methods=["POST"])
def create_student():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON.",
        }), 400

    required_fields = ("name", "email", "course")
    missing_fields = [
        field for field in required_fields
        if not isinstance(data.get(field), str) or not data.get(field).strip()
    ]

    if missing_fields:
        return jsonify({
            "success": False,
            "message": "name, email, and course are required.",
            "missing_fields": missing_fields,
        }), 400

    new_student = {
        "id": max((student["id"] for student in STUDENTS), default=0) + 1,
        "name": data["name"].strip(),
        "email": data["email"].strip(),
        "course": data["course"].strip(),
    }

    STUDENTS.append(new_student)

    return jsonify({
        "success": True,
        "message": "Student created successfully.",
        "student": new_student,
    }), 201


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
