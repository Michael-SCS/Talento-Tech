'''Para el siguiente ejercicio utilizar la librería numpy.
•
Crea un array de 1 dimensión con los números del 0 al 9.
•
Redimensiona este array en una matriz de 2x5.
•
Accede al elemento en la fila 1, columna 3 de la matriz'''

import numpy as np
array = np.arange(10)
print(array)

matriz = array.reshape(2,5)
print(matriz)
print(matriz[0,2])