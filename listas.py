#crear listas
#crear una lista vacia
lista_vacia = []
print(lista_vacia)

#crear una lista con elementos
numeros = [1,2,3,4,5]
print(numeros)

#crear una lista de elementos de diferentes tipos de datos

lista_variada = [1,2.0,"tres",4,5,True]
print(lista_variada)

#acceder a los elementos de una lista
animales = ["perro","gato","loro","pez","conejo","tortuga","iguana"]
print(animales[0])

#modificar un elemento de una lista
animales[1] = "Ardillas"

#agregar elementos al final de lista
animales.append("Elefante")

#Insertar un elemento en una posicion especifica
animales.insert(2,"Cocodrilo")
print(animales)

#eliminar un elemento de una lista
animales.remove("pez")
print(animales)


#longitud de una lista
print(len(animales))
print("La longitud de la lista animales es de: ", len(animales))

