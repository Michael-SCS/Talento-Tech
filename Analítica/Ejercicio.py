import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#configurar el estilo de seaborn
sns.set(style='whitegrid')

#Crear el dataset
data ={
    'Marca':['Audi', 'BMW', 'Chevrolet', 'Ford', 'Honda', 'Hyundai', 'Kia', 'Mazda', 'Mercedes', 'Nissan', 'Renault', 'Toyota', 'Volkswagen'],
    'Modelo':['A3', 'Serie 3', 'Spark', 'Fiesta', 'Civic', 'Accent', 'Rio', '2', 'Clase A', 'Versa', 'Clio', 'Corolla', 'Golf'],
    'Año':[2018, 2018, 2021, 2019, 2020, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021],
    'Precio':[35000, 45000, 20000, 25000, 30000, 18000, 19000, 20000, 50000, 22000, 21000, 30000, 40000],
    'Kilometraje':[20000, 15000, 5000, 10000, 8000, 3000, 4000, 5000, 10000, 6000, 7000, 9000, 12000],
}

df = pd.DataFrame(data)

#Mostrar las primeras 5 filas del dataset
print('Primeras 5 filas del dataset: ')
print(df.head())

#Limpieza de datos - Verificar si hay valores nulos
print('\n Conteo de valores nulos: ')
print(df.isnull().sum())

#Verificar datos duplicados
print('\n Conteo de datos duplicados: ')
print(df.duplicated().sum())

#Analisis descriptivo
print('\n Descripción del dataset: ')
print(df.describe())

#Realizar la visualización de la distribución de precios
plt.figure(figsize=(10, 6))
sns.histplot(df['Precio'], bins=30, kde=True, color='blue')
plt.title('Distribución de Precios')
plt.xlabel('Precio')
plt.ylabel('Conteo')
plt.grid(axis='y')
plt.show()

#Analisis de correlación
correlacion = df.corr()
print('\n Matriz de correlación: ')
print(correlacion)

#Visualización de la matriz de correlación
plt.figure(figsize=(10, 8))
sns.heatmap(correlacion, annot=True, cmap='coolwarm', fmt='.2f', square=True) 
plt.title('Matriz de Correlación')
plt.show()


#Analisis de precios Vs kilometraje
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Kilometraje', y='Precio', data=df, hue='Marca', style='Marca')
plt.title('Precio Vs Kilometraje')
plt.xlabel('Kilometraje')
plt.ylabel('Precio')
plt.grid()
plt.show()