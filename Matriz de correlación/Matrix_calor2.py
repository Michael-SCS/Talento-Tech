import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargamos el dataset
data = np.random.rand(100, 5)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])

#Calcular la matriz de correlación
correlation_matrix = df.corr()  
#calcular el mapa de calor
sns.heatmap(correlation_matrix, annot=True, cmap='YlGnBu', linewidths=0.5)
plt.show()