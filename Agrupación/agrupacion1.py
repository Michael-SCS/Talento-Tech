#Ejercicios de agrupación de datos de una fruteria
#Importar las librerias o bibliotecas necesarias
import pandas as pd
import numpy as np 

#Crear el DataFrame
data = {
    'Producto': ['Manzana', 'Pera', 'Naranja', 'Mango','Uva','Banano'],
    'Cantidad': [10, 5, 6, 12, 15, 20],
    'Precio': [5000, 3000, 4000, 6000, 7000, 2000],
    'Fecha': pd.date_range('2024-10-01', periods=6, freq='D')
}
df = pd.DataFrame(data)
print(df)
print('---------------------------------------------')
#Agrupacion por columna de producto, se va a calcular la cantidad total de productos vendidos por el tipo de producto
ventas_producto = df.groupby('Producto')['Cantidad'].sum().reset_index()
print(ventas_producto)


print('---------------------------------------------')
#Agrupación por multiples columnas de la tienda de frutas, agrupar por fcha para ver cuantos productos se vendieron cad día
ventas_producto_fecha = df.groupby(['Producto', 'Fecha'])['Cantidad'].sum().reset_index()
print(ventas_producto_fecha)

print('---------------------------------------------')
#Agrupar por producto y aplicar dos funciones, sumar y promediar 
estadistica_tienda = df.groupby('Producto').agg({'Cantidad': ['sum', 'mean'],'Precio':['sum','mean']}).reset_index()
print(estadistica_tienda)


print('---------------------------------------------')
#Agrupar los productos que tienen cantidad vendida o un valor en especifico, por ejemplo 7 unidades

productos_vendidos = df.groupby('Producto')['Cantidad'].sum().reset_index()
productos_vendidos = productos_vendidos[productos_vendidos['Cantidad'] > 7]

print(productos_vendidos)

print('---------------------------------------------')
#Agrupar por fechas
ventas_fecha = df.groupby('Fecha')['Cantidad'].sum().reset_index()
print(ventas_fecha)

