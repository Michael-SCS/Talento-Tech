import numpy as np
from scipy import stats
# Datos
datos = [15, 18, 21, 20, 36, 24, 18, 21, 30]
# Media
media = np.mean(datos)
print(f"Media: {media}")
# Mediana
mediana = np.median(datos)
print(f"Mediana: {mediana}")
# Moda
moda = stats.mode(datos,keepdims=True)
print(f"Moda: {moda.mode[0]} (Frecuencia: {moda.count[0]})")