# Abrir el archivo en modo lectura
with open("animales.txt", "r") as archivo:
    contenido = archivo.readline()
# Imprimir el contenido completo
print(contenido)