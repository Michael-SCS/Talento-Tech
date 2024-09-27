import pandas as pd

# 2 Cargar datos
df = pd.read_csv('datos.csv', delimiter=';')

#3 Revisr los datos
print(df.head())
print(df.info())

#4 Eliminar Datos duplicados
df = df.drop_duplicates()

#5 Manejo de Datos faltantes
df['Edad'] = df['Edad'].fillna(0)

#6 Convertir tipos de datos
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')

#7 Eliminar columnas que no se necesitan
df = df.drop(['Altura'], axis=1)

#8 Corregir valores incorrectos
df['Edad'] = df['Edad'].replace(['C'], 'Correcto')

#9 Imprimir el resultado de los datos limpiados
print(df.head())
print(df.info())