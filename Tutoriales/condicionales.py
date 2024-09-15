''' Las estructuras repetitivas, como su nombre lo indica, nos ayudan a repetir 
una "n" cantidad de veces un fragmento de código '''

#Ejemplo de for utilizando iterador:
print('#1')
numeros = [12,21,38,47,51]
for i in range(len(numeros)):
    print(numeros[i])

print('#2')
#Ejemplo de for each (especial para listas):
for numero in numeros:
    print(numero)

print('#3')
#Ejemplo de estructura while, funcionando de la misma manera que un for:
i = 0
while i < len(numeros):
    print(numeros[i])
    i += 1

print('#4')
# Funciones de los for: break y continue
for i in range(10):
    if i == 5:
        continue
    
    print(i)

print('#5')
for i in range(10):
    if i == 5:
        print('De verdad no me gusta el número 5')
        break
    
    print(i)