#Importar librerias y datos

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #Esta librería es para hacer gráficos más bonitos, avanzados y con más opciones

#Cargar datos
data = {
    'Año':[2018,2018,2018,2019,2019,2019,2020,2020,2020],
    'Fuente_energia':['Hidroeléctrica','Solar','Eólica','Hidroeléctrica','Solar','Eólica','Hidroeléctrica','Solar','Eólica'],
    'Generacion_mwh':[500,300,1000,600,350,1100,700,400,1200],
    'consumo_mwh':[1500,1500,1500,1600,1600,1600,1700,1700,1700]
}

df = pd.DataFrame(data)

#explorar el conjunto de datos
print(df.head()) #Muestra las primeras 5 filas del conjunto de datos

print(df.describe())#Genera una descripción estática de las columnas numéricas del conjunto de datos

print(df.info()) #Muestra información resumida del conjunto de datos

#Análisis de tendencias de Generación de energía
generacion_tendencia = df.groupby('Año')['Generacion_mwh'].sum().reset_index() #Agrupar por año y sumar la generación de energía

plt.figure(figsize=(10,6)) #Tamaño de la figura

sns.lineplot(x='Año',y='Generacion_mwh',data=generacion_tendencia,
marker='o')#Gráfico de línea

plt.title('Tendencia de generación de energía por año en Colombia') #Título del gráfico

plt.xlabel('Año') #Etiqueta eje x
plt.ylabel('Generación de energía (MWh)') #Etiqueta eje y

plt.grid(True) #Agregar cuadrícula
plt.show() #Mostrar gráfico


#Paso 4: Comparar la generación de energía por fuente
generacion_por_fuente = df.groupby['año','Fuente_energia']['Generacion_mwh'].sum().unstack() #Agrupar por año y fuente de energía

generacion_por_fuente.plot(kind='bar',stacked=True,figsize=(12,8)) #Gráfico de barras apiladas
plt.title('Generación de energía por fuente en Colombia') #Título del gráfico
plt.xlabel('Año') #Etiqueta eje x
plt.ylabel('Generación de energía (MWh)') #Etiqueta eje y
plt.grid(True) #Agregar cuadrícula
plt.show() #Mostrar gráfico

#paso 5: Visualización de resultados
sns.heatmap(df.pivot(index='año',columns='Fuente_energia',values='Generacion_mwh'),annot=True,cmap='YlGnBu') #Mapa de calor
plt.grid(True) #Agregar cuadrícula
plt.show() #Mostrar gráfico