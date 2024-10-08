import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
#Cargar el Dataset de almacen
data = pd.read_csv('almacen.csv', delimiter=';')
df = pd.DataFrame(data)
print(df.head())

df['Precio'] = df['Precio'].str.replace('$', '', regex=False)  # Eliminar el símbolo $ 
df['Precio'] = df['Precio'].str.replace('.', '', regex=False)  
df['Precio'] = df['Precio'].astype(int) # Convertir a entero

#agragar nueva columna Total
df['Total'] = df['Precio']*df['Cantidad']
print(df.head())

#alcular sobre las ventas: el total de ventas, la media, valor máximo, valor mínimo 
print('El total de ventas es ',df['Total'].sum())
print('La media es ',df['Total'].mean())
print('El valor máximo es ',df['Total'].max())
print('El valor mínimo es ',df['Total'].min())

#Agrupar las ventas por producto para ver el total de ventas por cada producto.
print('---------------------------------------------')
ventas_producto = df.groupby('Total')['Producto'].sum().reset_index()
print(ventas_producto)

#Filtrar los datos donde se vendieron más de 4 artículos.
print('---------------------------------------------')
articulos = df.groupby('Producto')['Cantidad'].sum().reset_index()
if articulos['Cantidad'].sum() > 1000:
    articulos4 = articulos[articulos['Cantidad'] > 1000]
print(articulos)
print(articulos4)