"""
Day 6 - Task 3: Filter Based on Conditions
File: students.csv

Goal: Produce shortlists of students based on specific conditions.
"""

import pandas as pd

df = pd.read_csv("students.csv")

# 1. Students with Marks above 80 and zero Backlogs
high_marks_no_backlog = df[(df["Marks"] > 80) & (df["Backlogs"] == 0)]
print("Students with Marks > 80 and 0 Backlogs:")
print(high_marks_no_backlog[["Name", "Marks", "Backlogs"]])

# 2. Students from the CSE department who are in 3rd Year
cse_3rd_year = df[(df["Department"] == "CSE") & (df["Year"] == "3rd Year")]
print("\nCSE students in 3rd Year:")
print(cse_3rd_year[["Name", "Department", "Year"]])

# 3. Students whose CGPA is above the class average
avg_cgpa = df["CGPA"].mean()
above_avg_cgpa = df[df["CGPA"] > avg_cgpa]
print(f"\nStudents with CGPA above the class average ({avg_cgpa:.2f}):")
print(above_avg_cgpa[["Name", "CGPA"]])
