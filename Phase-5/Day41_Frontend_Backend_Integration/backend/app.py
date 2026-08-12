from flask import Flask, jsonify
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


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "Day 41 Flask API is running",
        "endpoint": "/api/students"
    })


@app.route("/api/students", methods=["GET"])
def get_students():
    return jsonify(STUDENTS)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
