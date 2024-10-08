#Importar bibliotecas y el dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('venta_casas.csv', delimiter=';')
df = pd.DataFrame(data)
print(df.head())
#Obtener información básica del dataset con las funciones: info(), describe(), columnas()
print('________________________INFO________________________')
print(df.info())
print('________________________DESCRIBE________________________')
print(df.describe())
print('________________________COLUMNAS________________________')
print(df.columns)

#Identificar valores faltantes en la data
print('________________________VALORES FALTANTES________________________')
print(df.isnull().sum())

#Opcional: Elimnar filsa con valores faltantes
df = df.dropna()

#Visualización de la distribución de datos
print('________________________DISTRIBUCIÓN DE DATOS________________________')
plt.figure(figsize=(10,5))
plt.hist(df['Precio'],bins=10) #El bin es la cantidad de barras que se quieren mostrar
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.title('Distribución de precios')
plt.show()


#Establecer una relación entre variables categóricas y el precio
print('________________________RELACIÓN ENTRE VARIABLES CATEGÓRICAS Y PRECIO________________________')
plt.figure(figsize=(10,5))
plt.bar(df['Localización'], df['Precio'])
plt.xlabel('Tipo')
plt.ylabel('Precio')
plt.title('Relación entre tipo de casa y precio')
plt.show()
