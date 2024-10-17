import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Trabajar con los datos de Outliers
datos = [1, 2, 3, 4, 4, 5, 6, 7, 8, 100]
dataframe = pd.DataFrame(datos, columns=['Valor'])

#Crea el gráfico de Boxplot para identificar el Outlier
plt.boxplot(dataframe['Valor'])
plt.show()