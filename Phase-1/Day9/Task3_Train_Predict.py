# ============================================================
# Task3_Train_Predict.py -- Train, Predict & Compare
# ============================================================
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)  # predictions on the unseen testing dataset

print("Actual values:   ", y_test.tolist())
print("Predicted values:", y_pred.tolist())

# Compare both outputs side by side, flagging any mismatch
print("\nComparison:")
for i, (actual, predicted) in enumerate(zip(y_test, y_pred)):
    match = "correct" if actual == predicted else "WRONG"
    print(f"  Sample {i+1}: actual={iris.target_names[actual]:<10} "
          f"predicted={iris.target_names[predicted]:<10} ({match})")
