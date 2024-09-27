# Ejercicio de Manejo de valores faltantes
#importar la libreria
import pandas as pd
#crear DataFrame con valores que falten
datos = {
        'cedula': [100,20, 300,40,501,6325],
        'nombre': ['Astrid', 'Carlos','Jorge Alberto', 'Michael', 'Juan David', 'Tomas'],
        'pais': ['Francia', None, 'Argentina', 'Brazil', 'México', 'Canadá'],
        'edad': [25,None, 25, None, 19, 24 ]
        }
#Crear el DataFrame
df = pd.DataFrame(datos)    
#Mostrar el DataFrame
print("El siguiente DataFrame contiene los datos de los campistas")
print(df)
#Eliminar las filas que no tienen valores osea que contienen valores nulos
df_nulos = df.dropna()
# Ingresar valores especificos faltantes
df_ingresar = df.fillna({'nombre': 'Carlos','edad':df['edad'].mean(),'pais': 'Inglaterra'})
print("\nDataFrame después de que elimine las filas")
print(df_nulos)
print("\nDataFrame después de ingresar los valores")
print(df_ingresar)