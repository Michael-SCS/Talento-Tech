#Generar un DataFrame con información de varios empleados y analizar estadisticamente la edad, experiencia y salario
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear un DataFrame con información de varios empleados
empleados = pd.DataFrame({
    'Nombre':['Juan', 'Maria', 'Pedro', 'Luis', 'Ana', 'Sofia', 'Carlos', 'Andres', 'Jose', 'Laura'],
    'Edad': np.random.randint(18, 65, 10),
    'Experiencia': np.random.randint(0, 10, 10),
    'Salario': np.random.randint(1000, 10000, 10)
})
#Analisis exploratorio
print('-------------------Analisis exploratorio--------------------------')
print(empleados.head()) #Mostrar las primeras filas del dataframe
print(empleados.describe()) #Genera resumen estadistico


print('-------------------Salarios por Edades--------------------------')
#Visualizar las edades y salarios
empleados.plot(kind='scatter', x='Edad', y='Salario', color='blue',title='Salarios por Edades')
plt.show()

print('-------------------Histograma de la experiencia --------------------------')
#Visualizar la experiencia
empleados['Experiencia'].plot(kind='hist', color='green', title='Histograma de la Experiencia',bins=5,x='Años de experiencia')
plt.show()