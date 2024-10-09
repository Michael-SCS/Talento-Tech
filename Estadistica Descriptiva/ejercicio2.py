import pandas as pd

#Crear el Dataframe
df1 = pd.DataFrame({
    'id':[1,2,3,4,5],
    'edad':[23,45,56,34,23],
})
df2 = pd.DataFrame({
    'id':[1,2,3,4,5],
    'nombre':['Juan','Pedro','Maria','Luis','Ana'],
})

df_merge = pd.merge(df1, df2, on='id', how='inner')

print(df_merge)