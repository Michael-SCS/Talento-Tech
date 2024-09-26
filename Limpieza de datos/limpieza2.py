import pandas as pd

data = {
    'Nombre': ['Juan', 'Ana', 'Pedro', 'Maria', 'Laura'],
    'Edad': [23, 22, 19, 23, 78],
    'Ciudad': ['Bogota', 'Bogota', 'Bogota', 'Medellin', 'Bogota'],
}

df = pd.DataFrame(data)
print(df)

df_sin_duplicados = df.drop_duplicates()
print(df_sin_duplicados) #Todas las columnas tienen que ser iguales para que se elimine el duplicado

