#Desarrolle un programa que solicite 3 notas de un estudiante y retorne la calificación final con un mensaje que indique si el estudiante pasó o no pasó el curso. Tome en cuenta que, la primera nota equivale al 30% de la notal final, la segunda nota equivale al 30% de la nota final y la tercera nota equivale al 40% de la nota final

for i in range(3):
    if i == 0:
        nota1 = float(input("Ingrese la primera nota: "))
    elif i == 1:
        nota2 = float(input("Ingrese la segunda nota: "))
    else:
        nota3 = float(input("Ingrese la tercera nota: "))

nota_final = (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.40)
if nota_final >= 3:
    print("El estudiante pasó el curso con una nota de: ", nota_final)
else:
    print("El estudiante no pasó el curso con una nota de: ", nota_final)