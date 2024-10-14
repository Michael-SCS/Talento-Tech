import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'edad' : [23,45,31,50,19,50],
    'ingresos_mensuales' : [2500, 4000, 3200, 2900, 5000, 6000],
    'gastos_mensuales' : [1200, 2500, 1500, 2100, 2200, 1000],
    'ahorros_mensuales': [10000, 5000, 3000, 4000, 20000, 50000]
}

df = pd.DataFrame(data)

print('Este es el Dataframe de columnas numéricas:')
print(df)

correlation_matrix = df.corr()
print('Esta es la matriz de correlación:')
print(correlation_matrix)