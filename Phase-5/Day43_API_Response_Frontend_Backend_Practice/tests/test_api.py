import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))
from app import app, STUDENTS


def test_get_students():
    client = app.test_client()
    response = client.get("/api/students")

    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 5
    assert {"id", "name", "email", "course"} <= set(data[0])


def test_post_student():
    client = app.test_client()
    before_count = len(STUDENTS)

    response = client.post(
        "/api/students",
        json={
            "name": "Test Student",
            "email": "test.student@example.com",
            "course": "B.Tech AI & DS",
        },
    )

    assert response.status_code == 201
    data = response.get_json()
    assert data["success"] is True
    assert data["student"]["name"] == "Test Student"
    assert data["student"]["email"] == "test.student@example.com"
    assert data["student"]["course"] == "B.Tech AI & DS"
    assert len(STUDENTS) == before_count + 1


def test_post_student_validation():
    client = app.test_client()
    response = client.post("/api/students", json={})

    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert set(data["missing_fields"]) == {"name", "email", "course"}


if __name__ == "__main__":
    test_get_students()
    test_post_student()
    test_post_student_validation()
    print("Day 42 API tests passed.")
