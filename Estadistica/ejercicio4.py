import pandas as pd

data = {
    'Nombre':['Ana, Luis, Marta, Juan'],
    'Edad':[15,16,15,16],
    'Nota Matemáticas':[7.5,6.0,8.5,7.0],
    'Nota Ciencias':[8.0,7.5,9.5,7.0],
}

df = pd.DataFrame(data)
#Muestra las primeras dos filas del dataframe
print(df.head(2))

#Calcular la media de las notas de matemáticas

MediaMatematicas = df['Nota Matemáticas'].mean()

print(f"La media de las notas de matemáticas es: {MediaMatematicas}")

