import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo para seaborn
sns.set(style="whitegrid")

# 1. Crear un DataFrame
data = {
    'Marca': ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Audi', 'Mercedes', 'Hyundai', 'Volkswagen'],
    'Modelo': ['Corolla', 'Civic', 'Focus', 'Malibu', 'Altima', 'X5', 'A4', 'C-Class', 'Elantra', 'Golf'],
    'Año': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2021, 2022, 2023],
    'Precio': [20000, 22000, 21000, 23000, 24000, 55000, 40000, 45000, 23000, 26000],
    'Kilómetros': [50000, 30000, 15000, 40000, 20000, 25000, 10000, 8000, 5000, 2000]
}

df = pd.DataFrame(data)

# 2. Mostrar los primeros registros
print("Primeros registros del DataFrame:")
print(df.head())

# 3. Limpieza de Datos
# Verificar datos nulos
print("\nDatos nulos en el DataFrame:")
print(df.isnull().sum())

# Verificar duplicados
print("\nNúmero de duplicados en el DataFrame:")
print(df.duplicated().sum())

# 4. Análisis Descriptivo
print("\nEstadísticas descriptivas:")
print(df.describe())

# 5. Visualización de la Distribución de Precios
plt.figure(figsize=(10, 6))
sns.histplot(df['Precio'], bins=10, kde=True, color='blue')
plt.title('Distribución de Precios de Automóviles')
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.grid()
plt.show()

# 6. Gráfico de Caja para Precios por Marca
plt.figure(figsize=(12, 6))
sns.boxplot(x='Marca', y='Precio', data=df)
plt.title('Distribución de Precios por Marca')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# 7. Análisis de Correlación
correlation_matrix=df.select_dtypes(include=[np.number]).corr()
print("\nMatriz de correlación:")
print(correlation_matrix)

# 8. Visualización de la Matriz de Correlación
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Matriz de Correlación')
plt.show()

# 9. Análisis de Precio vs. Kilómetros
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Kilómetros', y='Precio', data=df, hue='Marca', style='Marca', size=100)
plt.title('Precio vs. Kilómetros')
plt.xlabel('Kilómetros')
plt.ylabel('Precio')
plt.grid()
plt.show()