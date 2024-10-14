import pandas as pd

#1. crear el DataFrame
datos = {
    'altura' : [1.75, 1.80, 1.65, 1.60, 1.70],
    'peso' : [70, 80, 60, 55, 68],
    'edad' : [25, 32, 47, 50, 29]
}
df = pd.DataFrame(datos)

#2. Calcular la matriz de correlación
correlacion_matriz = df.corr()

#3. Mostrar en pantalla la matriz de correlación
print(correlacion_matriz)