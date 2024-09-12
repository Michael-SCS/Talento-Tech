#hallar la potencia y la raíz cuadrada de un número

import math

#solicitar al usuario que digite un número  
numero = float(input("Digite un número al que desea calcular la potencia y sacar la raiz cuadrada: "))
elevado = float(input("Digite un número al que desea elevar el número: "))
#calculando la potencia del número
potencia = math.pow(numero, elevado)
print("La potencia de ",numero," es: ",potencia)

#calculando la raíz cuadrada del número
raiz = math.sqrt(numero)

print("La raíz cuadrada de ",numero," es: ",raiz)
print("La potencia del número ",numero," elevado a ",elevado," es: ",potencia)