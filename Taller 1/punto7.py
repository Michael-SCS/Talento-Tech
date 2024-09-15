'''Se requiere desarrollar un programa donde almacene cada una de las edades del grupo Análisis de datos, en un vector de números enteros y determinar lo siguiente:

Cantidad de estudiantes menores de edad.
•
Cantidad de estudiantes mayores a 25 años.
•
Mostrar el estudiante con la edad más baja del grupo.
•
Mostrar el estudiante con la edad más alta del grupo.
•
Hallar y mostrar el promedio de las edades de los estudiantes.'''
edades = []
menores_18 = 0
mayores_25 = 0
menor = 0
mayor = 0
suma = 0


print("BIENVENIDO AL PROGRAMA DE ANÁLISIS DE DATOS")
while True:
    edad = int(input("Por favor ingrese la edad del estudiante: "))
    if edad == 0:
        break
    else:
        edades.append(edad)
        print("Gracias por guardar la edad del estudiante, continua guardando si deseas, de lo contrario oprime 0 ")
        if edad < 18:
            menores_18 =menores_18 + 1
        if edad > 25:
            mayores_25 = mayores_25 + 1
menor = min(edades)
mayor = max(edades)
suma = sum(edades) / len(edades)



print("Cantidad de estudiantes menores de edad:", menores_18)
print("Cantidad de estudiantes mayores a 25 años:", mayores_25)
print("Estudiante con la edad más baja del grupo:", menor)
print("Estudiante con la edad más alta del grupo:", mayor)
print("Promedio de las edades de los estudiantes:", suma)

