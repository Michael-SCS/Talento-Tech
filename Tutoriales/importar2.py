
#Abrir el archivo en modo lectura

with open('animales.txt', 'r') as archivo:
    lineas = archivo.readlines()

#Imprimir los datos
for linea in lineas:
    print(linea.strip())