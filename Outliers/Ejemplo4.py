import numpy as np 
import pandas as pd

np.random.seed(42)
data = np.random.normal(0, 1, 100) #Datos simulados con media 0 y desviación estándar 1
data_with_outliers = np.append(data, [8,9,-7,-10])   #Agrega Outliers

df = pd.DataFrame(data_with_outliers, columns=['Valor'])

def calculate_s_score(df):
    mean = np.mean(df)
    std = np.std(df)
    s_score = (df - mean) / std
    return s_score

df['S_score'] = calculate_s_score(df['Valor'])
df['Outlier'] =df['S_score'].abs() > 3
print('Valores con Outliers:')
print(df)