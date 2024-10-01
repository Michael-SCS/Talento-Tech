import numpy as np


#lista de números
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Calcular los percentiles
percentil_25 = np.percentile(data, 25)
percentil_50 = np.percentile(data, 50)
percentil_75 = np.percentile(data, 75)

print(f'El Percentil 25: {percentil_25}', f'\n El percentil de 50 es: {percentil_50} ', f'\n El percentil de 75 es: {percentil_75}')