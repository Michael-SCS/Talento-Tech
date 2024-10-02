print('-------------TRABAJO PROPUESTO EN CLASE--------------------------------')
#Agrupar por estudiantes y notas
import pandas as pd
import numpy as np

datos ={
    'Estudiante': ['Lina Maria', 'Kisis Paola', 'Juan Pablo', 'Lucelly', 'Luis Fernando', 'Natalia'],
    'Materia': ['Español', 'Inglés','Matemáticas','Física','Sociales', 'Español'],
    'Calificación':[4.2, 3.5, 3.5, 2.0, 2.6, 3.7],
}

df = pd.DataFrame(datos)
print(df)

print('--------------Materias y promedio-------------------------------')
#Agrupar por columna Materia, donde se calcula el promedio de las califiaciones por materia
columna_materia = df.groupby('Materia')['Calificación'].mean().reset_index()
columna_materia.index += 1
print(columna_materia)

print('------------------Estudiante y promedio---------------------------')
#Agrupar por la columna estudiante y calcular el promedio de las calificaciones por estudiante
columna_estudiantes = df.groupby('Estudiante')['Calificación'].mean().reset_index()
columna_estudiantes.index += 1
print(columna_estudiantes)

print('-------------------Multiples columnas--------------------------')
#Agrupar por multiples columnas, donde se agrupa por estudiante y materia para saber como está el desempeño del estudiante por materia
columna_estudiante_materia = df.groupby(['Estudiante','Materia'])['Calificación'].sum().reset_index()
columna_estudiante_materia.index += 1
print(columna_estudiante_materia)

print('-------------------Agrupacion multiples funciones--------------------------')
#Agrupar por multiples funciones de agregacion como en la suma, el conteo de califacliones y el promedio
estadistica_materia = df.groupby('Materia').agg({'Calificación': ['sum', 'count', 'mean']}).reset_index()
estadistica_materia.index += 1
print(estadistica_materia)

print('-------------------Agrupacion por calificaciones mayores a 3.0--------------------------')
#Mostrar el estudiante cuya calificación sea mayor a 3.5
calificacion_estudiante = df.groupby('Estudiante')['Calificación'].sum().reset_index()

calificacion_estudiante = calificacion_estudiante[calificacion_estudiante['Calificación'] > 3.5]

calificacion_estudiante.index += 1

print(calificacion_estudiante)