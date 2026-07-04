# ============================================================
# dict_practice.py -- Quick Practice Round 2: Dictionary Card
# ============================================================
student = {
    "name": "Abd",
    "subject": "Data Structures",
    "score": 82,
    "status": "Distinction",
}

print(f"Name: {student['name']}")
print(f"Subject: {student['subject']}")
print(f"Score: {student['score']}")
print(f"Status: {student['status']}")

student["score"] = 90  # update an existing value

print("\nAfter updating score:")
print(f"Name: {student['name']}")
print(f"Subject: {student['subject']}")
print(f"Score: {student['score']}")
print(f"Status: {student['status']}")
