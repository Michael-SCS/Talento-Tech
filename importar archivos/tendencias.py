import numpy as np
import matplotlib.pyplot as plt

#Datos de ejemplo -> Necesitamos numpy para calcular la regresión lineal

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([2,4,5,7,10,11,14,15,18,20])

#grafico de dispersión
plt.scatter(x,y,color='blue',label='Datos')

#Calcular los coeficientes de la linea de tendencia
a,b = np.polyfit(x,y,1)

#Graficar la linea de tendencia
plt.plot(x,a*x+b,color='red',label='Linea de tendencia')

plt.title('Gráfico de dispersión con línea de tendencia')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.legend()

plt.show()