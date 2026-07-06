"""
Day 6 - Task 5: Scholarship Shortlist Report
File: cleaned_students.csv (produced by Task 4)

Scenario: The college is selecting students for a Merit Scholarship.
Eligibility (all must be true): CGPA >= 8.5, Backlogs = 0, Attendance >= 90
"""

import pandas as pd

df = pd.read_csv("cleaned_students.csv")

# Apply eligibility conditions
eligible = df[
    (df["CGPA"] >= 8.5)
    & (df["Backlogs"] == 0)
    & (df["Attendance"] >= 90)
]

num_eligible = len(eligible)
most_common_dept = (
    eligible["Department"].value_counts().idxmax() if num_eligible > 0 else "N/A"
)
avg_marks_eligible = eligible["Marks"].mean() if num_eligible > 0 else float("nan")
avg_marks_class = df["Marks"].mean()

print("Eligible students (Name, Department, CGPA):")
print(eligible[["Name", "Department", "CGPA"]])

print("\nDepartment breakdown of eligible students:")
print(eligible["Department"].value_counts())

# --- Printed report (5-6 lines) ---
print("\n----- Merit Scholarship Shortlist Report -----")
print(f"1. Total eligible students: {num_eligible}")
print("2. Eligibility criteria: CGPA >= 8.5, Backlogs = 0, Attendance >= 90")
print(f"3. Department with the most eligible students: {most_common_dept}")
print(f"4. Average Marks of eligible students: {avg_marks_eligible:.2f}")
print(f"5. Average Marks of the whole class: {avg_marks_class:.2f}")
print(
    f"6. Eligible students outperform the class average by "
    f"{avg_marks_eligible - avg_marks_class:.2f} marks"
)
print("-----------------------------------------------")

eligible.to_csv("scholarship_shortlist.csv", index=False)
print("\nSaved eligible students to 'scholarship_shortlist.csv'")
