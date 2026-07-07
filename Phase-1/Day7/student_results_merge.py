# ============================================================
# student_results_merge.py -- Task 3: Merging (Students.csv + Results.csv)
# ============================================================
import pandas as pd

# --- Create sample Students.csv (one row per student) ---
students = pd.DataFrame([
    (1, "Aarav", "I", "M", "Chennai"), (2, "Diya", "II", "F", "Chennai"),
    (3, "Kabir", "II", "M", "Coimbatore"), (4, "Ananya", "II", "F", "Chennai"),
    (5, "Vihaan", "III", "M", "Madurai"), (6, "Meera", "I", "F", "Chennai"),
    (7, "Reyansh", "III", "M", "Coimbatore"), (8, "Ishita", "III", "F", "Madurai"),
    (9, "Arjun", "II", "M", "Chennai"),
    # Note: Adm_No 10 exists here but has NO matching rows in Results.csv (transfer student, no results yet)
    (10, "Sneha", "I", "F", "Chennai"),
], columns=["Adm_No", "Name", "Class", "Gender", "City"])
students.to_csv("Students.csv", index=False)

# --- Create sample Results.csv (multiple rows per student -- one per Term+Subject) ---
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
    # Adm_No 11 has results but doesn't exist in Students.csv (data entry mismatch)
    (11, "Term1", "Maths", 50),
], columns=["Adm_No", "Term", "Subject", "Marks"])
results.to_csv("Results.csv", index=False)

# --- Step 1: Read both CSVs, inspect keys and duplicates ---
students = pd.read_csv("Students.csv")
results = pd.read_csv("Results.csv")
print(f"Students: {students.shape}, Results: {results.shape}")
print(f"Duplicate Adm_No in Results: {results['Adm_No'].duplicated().sum()}")  # each student has 2 terms, so duplicates are expected

# --- Step 2: Inner merge on Adm_No, save as inner_merge.csv ---
inner_merge = pd.merge(students, results, on="Adm_No", how="inner")
inner_merge.to_csv("inner_merge.csv", index=False)

# --- Step 3: Left merge, identify students without results ---
left_merge = pd.merge(students, results, on="Adm_No", how="left")
no_results = left_merge[left_merge["Term"].isna()]  # Term is NaN where no matching Results row existed
print("\nStudents with no results:")
print(no_results[["Adm_No", "Name"]].drop_duplicates())

# --- Step 4: Outer merge, fill NaNs (-1 or "No Result") ---
outer_merge = pd.merge(students, results, on="Adm_No", how="outer")
outer_merge["Marks"] = outer_merge["Marks"].fillna(-1)
outer_merge["Term"] = outer_merge["Term"].fillna("No Result")
outer_merge["Subject"] = outer_merge["Subject"].fillna("No Result")

# --- Step 5: Merge on multiple keys (Adm_No + Term) ---
# Build a small term-level summary, then merge it back onto Results using both keys
term_summary = results.groupby(["Adm_No", "Term"])["Marks"].mean().round(2).reset_index()
term_summary = term_summary.rename(columns={"Marks": "Term_Avg_Marks"})
multi_key_merge = pd.merge(results, term_summary, on=["Adm_No", "Term"], how="left")
print("\nMerged on multiple keys (Adm_No + Term):")
print(multi_key_merge.head())

# --- Answers ---
print("\n===== ANSWERS =====")
print(f"1. Row count difference (inner vs left): inner={len(inner_merge)}, "
      f"left={len(left_merge)}, difference={len(left_merge) - len(inner_merge)} "
      f"(the extra row(s) are Sneha, who has no matching Results rows).")
print("2. Renaming duplicate columns from a merge (e.g. if both tables share a non-key "
      "column like 'Class'):")
print("   merged = pd.merge(students, results, on='Adm_No', suffixes=('_student', '_result'))")
print("   merged = merged.rename(columns={'Class_student': 'Class'})")
print("3. Use LEFT merge when you want to keep every row from your main/reference table "
      "(e.g. every student) even if some have no match. Use OUTER merge when you want to "
      "keep every row from BOTH tables, including rows that only exist on one side "
      "(useful for spotting mismatched data on either side, like Adm_No 11 above).")
print(f"4. If Adm_No is duplicated in Results (which it is here, {results['Adm_No'].duplicated().sum()} "
      f"duplicates from multiple terms), an inner merge multiplies matching rows: each "
      f"Students row gets repeated once per matching Results row, so the merged table can "
      f"end up LARGER than either original table (Students has {len(students)} rows, "
      f"but inner_merge has {len(inner_merge)} rows).")
