#Ejercicio de dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Cargar el Dataset
dataset = pd.read_csv('datos.csv', delimiter=';')

#resumen de los datos
print('-------------Resumen estadistico-------------')
print(dataset.describe())

#Mostrar los primeros 5 registros
print('-------------Primeros 5 registros-------------')
print(dataset.head())

#Gráfico de distribución de una variable numérica
sns.histplot(dataset['Numero'])
plt.show()

#Gráfico de dispersión para ver la relación entre dos variables numéricas
sns.scatterplot(x='Peso', y='Altura', data=dataset)
plt.show()

#Grafico de caja para identificar
sns.boxplot(x='Categoria', y='Altura', data=dataset)
plt.show()

