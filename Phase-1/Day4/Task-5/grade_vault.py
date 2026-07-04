# ============================================================
# grade_vault.py -- Task 5: GradeVault, a student score manager
# grade_utils.py must be in the same folder as this file.
# ============================================================
from grade_utils import PASS_CUTOFFS

LOG_FILE = "grades_log.txt"

# List of dictionaries -- each student is one record, the class is the whole list
students = [
    {"name": "Abd", "subject": "Python", "score": 88, "status": ""},
    {"name": "Priya", "subject": "Python", "score": 42, "status": ""},
    {"name": "Rahul", "subject": "Data Structures", "score": 91, "status": ""},
    {"name": "Sneha", "subject": "Data Structures", "score": 60, "status": ""},
    {"name": "Arjun", "subject": "Python", "score": 30, "status": ""},
]

def set_status(score):
    # Compares score against the locked PASS_CUTOFFS tuple to decide status
    if score < PASS_CUTOFFS[0]:
        return "Fail"
    elif score < PASS_CUTOFFS[2]:
        return "Pass"
    else:
        return "Distinction"

def log_action(text):
    # Append a line to the grades log so history survives after the program closes
    with open(LOG_FILE, "a") as f:
        f.write(text + "\n")

def add_student(name, subject, score):
    status = set_status(score)
    students.append({"name": name, "subject": subject, "score": score, "status": status})
    log_action(f"ADDED | {name} | {subject} | score={score} | status={status}")

def list_students():
    for s in students:
        print(f"{s['name']:<10} {s['subject']:<16} score={s['score']:<4} status={s['status']}")

def unique_subjects():
    return {s["subject"] for s in students}  # a set -- automatically drops duplicate subjects

def class_average(subject):
    # Filter the class down to just this subject, then average their scores
    scores = [s["score"] for s in students if s["subject"] == subject]
    if not scores:
        return 0
    return sum(scores) / len(scores)

def top_scorer():
    # Walk the whole class, keeping track of whoever has the highest score so far
    best = students[0]
    for s in students[1:]:
        if s["score"] > best["score"]:
            best = s
    return best

def search_student(name):
    for s in students:
        if s["name"].lower() == name.lower():
            return s
    return "Not found"

def top_scorers():
    # Bonus: list comprehension -- every Distinction student's name, in one line
    return [s["name"] for s in students if s["status"] == "Distinction"]

# --- Set initial statuses for the starting students ---
for s in students:
    s["status"] = set_status(s["score"])

# --- Demo run ---
add_student("Kavya", "Data Structures", 78)

print("All students:")
list_students()

print(f"\nUnique subjects: {unique_subjects()}")
print(f"Python class average: {class_average('Python'):.2f}")
print(f"Data Structures class average: {class_average('Data Structures'):.2f}")

top = top_scorer()
print(f"\nTop scorer: {top['name']} ({top['score']} in {top['subject']})")

print(f"\nSearch 'Rahul': {search_student('Rahul')}")
print(f"Search 'Zoya': {search_student('Zoya')}")

print(f"\nDistinction students: {top_scorers()}")
