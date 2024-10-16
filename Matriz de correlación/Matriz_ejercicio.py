#Ejercicios 4 Para los campistas:
#·       Importa las bibliotecas necesarias: NumPy, Matplotlib y Seaborn.
#·       Genera una matriz aleatoria de 10x10 utilizando NumPy.
#·       Usa Seaborn para crear un mapa de calor a partir de la matriz generada.
#·       Añade un título y ajusta la paleta de colores.
#·       Muestra el mapa de calor.

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#Crear datos aleatorios
data = np.random.rand(10,10)

#Crear el heatmap
sns.heatmap(data, cmap='coolwarm',annot=True)
plt.title('Matriz de correlación')
plt.show()