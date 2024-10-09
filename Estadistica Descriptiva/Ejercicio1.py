import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#Conjunto de datos
data = [10, 20, 30, 40, 50, 60, 70, 80, 90]

#Convertir el dataframe
df = pd.DataFrame(data, columns=['Valores'])

#Calcular la medida de tendencia central
media = np.mean(data)
mediana = np.median(data)
moda = stats.mode(data)[0]

#Medida de dispesión
varianza = np.var(data)
desviacion = np.std(data)
rango = np.ptp(data)

#Percentiles
percentil25 = np.percentile(data, 25)
percentil50 = np.percentile(data, 50)
percentil75 = np.percentile(data, 75)
percentile100 = np.percentile(data, 100)    

#Imprimir los resultados
print('Meidas de tendencia central')
print('Media: ', media)
print('Mediana: ', mediana)
print('Moda: ', moda)

print('Medidas de dispersión')
print('Varianza: ', varianza)
print('Desviación estándar: ', desviacion)
print('Rango: ', rango)

print('Percentiles')
print('Percentil 25: ', percentil25)
print('Percentil 50: ', percentil50)
print('Percentil 75: ', percentil75)
print('Percentil 100: ', percentile100)

#Visualización de los datos
plt.figure(figsize=(10,5))
plt.hist(df['Valores'], bins=10, color='red', edgecolor='black')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Distribución de valores')
plt.show()

#Diagrama de caja
plt.figure(figsize=(10,5))
plt.boxplot(df['Valores'])
plt.ylabel('Valores')
plt.xlabel('Frecuencia')
plt.title('Diagrama de caja')
plt.show()

#Resumen estadistico
print('Resumen estadístico')
print(df.describe())