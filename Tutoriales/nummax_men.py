#Realizar un programa que determine cual es el número mayor y menor de tres números ingresados

#Se ingresan 3 números por teclado

numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

#Determinar el número mayor y menor
mayor = max(numero1,numero2,numero3)
menor = min(numero1,numero2,numero3)

print("El número mayor es: ",mayor, " ,Y el menor es: ",min)