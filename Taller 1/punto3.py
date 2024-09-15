#Cree un programa que pida un ángulo y regrese el seno, el coseno y la tangente de este. Pista: use la clase math.

import math
angulo = float(input("Ingrese el ángulo: "))
seno = math.sin(angulo)
coseno = math.cos(angulo)
tangente = math.tan(angulo)
print("El seno del ángulo es: ", seno)
print("El coseno del ángulo es: ", coseno)
print("La tangente del ángulo es: ", tangente)
