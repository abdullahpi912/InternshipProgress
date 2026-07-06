"""
File: students.csv

Before doing anything else, understand what's inside the dataset.
"""

import pandas as pd

df = pd.read_csv("students.csv")

print(f"Number of students (rows): {df.shape[0]}")
print(f"Number of columns:         {df.shape[1]}")

print("\nColumn names:")
print(list(df.columns))

print("\nData type of each column:")
print(df.dtypes)

print("\nFirst 5 records:")
print(df.head())

print("\nLast 5 records:")
print(df.tail())
