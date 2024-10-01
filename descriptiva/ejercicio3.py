import numpy as np
import pandas as pd

#Generar 100 numeros aleatorios entre 0 y 1000
data = np.random.randint(0, 1000, 100)

#Calcular los percentiles
percentil_10 = np.percentile(data, 10)
percentil_25 = np.percentile(data, 25)
percentile_50 = np.percentile(data, 50)
percentil_75 = np.percentile(data, 75)
percentil_90 = np.percentile(data, 90)

#redondear los percentiles
percentil_10 = round(percentil_10, 0)
percentil_25 = round(percentil_25, 0)
percentile_50 = round(percentile_50, 0)
percentil_75 = round(percentil_75, 0)
percentil_90 = round(percentil_90, 0)

print(f'El Percentil 10: {percentil_10}', f'\n El percentil de 25 es: {percentil_25} ', f'\n El percentil de 50 es: {percentile_50}', f'\n El percentil de 75 es: {percentil_75}', f'\n El percentil de 90 es: {percentil_90}')

