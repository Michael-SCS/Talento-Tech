#La emisora, cuenta con presencia en diferentes municipios de Caldas y se desea conocer el rating de canciones y cantantes más escuchados en el 2024. De acuerdo a lo planteado anteriormente, se solicita a los estudiantes de Análisis de datos, brinden una solución para conocer la respuesta de 10 personas, esto se hará con fines administrativos y realizar una rifa entre las personas encuestadas, la emisora desea poder registrar estas personas con los siguientes datos: cédula, fecha de nacimiento, nombre completo, correo electrónico, municipio de residencia, esta información debe ser almacenada en un arreglo y mostrarla en pantalla.

import pandas as pd
personas = []
print("BIENVENIDO AL PROGRAMA DE ANÁLISIS DE DATOS")
for i in range(10):
    cedula = int(input("Por favor ingrese su cédula: "))
    fecha_nacimiento = input("Por favor ingrese su fecha de nacimiento: ")
    nombre = input("Por favor ingrese su nombre completo: ")
    correo = input("Por favor ingrese su correo electrónico: ")
    municipio = input("Por favor ingrese su municipio de residencia: ")
    personas.append([cedula, fecha_nacimiento, nombre, correo, municipio])
df = pd.DataFrame(personas, columns=['Cédula', 'Fecha de nacimiento', 'Nombre completo', 'Correo electrónico', 'Municipio de residencia'])
print(df)