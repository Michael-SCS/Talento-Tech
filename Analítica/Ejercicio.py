import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#configurar el estilo de seaborn
sns.set(style='whitegrid')

#Crear el dataset
data ={
    'Marca':['Audi', 'BMW', 'Chevrolet', 'Ford', 'Honda', 'Hyundai', 'Kia', 'Mazda', 'Mercedes', 'Nissan', 'Renault', 'Toyota', 'Volkswagen'],
    'Modelo':['A3', 'Serie 3', 'Spark', 'Fiesta', 'Civic', 'Accent', 'Rio', '2', 'Clase A', 'Versa', 'Clio', 'Corolla', 'Golf'],
    'Año':[2018, 2018, 2021, 2019, 2020, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021],
    'Precio':[35000, 45000, 20000, 25000, 30000, 18000, 19000, 20000, 50000, 22000, 21000, 30000, 40000],
    'Kilometraje':[20000, 15000, 5000, 10000, 8000, 3000, 4000, 5000, 10000, 6000, 7000, 9000, 12000],
}

df = pd.DataFrame(data)

#Mostrar las primeras 5 filas del dataset
print('Primeras 5 filas del dataset: ')
print(df.head())