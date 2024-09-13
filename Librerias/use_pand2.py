import pandas as pd

#crear el dataframe

data = {
    'Nombre': ['Jorge', 'James','Jose','Lina'],
    'Edad': [22, 33, 12, 17], 
    'Ciudad': ['Medellín', 'Bogotá', 'Manizales', 'Bucaramanga']
}
df = pd.DataFrame(data)
# Filtrar personas mayores de 25
df_mayores = df[df['Edad'] > 25]

print(df_mayores)
