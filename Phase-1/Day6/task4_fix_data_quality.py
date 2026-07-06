"""
Day 6 - Task 4: Fix Data Quality Issues
File: dirty_students.csv -> cleaned_students.csv

Goal: Check for missing values / duplicate rows, fill missing values
sensibly, remove duplicates, and save the corrected file.
"""

import pandas as pd

df = pd.read_csv("dirty_students.csv")

print("Missing values per column (before cleaning):")
print(df.isnull().sum())

duplicate_count = df.duplicated().sum()
print(f"\nNumber of duplicate rows (before cleaning): {duplicate_count}")

# Fill missing values sensibly:
#   - Numeric columns (Age, Marks, Attendance, CGPA) -> column mean
#   - Text columns (Department, City)                -> 'Unknown' placeholder
numeric_cols_to_fill = ["Age", "Marks", "Attendance", "CGPA"]
for col in numeric_cols_to_fill:
    df[col] = df[col].fillna(df[col].mean())

text_cols_to_fill = ["Department", "City"]
for col in text_cols_to_fill:
    df[col] = df[col].fillna("Unknown")

# Remove duplicate rows
df = df.drop_duplicates()

# Clean up the index after dropping duplicates
df = df.reset_index(drop=True)

print("\nMissing values per column (after cleaning):")
print(df.isnull().sum())
print(f"Duplicate rows remaining: {df.duplicated().sum()}")
print(f"Final cleaned shape: {df.shape}")

df.to_csv("cleaned_students.csv", index=False)
print("\nSaved cleaned data to 'cleaned_students.csv'")
