"""
Day 6 - Task 2: Answer Basic Questions
File: students.csv

Goal: Answer quick questions a professor might ask about the class.
"""

import pandas as pd

df = pd.read_csv("students.csv")

# Who scored the highest Marks?
top_marks_student = df.loc[df["Marks"].idxmax()]
print(f"Highest Marks: {top_marks_student['Name']} scored {top_marks_student['Marks']}")

# What is the average CGPA of all students?
avg_cgpa = df["CGPA"].mean()
print(f"Average CGPA of all students: {avg_cgpa:.2f}")

# Which student has the best Attendance?
best_attendance_student = df.loc[df["Attendance"].idxmax()]
print(
    f"Best Attendance: {best_attendance_student['Name']} "
    f"with {best_attendance_student['Attendance']}%"
)

# What is the average Attendance of the whole class?
avg_attendance = df["Attendance"].mean()
print(f"Average Attendance of the class: {avg_attendance:.2f}%")
