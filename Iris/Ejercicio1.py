import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Cargar el conjunto de datos de Iris
iris = sns.load_dataset('iris')

#Mostrar las primeras filas del Dataset

print('Primeras 5 filas de conjunto de dataset de Iris')
print(iris.head())

#Descripción estadistica básica
print('\n Descripción estadistica básica')
print(iris.describe())

#Verificar valores nulos
print('\n Valores nulos: ')
print(iris.isnull().sum())

#Visualización de la distribución de las variables
sns.pairplot(iris, hue='species', diag_kind='kde') 
plt.show()

#Mapa de calor de la corellación de las varibales
plt.figure(figsize=(7,4))
sns.heatmap(iris.corr(), annot=True, cmap='cubehelix_r',fmt='.2f')
plt.title('Mapa de calor de la correlación')
plt.show()