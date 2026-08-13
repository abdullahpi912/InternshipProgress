import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))
from app import app, STUDENTS


def test_get_students_success():
    client = app.test_client()
    response = client.get("/api/students")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 5


def test_get_students_empty_state():
    client = app.test_client()
    response = client.get("/api/students?empty=true")
    assert response.status_code == 200
    assert response.get_json() == []


def test_post_success_updates_list():
    client = app.test_client()
    before = len(STUDENTS)
    response = client.post(
        "/api/students",
        json={
            "name": "Day 43 Student",
            "email": "day43@example.com",
            "course": "B.Tech AI & DS",
        },
    )
    assert response.status_code == 201
    payload = response.get_json()
    assert payload["success"] is True
    assert payload["student"]["name"] == "Day 43 Student"
    assert len(STUDENTS) == before + 1


def test_post_failure_invalid_data():
    client = app.test_client()
    response = client.post("/api/students", json={})
    assert response.status_code == 400
    payload = response.get_json()
    assert payload["success"] is False
    assert set(payload["missing_fields"]) == {"name", "email", "course"}


if __name__ == "__main__":
    test_get_students_success()
    test_get_students_empty_state()
    test_post_success_updates_list()
    test_post_failure_invalid_data()
    print("Day 43 API tests passed.")
