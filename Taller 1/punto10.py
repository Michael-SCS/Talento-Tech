'''Para el siguiente ejercicio utilizar la librería panda.
Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.'''

import pandas as pd

# Definimos el Data Frame
ventas = pd.DataFrame()

# Segmentamos las listas para que sean más fáciles de utilizar
año = []
ventas_totales = []
ventas_descuento = []

# Pedimos los datos de inicio y fin del ciclo
inicio = int(input("Por favor ingrese el año de inicio: "))
fin = int(input("Por favor ingrese el año de fin: "))

# Pedimos los datos de venta por año
for i in range(inicio, fin+1):
    año.append(i)
    venta = float(input(f"Por favor ingrese las ventas del año {i}: ")) # Agregamos aparte el input
    ventas_totales.append(venta) # Agregamos las ventas a la lista de ventas totales por año
    ventas_descuento.append(venta * 0.9) # Multiplicamos por 0,9 para obtener el 90%, es decir, el descuento de 10%

#Creamos las columnas y le asignamos los valores de las listas al Data Frame. 
ventas['Año'] = año
ventas['Ventas totales'] = ventas_totales
ventas['Ventas con descuento'] = ventas_descuento

print(ventas)