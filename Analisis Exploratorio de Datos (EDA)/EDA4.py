#Generar un Dataframe con nombres de estudiantes y sus calificaciones en tres materias y realiza un análisis simple de estas calificaciones.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Generar el Dataframe
estudiantes = pd.DataFrame({
    'Nombre':['Juan', 'Maria', 'Pedro', 'Luis', 'Ana',],
    'Calculo_1': np.random.randint(1,10, 5),
    'Matemáticas_Especiales': np.random.randint(1,10, 5),
    'Física_mecánica':np.random.randint(1,10, 5)
})

#Calcular el promedio de cada estudiante
estudiantes['Promedio'] = estudiantes[['Calculo_1', 'Matemáticas_Especiales', 'Física_mecánica']].mean(axis=1) #axis=1 para que se calcule por fila
print(estudiantes)

#Visualizacion de la distribución de las notas
estudiantes['Calculo_1'].plot(kind='hist', bins=5, color='blue', edgecolor='black',title='Distribución de notas de Calculo 1',x='Notas',)
plt.show()

#Visualizacion del promedio de notas por estudiantes
estudiantes.plot(kind='bar', x='Nombre', y='Promedio', color='green', title='Promedio de notas por estudiante')
plt.show()

