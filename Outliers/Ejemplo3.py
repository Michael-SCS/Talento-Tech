import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Crear un dataframe con datos simulados
np.random.seed(42)
data = np.random.normal(50, 10, 100) #Datos simulados con media 50 y desviación estándar 10
data = np.append(data, [150,160,170]) #Agrega un Outlier

df = pd.DataFrame(data, columns=['Valor'])

#Calcular el rango intercuartilico
Q1 = df['Valor'].quantile(0.25)
Q3 = df['Valor'].quantile(0.75)
IQR = Q3 - Q1 #para detectar los Outliers

#Definir los límites para identificar los Outliers
lower_bound = Q1 - 1.5 * IQR 
upper_bound = Q3 + 1.5 * IQR

#Reemplazar los Outliers por el valor de la mediana

median = df['Valor'].median()

df['Valor_corregido'] = np.where((df['Valor'] < lower_bound) | (df['Valor'] > upper_bound), median, df['Valor'])
print('Valores después de corregir los Outliers:')
print(df.head())

#Crear boxplot para visualizar los datos
plt.figure(figsize=(10,6))
plt.boxplot(df['Valor_corregido'])
plt.title('Boxplot de los datos')
plt.show()