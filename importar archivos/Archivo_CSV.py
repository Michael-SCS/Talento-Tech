import pandas as pd

#Leer archivo CSV
datos = pd.read_csv('ventas.csv') #Se pueden usar archivos .txt .json o .xlsx
print(datos.head()) #Imprime el archivo completo