# ============================================================
# student_filtering.py -- Task 1: Filtering (Student_results.csv)
# ============================================================
import pandas as pd

# --- Create a sample Student_results.csv if one doesn't already exist ---
# (Adm_No, Name, Gender, Class, Subject, Marks) -- Percentage is added after
records = [
    (1, "Aarav", "M", "I", "Maths", 78), (1, "Aarav", "M", "I", "Science", 82), (1, "Aarav", "M", "I", "English", 75),
    (2, "Diya", "F", "II", "Maths", 91), (2, "Diya", "F", "II", "Science", 88), (2, "Diya", "F", "II", "English", 85),
    (3, "Kabir", "M", "II", "Maths", 32), (3, "Kabir", "M", "II", "Science", 55), (3, "Kabir", "M", "II", "English", 48),
    (4, "Ananya", "F", "II", "Maths", 66), (4, "Ananya", "F", "II", "Science", 70), (4, "Ananya", "F", "II", "English", 62),
    (5, "Vihaan", "M", "III", "Maths", 45), (5, "Vihaan", "M", "III", "Science", 39), (5, "Vihaan", "M", "III", "English", 50),
    (6, "Meera", "F", "I", "Maths", 95), (6, "Meera", "F", "I", "Science", 93), (6, "Meera", "F", "I", "English", 90),
    (7, "Reyansh", "M", "III", "Maths", 60), (7, "Reyansh", "M", "III", "Science", 58), (7, "Reyansh", "M", "III", "English", 65),
    (8, "Ishita", "F", "III", "Maths", 35), (8, "Ishita", "F", "III", "Science", 42), (8, "Ishita", "F", "III", "English", 40),
    (9, "Arjun", "M", "II", "Maths", 80), (9, "Arjun", "M", "II", "Science", 76), (9, "Arjun", "M", "II", "English", 72),
    (10, "Sneha", "F", "I", "Maths", 55), (10, "Sneha", "F", "I", "Science", 60), (10, "Sneha", "F", "I", "English", 58),
]
df = pd.DataFrame(records, columns=["Adm_No", "Name", "Gender", "Class", "Subject", "Marks"])
df["Percentage"] = df.groupby("Adm_No")["Marks"].transform("mean").round(2)  # overall % per student, repeated per subject row
df.to_csv("Student_results.csv", index=False)

# --- Step 1: Read CSV, show shape and first 5 rows ---
df = pd.read_csv("Student_results.csv")
print(f"Shape: {df.shape}")
print(df.head())

# --- Step 2: A Series of all Percentage values ---
percentage_series = df["Percentage"]
print("\nPercentage Series (first 5):")
print(percentage_series.head())

# --- Step 3: Filter Percentage >= 75, save to filtered_high.csv ---
filtered_high = df[df["Percentage"] >= 75]
filtered_high.to_csv("filtered_high.csv", index=False)

# --- Step 4: Filter Maths rows with Marks < 40, display count ---
low_maths = df[(df["Subject"] == "Maths") & (df["Marks"] < 40)]
print(f"\nMaths students below 40: {len(low_maths)}")
print(low_maths[["Adm_No", "Name", "Marks"]])

# --- Step 5: .query() for female Class II students with Percentage > 60 ---
female_class2 = df.query("Gender == 'F' and Class == 'II' and Percentage > 60")
print("\nFemale Class II, Percentage > 60:")
print(female_class2[["Adm_No", "Name", "Percentage"]].drop_duplicates())

# --- Answers ---
print("\n===== ANSWERS =====")
print(f"1. Students with Percentage >= 75: {filtered_high['Adm_No'].nunique()}")
print(f"2. Average Percentage of the high-% group: {filtered_high['Percentage'].mean():.2f}")
print(f"3. Student(s) in Maths below 40: {', '.join(low_maths['Name'].tolist())}")
print("4. .loc vs .iloc: .loc selects rows/columns by LABEL (e.g. df.loc[3, 'Marks'] "
      "or a boolean condition like df.loc[df['Marks'] < 40]). .iloc selects by INTEGER "
      "POSITION only (e.g. df.iloc[0] always means the first row, regardless of its "
      "label/index value). Use .loc for conditional filtering, .iloc for position-based access.")
