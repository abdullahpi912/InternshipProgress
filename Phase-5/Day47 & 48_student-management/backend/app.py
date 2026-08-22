import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from mysql.connector import Error as MySQLError
from dotenv import load_dotenv

from db import fetch_all_students, insert_student
from ml.model import FEATURES, load_model, predict

load_dotenv()

app = Flask(__name__)
CORS(app)

# Load the ML model once, at startup — not on every request.
load_model()


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


@app.route("/api/predict", methods=["POST"])
def predict_crop():
    body = request.get_json(silent=True) or {}

    # Presence + type validation for every required feature
    values = {}
    for field in FEATURES:
        if field not in body:
            return jsonify({"success": False, "error": f"Missing required input: {field}"}), 400

        raw = body[field]
        if raw is None or (isinstance(raw, str) and not raw.strip()):
            return jsonify({"success": False, "error": f"{field} cannot be empty"}), 400

        try:
            values[field] = float(raw)
        except (TypeError, ValueError):
            return jsonify({"success": False, "error": f"{field} must be a number"}), 400

    # Basic real-world range checks (the dataset's ph is 0-14, humidity is a %)
    if not (0 <= values["ph"] <= 14):
        return jsonify({"success": False, "error": "ph must be between 0 and 14"}), 400
    if not (0 <= values["humidity"] <= 100):
        return jsonify({"success": False, "error": "humidity must be between 0 and 100"}), 400

    try:
        crop = predict(values)
    except Exception:
        return jsonify({"success": False, "error": "Prediction failed"}), 500

    return jsonify({"success": True, "prediction": crop}), 200


# JSON error handlers (Flask's defaults return HTML, which breaks API clients)
@app.errorhandler(404)
def not_found(e):
    return jsonify({"success": False, "message": "Endpoint not found"}), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"success": False, "message": "Method not allowed on this endpoint"}), 405


@app.errorhandler(500)
def server_error(e):
    return jsonify({"success": False, "message": "Internal server error"}), 500


if __name__ == "__main__":
    # Local dev only — in production, gunicorn runs app:app directly (see docs/day-48-backend-deployment.md)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", debug=True, port=port)
