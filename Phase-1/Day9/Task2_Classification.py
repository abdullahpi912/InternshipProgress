# ============================================================
# Task2_Classification.py -- Train a Decision Tree Classifier
# ============================================================
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X, y = iris.data, iris.target

# random_state fixes the shuffle so the split is identical every run
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict the class for 2 new sample inputs (sepal length, sepal width, petal length, petal width)
sample_inputs = [
    [5.1, 3.5, 1.4, 0.2],   # looks like a setosa
    [6.7, 3.1, 4.7, 1.5],   # looks like a versicolor
]
predictions = model.predict(sample_inputs)
predicted_names = [iris.target_names[p] for p in predictions]  # map 0/1/2 back to the flower name

for sample, name in zip(sample_inputs, predicted_names):
    print(f"Input {sample} -> Predicted: {name}")
