import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#Crear datos aleatorios
data = np.random.rand(10,12)
#El 10 indica el número de filas y el 12 el número de columnas

#Crear el heatmap
sns.heatmap(data, cmap='coolwarm',annot=True)
plt.show()