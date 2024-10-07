import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Cargar el Dataset Titanic directamente desde seaborn
df = sns.load_dataset('titanic')

#mostrar las primeras filas
print('-------------Primeros 5 registros-------------')
print(df.head())

#información del Dataframe
print('-------------Información del Dataframe-------------')
print(df.info())

#Descripción estadistica
print('-------------Resumen estadistico-------------')
print(df.describe().round(2))

#Verificar si hay valores nulos
print('-------------Valores nulos-------------')
print(df.isnull().sum())

#Elimine filas con valores nulos
df_cleaned = df.dropna()

#Rellenar valores nulos en columnas
df['age'].fillna(df['age'].mean(),inplace=True)

#Verificar valores nulos después de la limpieza
print('-------------Valores nulos despues de la limpieza-------------')
print(df.isnull().sum())
plt.figure(figsize=(8,6))
sns.histplot(df['age'], kde=True,bins=30)
plt.title('Distribución de la edad')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()


plt.figure(figsize=(8,6))
sns.scatterplot(x='age', y='fare', data=df)
plt.title('Relación entre la edad y la tarifa')
plt.show()


sns.countplot(x='sex', hue='survived', data=df)
plt.title('Sobrevivientes por género')
plt.xlabel('Género')
plt.ylabel('Total')
plt.show()