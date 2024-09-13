import pandas as pd

#crear un diccionario de datos
diccionario = {
    'Nombre': ['Juan', 'Ana','Jose','Arturo'],
    'Edad': [25, 30, 35, 40], 
    'Ciudad': ['Medellín', 'Bogotá', 'Manizales', 'Bucaramanga']
}
#crear un dataframe usando el diccionario

df = pd.DataFrame(diccionario)
#imprimir el dataframe
print(df)

