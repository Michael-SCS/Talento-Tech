import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Crear datos aleatorios
data = np.random.rand(6, 8)

#Heatmap
sns.heatmap(data, annot=True, fmt=".2f", cmap='coolwarm')

#Etiquetas de los ejes
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()