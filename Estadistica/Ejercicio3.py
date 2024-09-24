import pandas as pd

#Crear un dataframe de edades
data = {
    'Nombre':['Ursula', 'Pedro', 'Juan', 'Maria', 'Luis', 'Ana', 'Carlos', 'Sofia', 'Pablo', 'Lucia'],
    'Edad':[25, 30, 35, 40, 45, 50, 55, 60, 65, 70]}

df = pd.DataFrame(data)

#Calcular la media y la mediana de la edad
Media = df['Edad'].mean()
Mediana = df['Edad'].median()

print(f"La media de las edades es: {Media}")
print(f"La mediana de las edades es: {Mediana}")