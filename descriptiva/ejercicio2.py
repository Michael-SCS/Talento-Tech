import pandas as pd
import numpy as np

#Crear nuevo DataFrame
datos = {'nombre': ['Juan', 'Ana', 'Pedro', 'Maria', 'Erica', 'Laura'],
        'edad': [23, 25, 22, 19, 23, 78],}

df = pd.DataFrame(datos)

#Calcular los percentiles de la edad

percentil_10 = np.percentile(df['edad'], 10)
percentil_50 = np.percentile(df['edad'], 50)
percentil_90 = np.percentile(df['edad'], 90)

print(f'El Percentil 10: {percentil_10}', f'\n El percentil de 50 es: {percentil_50} ', f'\n El percentil de 90 es: {percentil_90}')