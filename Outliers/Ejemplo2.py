import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Crear un DataFrame con datos simulados
np.random.seed(42)
data = np.random.normal(50, 10, 100) #Datos simulados con media 50 y desviación estándar 10
data = np.append(data, [150,160,170]) #Agrega un Outlier

df = pd.DataFrame(data, columns=['Valor'])

#Crear un boxplot para visualizar los datos
plt.figure(figsize=(10,6))
plt.boxplot(df['Valor'])
plt.title('Boxplot de los datos')
plt.show()