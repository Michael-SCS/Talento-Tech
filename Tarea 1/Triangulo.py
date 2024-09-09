import math

a = float(input("Ingresa el valor del cateto opuesto"))
b = float(input("Ingresa el valor del cateto adyacente"))

c = math.sqrt(a**2 + b**2)

print("La hipotenusa es: ", c)