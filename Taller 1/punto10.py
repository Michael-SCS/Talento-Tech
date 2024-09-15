'''Para el siguiente ejercicio utilizar la librería panda.
Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.'''

import pandas as pd

ventas = {"Año": [], "Ventas": [], "Ventas con descuento": []}
inicio = int(input("Por favor ingrese el año de inicio: "))
fin = int(input("Por favor ingrese el año de fin: "))
for i in range(inicio, fin+1):
    ventas["Año"].append(i)
    ventas["Ventas"].append(float(input(f"Por favor ingrese las ventas del año {i}: ")))
    ventas["Ventas con descuento"].append(ventas["Ventas"][-1] * 0.9)
print(ventas)
ventas = pd.DataFrame(ventas)
print(ventas)