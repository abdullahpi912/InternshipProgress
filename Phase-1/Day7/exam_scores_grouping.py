# ============================================================
# exam_scores_grouping.py -- Task 2: Grouping & Aggregation (Exam_scores.csv)
# ============================================================
import pandas as pd
import numpy as np

# --- Create a sample Exam_scores.csv with a few missing Marks ---
records = [
    (1, "Aarav", "I", "Maths", 78), (1, "Aarav", "I", "Science", np.nan), (1, "Aarav", "I", "English", 75),
    (2, "Diya", "II", "Maths", 91), (2, "Diya", "II", "Science", 88), (2, "Diya", "II", "English", 85),
    (3, "Kabir", "II", "Maths", np.nan), (3, "Kabir", "II", "Science", 55), (3, "Kabir", "II", "English", 48),
    (4, "Ananya", "II", "Maths", 66), (4, "Ananya", "II", "Science", 70), (4, "Ananya", "II", "English", 62),
    (5, "Vihaan", "III", "Maths", 45), (5, "Vihaan", "III", "Science", 39), (5, "Vihaan", "III", "English", np.nan),
    (6, "Meera", "I", "Maths", 95), (6, "Meera", "I", "Science", 93), (6, "Meera", "I", "English", 90),
    (7, "Reyansh", "III", "Maths", 60), (7, "Reyansh", "III", "Science", 58), (7, "Reyansh", "III", "English", 65),
    (8, "Ishita", "III", "Maths", 35), (8, "Ishita", "III", "Science", np.nan), (8, "Ishita", "III", "English", 40),
    (9, "Arjun", "II", "Maths", 80), (9, "Arjun", "II", "Science", 76), (9, "Arjun", "II", "English", 72),
    (10, "Sneha", "I", "Maths", 55), (10, "Sneha", "I", "Science", 60), (10, "Sneha", "I", "English", 58),
    (11, "Kiaan", "I", "Maths", 88), (11, "Kiaan", "I", "Science", 84), (11, "Kiaan", "I", "English", 79),
    (12, "Riya", "III", "Maths", 72), (12, "Riya", "III", "Science", 69), (12, "Riya", "III", "English", 74),
]
df = pd.DataFrame(records, columns=["Adm_No", "Name", "Class", "Subject", "Marks"])
df.to_csv("Exam_scores.csv", index=False)

# --- Step 1: Read CSV, display info (dtypes, missing counts) ---
df = pd.read_csv("Exam_scores.csv")
print(df.info())
print("\nMissing values per column:")
print(df.isna().sum())

# --- Step 2: Fill missing Marks with subject-wise mean ---
missing_before = df["Marks"].isna().sum()
subject_means = df.groupby("Subject")["Marks"].transform("mean").round(2)  # each row gets its own subject's mean
df["Marks"] = df["Marks"].fillna(subject_means)

# --- Step 3: Group by Subject -- count, mean, min, max Marks ---
subject_stats = df.groupby("Subject")["Marks"].agg(["count", "mean", "min", "max"]).round(2)
print("\nSubject-wise stats:")
print(subject_stats)

# --- Step 4: Group by Class, compute average Marks ---
class_avg = df.groupby("Class")["Marks"].mean().round(2)
print("\nClass-wise average Marks:")
print(class_avg)

# --- Step 5: Top 3 students by total marks (groupby + sum) ---
top3 = df.groupby(["Adm_No", "Name"])["Marks"].sum().sort_values(ascending=False).head(3)
top3 = top3.reset_index()  # turns the groupby result back into normal columns instead of an index
print("\nTop 3 students by total marks:")
print(top3)

# --- Answers ---
print("\n===== ANSWERS =====")
print(f"1. Missing Marks filled: {missing_before}, each filled with its own subject's mean "
      f"(Maths={df[df['Subject']=='Maths']['Marks'].mean():.2f} used as reference before fill, "
      f"same logic applied per subject).")
print(f"2. Subject with highest mean Marks: {subject_stats['mean'].idxmax()} "
      f"({subject_stats['mean'].max():.2f})")
print("3. Flattening a multi-aggregation result:")
print("   agg_result = df.groupby('Subject')['Marks'].agg(['mean', 'sum'])")
print("   agg_result.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in agg_result.columns]")
print("   (or simply: agg_result.columns = ['Marks_mean', 'Marks_sum'])")
print("4. reset_index() is necessary after groupby because groupby() turns the grouping "
      "column(s) into the DataFrame's index instead of a normal column -- reset_index() "
      "moves them back into regular columns so the result can be filtered, merged, or "
      "saved to CSV like a normal DataFrame.")
