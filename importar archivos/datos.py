#importar libreria
import matplotlib.pyplot as plt
import numpy as np

#tener datos
datos = np.random.randn(500)

#crear el gráfico
plt.hist(datos, bins=30, alpha=0.7)

#Añadir titulos
plt.title("Histograma")
plt.xlabel("valor")
plt.ylabel("Frecuencia")

#Mostrar el grafico
plt.show()