#leer el archivo .txt y guardar en una lista

with open('animales.txt', 'r') as archivo:
    datos = [linea.strip() for linea in archivo]

print(datos)

