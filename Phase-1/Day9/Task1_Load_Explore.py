# ============================================================
# Task1_Load_Explore.py -- Load and Explore the Iris Dataset
# ============================================================
import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset and build a DataFrame with readable species names
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = [iris.target_names[i] for i in iris.target]  # map 0/1/2 to actual flower names

print(df.to_string())

# Filter rows where Sepal Length > 5.0
long_sepals = df[df["sepal length (cm)"] > 5.0]
print(f"\nRows with Sepal Length > 5.0: {len(long_sepals)}")

# Display only Sepal Length and Petal Length
print("\nSepal Length & Petal Length only:")
print(df[["sepal length (cm)", "petal length (cm)"]].head())

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nSummary statistics:")
print(df.describe())

print("\nData types:")
print(df.dtypes)

df.to_csv("iris_dataset.csv", index=False)
print("\nSaved to iris_dataset.csv")
