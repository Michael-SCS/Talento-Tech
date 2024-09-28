#importar librerias
import pandas as pd

#Leer el archivo csv
data = pd.read_csv('datos_problematicos.csv')
df = pd.DataFrame(data)

print('\nData frame original:\n')
print(df)

#Renombrar columnas
df.rename(columns={'nombrrre': 'Nombre', 'apelllidos' : 'Apellidos', 'email':'Correo',
            'gender' : 'Género', 'direccioness':'Direccion IP', 'edaaaaad':'Edad'
        }, inplace=True)

print('\nColumnas con datos nulos:\n')
print(df.isnull().sum())

#Eliminar valores duplicados
df = df.drop_duplicates()

#Eliminar valores nulos por columna | Esto ya que como son diferentes datos, no pueden interpretarse igual
df['Correo'] = df['Correo'].fillna('sincorreo@desconocido.com')
df['Género'] = df['Género'].fillna('No especificado')
df['Direccion IP'] = df['Direccion IP'].fillna('0.0.0.1')
df['Edad'] = df['Edad'].fillna(df['Edad'].mean())

#Cambiar todo el Female y Male por Masculino y femenino
df['Género'] = df['Género'].replace({'Male':'Masculino', 'Female': 'Femenino', 'Non-Binary':'No binario'})

#Cambiar la edad a entero
df['Edad'] = df['Edad'].astype(int)

print('\nData frame limpio:\n')
print(df)

#Escribir los datos limpios en un nuevo archivo csv
df.to_csv('datos_normalizados.csv')
