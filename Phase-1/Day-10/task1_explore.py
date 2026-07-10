from sklearn.datasets import load_iris
import pandas as pd

iris=load_iris(as_frame=True)
df=iris.frame
df['species']=df['target'].map(dict(enumerate(iris.target_names)))

print(df.head())
print("\nFlowers in each species:")
print(df['species'].value_counts())

features=iris.feature_names
print("\nAverage features by species:")
print(df.groupby('species')[features].mean())

avg=df['petal length (cm)'].mean()
print("\nVirginica with petal length > dataset average:")
print(df[(df['species']=='virginica') & (df['petal length (cm)']>avg)])

print("\nSpecies with highest average sepal length:")
print(df.groupby('species')['sepal length (cm)'].mean().idxmax())

df['Sepal Area']=df['sepal length (cm)']*df['sepal width (cm)']
df.to_csv('filtered_iris.csv',index=False)
print("\nSaved filtered_iris.csv")
