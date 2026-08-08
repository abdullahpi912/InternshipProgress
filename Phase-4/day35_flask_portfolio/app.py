from flask import Flask, jsonify, request, render_template, g
import mysql.connector
import time

app = Flask(__name__)

# ==========================================
# DATABASE CONNECTION
# ==========================================
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Abdullah@2007",   # <-- put your real MySQL root password here
    "database": "portfolio_db"
}


def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)


# ==========================================
# MIDDLEWARE-EQUIVALENTS (Flask uses before/after_request)
# ==========================================

# 1. Request logger — runs on every request
@app.before_request
def request_logger():
    g.start_time = time.time()
    print(f"[REQUEST] {request.method} {request.path}")


# 2. Response timer — attaches X-Response-Time-Ms header, logs duration
@app.after_request
def response_timer(response):
    duration_ms = int((time.time() - g.start_time) * 1000)
    response.headers["X-Response-Time-Ms"] = str(duration_ms)
    print(f"[RESPONSE] {request.method} {request.path} -> {response.status_code} ({duration_ms}ms)")
    return response


# 3. Body validator — used inside POST/PUT routes before touching the DB
def validate_project_body(data):
    if not data or not data.get("title") or not data.get("description"):
        return False
    return True


def validate_message_body(data):
    if not data or not data.get("name") or not data.get("email") or not data.get("message"):
        return False
    return True


# ==========================================
# PAGE ROUTES
# ==========================================
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/home.html')
def home():
    return render_template('home.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/projects.html')
def projects_page():
    return render_template('projects.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


# ==========================================
# REST API — /api/projects (backed by MySQL, not in-memory)
# ==========================================
@app.route('/api/projects', methods=['GET'])
def get_projects():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(projects), 200


@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM projects WHERE id = %s", (project_id,))
    project = cursor.fetchone()
    cursor.close()
    conn.close()
    if not project:
        return jsonify({"error": f"Project {project_id} not found"}), 404
    return jsonify(project), 200


@app.route('/api/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    if not validate_project_body(data):
        return jsonify({"error": "title and description are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO projects (title, description, tech_stack, github_url) VALUES (%s, %s, %s, %s)",
        (data["title"], data["description"], data.get("tech", ""), data.get("github_url", ""))
    )
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return jsonify({"id": new_id, **data}), 201


@app.route('/api/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.get_json()
    if not validate_project_body(data):
        return jsonify({"error": "title and description are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE projects SET title=%s, description=%s, tech_stack=%s, github_url=%s WHERE id=%s",
        (data["title"], data["description"], data.get("tech", ""), data.get("github_url", ""), project_id)
    )
    conn.commit()
    updated = cursor.rowcount
    cursor.close()
    conn.close()
    if not updated:
        return jsonify({"error": f"Project {project_id} not found"}), 404
    return jsonify({"id": project_id, **data}), 200


@app.route('/api/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE id=%s", (project_id,))
    conn.commit()
    deleted = cursor.rowcount
    cursor.close()
    conn.close()
    if not deleted:
        return jsonify({"error": f"Project {project_id} not found"}), 404
    return jsonify({"message": f"Project {project_id} deleted"}), 200


# ==========================================
# EXTRA — /api/skills and /api/certifications (read-only)
# ==========================================
@app.route('/api/skills', methods=['GET'])
def get_skills():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM skills")
    skills = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(skills), 200


@app.route('/api/certifications', methods=['GET'])
def get_certifications():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM certifications")
    certs = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(certs), 200


# ==========================================
# /api/messages — saves contact form submissions to MySQL
# ==========================================
@app.route('/api/messages', methods=['POST'])
def create_message():
    data = request.get_json()
    if not validate_message_body(data):
        return jsonify({"error": "name, email and message are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO messages (name, email, subject, message) VALUES (%s, %s, %s, %s)",
        (data["name"], data["email"], data.get("subject", ""), data["message"])
    )
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return jsonify({"id": new_id, "message": "Message saved"}), 201


@app.route('/api/health')
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
