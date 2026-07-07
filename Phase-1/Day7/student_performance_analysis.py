# ============================================================
# student_performance_analysis.py -- Task 4: Mini Project
# Student Performance Analysis using Students, Results & Attendance
# ============================================================
import pandas as pd
import numpy as np

# --- Create the 3 sample CSVs ---
students = pd.DataFrame([
    (1, "Aarav", "I", "M", "Chennai"), (2, "Diya", "II", "F", "Chennai"),
    (3, "Kabir", "II", "M", "Coimbatore"), (4, "Ananya", "II", "F", "Chennai"),
    (5, "Vihaan", "III", "M", "Madurai"), (6, "Meera", "I", "F", "Chennai"),
    (7, "Reyansh", "III", "M", "Coimbatore"), (8, "Ishita", "III", "F", "Madurai"),
    (9, "Arjun", "II", "M", "Chennai"), (10, "Sneha", "I", "F", "Chennai"),
], columns=["Adm_No", "Name", "Class", "Gender", "City"])
students.to_csv("Students.csv", index=False)

results = pd.DataFrame([
    (1, "Term1", "Maths", 78), (1, "Term2", "Maths", 82),
    (2, "Term1", "Maths", 91), (2, "Term2", "Maths", 88),
    (3, "Term1", "Maths", 32), (3, "Term2", "Maths", 55),
    (4, "Term1", "Maths", 66), (4, "Term2", "Maths", 70),
    (5, "Term1", "Maths", 45), (5, "Term2", "Maths", 39),
    (6, "Term1", "Maths", 95), (6, "Term2", "Maths", 93),
    (7, "Term1", "Maths", 60), (7, "Term2", "Maths", 58),
    (8, "Term1", "Maths", 35), (8, "Term2", "Maths", 42),
    (9, "Term1", "Maths", 80), (9, "Term2", "Maths", 76),
    (10, "Term1", "Maths", 38), (10, "Term2", "Maths", 34),
], columns=["Adm_No", "Term", "Subject", "Marks"])
results.to_csv("Results.csv", index=False)

# Attendance -- Adm_No 5 (Vihaan) is deliberately missing from this file to show the bias later
attendance = pd.DataFrame([
    (1, "Term1", 85, 90), (1, "Term2", 88, 90),
    (2, "Term1", 89, 90), (2, "Term2", 90, 90),
    (3, "Term1", 60, 90), (3, "Term2", 65, 90),
    (4, "Term1", 80, 90), (4, "Term2", 82, 90),
    (6, "Term1", 88, 90), (6, "Term2", 87, 90),
    (7, "Term1", 70, 90), (7, "Term2", 68, 90),
    (8, "Term1", 55, 90), (8, "Term2", 58, 90),
    (9, "Term1", 84, 90), (9, "Term2", 86, 90),
    (10, "Term1", 50, 90), (10, "Term2", 52, 90),
], columns=["Adm_No", "Term", "Days_Present", "Days_Total"])
attendance.to_csv("Attendance.csv", index=False)

# --- Step 1: Read the 3 CSV files ---
students = pd.read_csv("Students.csv")
results = pd.read_csv("Results.csv")
attendance = pd.read_csv("Attendance.csv")

# --- Step 2: Filter Results to a specific Class / Term (demo: Class II, Term1) ---
results_with_class = pd.merge(results, students[["Adm_No", "Class"]], on="Adm_No", how="left")
class2_term1 = results_with_class[(results_with_class["Class"] == "II") & (results_with_class["Term"] == "Term1")]
print("Results for Class II, Term1:")
print(class2_term1[["Adm_No", "Term", "Subject", "Marks"]])

# --- Step 3: Group by Adm_No -- total & avg Marks per student ---
marks_summary = results.groupby("Adm_No")["Marks"].agg(Total_Marks="sum", Avg_Marks="mean")
marks_summary["Avg_Marks"] = marks_summary["Avg_Marks"].round(2)
marks_summary = marks_summary.reset_index()

# --- Step 4: Group Attendance by Adm_No, compute attendance % ---
att_summary = attendance.groupby("Adm_No")[["Days_Present", "Days_Total"]].sum()
att_summary["Attendance_Rate"] = (att_summary["Days_Present"] / att_summary["Days_Total"] * 100).round(2)
att_summary = att_summary.reset_index()[["Adm_No", "Attendance_Rate"]]

# --- Step 5: Merge scores + attendance + students into final_report.csv ---
final_report = students.merge(marks_summary, on="Adm_No", how="left")
final_report = final_report.merge(att_summary, on="Adm_No", how="left")
final_report["Avg_Marks"] = final_report["Avg_Marks"].round(2)
final_report.to_csv("final_report.csv", index=False)
print("\nFinal report:")
print(final_report)

# --- Step 6: Filter attendance < 75% AND avg Marks < 40, save at_risk.csv ---
at_risk = final_report[(final_report["Attendance_Rate"] < 75) & (final_report["Avg_Marks"] < 40)]
at_risk.to_csv("at_risk.csv", index=False)
print("\nAt-risk students:")
print(at_risk[["Adm_No", "Name", "Avg_Marks", "Attendance_Rate"]])

# --- Answers ---
print("\n===== ANSWERS =====")
top5 = final_report.sort_values("Avg_Marks", ascending=False).head(5)
print("1. Top 5 students by avg Marks and their attendance rates:")
print(top5[["Name", "Avg_Marks", "Attendance_Rate"]])
print(f"2. Students flagged as at-risk: {len(at_risk)}")
print("3. Missing Attendance bias: Vihaan (Adm_No 5) has no rows in Attendance.csv, so "
      "his Attendance_Rate becomes NaN after the left merge. A comparison like "
      "'NaN < 75' always evaluates to False in pandas, so a genuinely at-risk student "
      "with missing attendance data would be silently EXCLUDED from at_risk.csv instead "
      "of being flagged -- missing data hides risk rather than showing it as zero.")
print("4. final_report.csv was exported with Avg_Marks (used here as the Percentage-style "
      "metric) rounded to 2 decimal places via .round(2) before saving.")
print("5. Fixing an int vs str Adm_No type mismatch before merging:")
print("   students['Adm_No'] = students['Adm_No'].astype(str)")
print("   results['Adm_No'] = results['Adm_No'].astype(str)")
print("   (cast both sides to the SAME type before merging -- pandas treats "
      "1 (int) and '1' (str) as non-matching keys, silently dropping rows on an inner merge.)")
