import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Generar el Dataframe
estudiantes = pd.DataFrame({
    'Nombre':['Juan', 'Maria', 'Pedro', 'Luis', 'Ana', 'Sofia', 'Carlos', 'Andres', 'Jose', 'Laura'],
    'Matemáticas': np.random.randint(1,5, 10),
    'Ciencias': np.random.randint(1,5, 10),
    'Español':np.random.randint(1,5, 10)
})

#Calcular el promedio de cada estudiante
estudiantes['Promedio'] = estudiantes[['Matemáticas', 'Ciencias', 'Español']].mean(axis=1) #axis=1 para que se calcule por fila
print(estudiantes)

#Visualizacion de la distribución de las notas
estudiantes['Matemáticas'].plot(kind='hist', bins=5, color='blue', edgecolor='black',title='Distribución de notas de Matemáticas',x='Notas',)
plt.show()

#Visualizacion del promedio de notas por estudiantes
estudiantes.plot(kind='bar', x='Nombre', y='Promedio', color='green', title='Promedio de notas por estudiante')
plt.show()