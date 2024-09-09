#Salario Bruto=Sueldo Base+Horas Extras
#Salario Neto=Salario Bruto − Descuentos


nombre = input("Ingresa el nombre del empleado: ")
base = float(input("Ingresa el sueldo base: "))
horas_extras = float(input("Ingresa el número de horas extras: "))
if horas_extras > 0:
    horas = float(input("Ingresa el valor de la hora extra: "))
else:
    horas = 0
salario_bruto = base + (horas * horas_extras)
descuentos = float(input("Ingresa el valor de los descuentos: "))
salario_neto = salario_bruto - descuentos

print("El salario neto de ",nombre," es: ",salario_neto)