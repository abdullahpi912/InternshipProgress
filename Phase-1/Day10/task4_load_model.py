import pickle
from sklearn.datasets import load_diabetes

with open("diabetes_model.pkl","rb") as f:
    model=pickle.load(f)

new_patient=load_diabetes().data[:1]
prediction=model.predict(new_patient)
print("Predicted disease progression:",prediction[0])
print("Prediction completed without retraining.")
