from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle

data=load_diabetes()
X,y=data.data,data.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
pred=model.predict(X_test)
print("Actual vs Predicted:")
for a,p in zip(y_test[:10],pred[:10]):
    print(f"{a:.2f} -> {p:.2f}")
print("MSE:",mean_squared_error(y_test,pred))
with open("diabetes_model.pkl","wb") as f:
    pickle.dump(model,f)
print("Saved diabetes_model.pkl")
