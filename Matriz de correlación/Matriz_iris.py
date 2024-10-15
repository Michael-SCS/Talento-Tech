import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

#Mostrar las primeras filas del Dataframe iris
print('Dataset IRIS')
print(df.head())

#Calcular la matriz de correlación
correlation_matrix = df.corr()
print('\nMatriz de correlación')
print(correlation_matrix)

#mapa de calor
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()
