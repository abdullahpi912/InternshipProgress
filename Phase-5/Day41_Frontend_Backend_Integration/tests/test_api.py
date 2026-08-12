import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))
from app import app

def test_get_students():
    client = app.test_client()
    response = client.get("/api/students")

    assert response.status_code == 200
    data = response.get_json()

    assert isinstance(data, list)
    assert len(data) >= 5
    assert {"id", "name", "email", "course"} <= set(data[0])

if __name__ == "__main__":
    test_get_students()
    print("Day 41 API test passed.")
