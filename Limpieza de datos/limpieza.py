#Verificar si hay valores nulos con la funcion isnull()

import pandas as pd
#Crear nuevo DataFrame
datos = {'Nombre': ['Juan', 'Ana', 'Pedro', 'Maria', None, 'Laura'],
'Edad': [23, None, 22, 19, 23, 78],
'Ciudad': ['Bogota', 'Bogota', None, 'Bogota', 'Medellin', 'Bogota'],
}

df = pd.DataFrame(datos)
print(df)

#Verificar si existen datos nulos
print(df.isnull())

#Contar cuantos datos nulos hay en cada columna
print(df.isnull().sum())

#Eliminar filas con datos nulos
df = df.dropna()
print(df)

#Rellenar los valores nulos
#Rellenar los valores nulos
df_relleno = df.fillna({'Nombre': 'Desconocido', 'Edad': 0, 'Ciudad': 'Desconocido'})
print (df_relleno)

#Rellenar los valores nulos con el valor anterior
df_relleno = df.bfill()
print(df_relleno)