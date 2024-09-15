#Realizar el siguiente código, al frente de cada línea colocar un comentario donde explique ¿cuál es su función

agenda ={} #declaramos un diccionario vacio llamado agenda

print("BIENVENIDO A TU AGENDA TELEFÓNICA") #imprimimos un mensaje de bienvenida
while True:
    nombre = input("Por favor ingrese el nombre: ") #solicitamos el nombre del contacto
    if nombre == "0": #comparamos si el nombre es igual a 0
        break #si el nombre es igual a 0 se rompe el ciclo
    else:
        telefono = input("Por favor ingrese el número telefonico: ") #solicitamos el telefono del contacto
        correo = input("Por favor ingrese el correo electrónico: ") #solicitamos el correo del contacto
        agenda[nombre] = [telefono, correo] #agregamos el contacto a la agenda
        print("Gracias por guardar tu contacto, continua guardando si deseas, de lo contrario oprime 0 ") #imprimimos un mensaje de agradecimiento y damos instrucciones para salir del ciclo

print("Tu agenda es: ", agenda) #imprimimos la agenda completa