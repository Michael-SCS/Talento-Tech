import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Dataframe con los datos de las ventas
np.random.seed(0)
productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D']
ventas = pd.DataFrame({
    'Producto': np.random.choice(productos, 100), #Selecciona aleatoriamente un producto de un array, en este caso de productos
    'Cantidad': np.random.randint(1, 10, 100), #Selecciona aleatoriamente una cantidad
    'Precio': np.random.randint(10, 100, 100) #Selecciona aleatoriamente un precio
})

#Calcular la columna de ingresos de las ventas
ventas['Ingresos'] = ventas['Cantidad'] * ventas['Precio']

#Realizar el analisis exploratorio
print('-------------------Analisis exploratorio--------------------------')
print(ventas.head()) #Mostrar las primeras filas del dataframe
print(ventas.describe()) #Genera resumen estadistico de las columnas numericas


print('-------------------Ingresos por producto--------------------------')
#agrupar por producto y calcular el total de ingresos
ingresos_producto = ventas.groupby('Producto')['Ingresos'].sum().reset_index() #Agrupa por producto y suma los ingresos
ingresos_producto.index += 1
print(ingresos_producto)

print('-------------------Graficar los Ingresos por producto--------------------------')
#Visualizar los ingresos por producto
ingresos_producto.plot(kind='bar', x='Producto', y='Ingresos', color='skyblue', title='Ingresos por producto')
plt.show()