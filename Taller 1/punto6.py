#Realizar el siguiente diccionario de datos, al frente de cada línea explicar su función.

equipos = {"Tigres":["Patricia","Juana","Esmeralda"],
           "Diablos":["Jorge","Diana","Luis"],
           "Lobos":["Alejandro","Paola","Yenny"]} #declaramos un diccionario con 3 equipos de futbol y sus respectivos jugadores    
for nombreEquipo in equipos:
    print(nombreEquipo, equipos[nombreEquipo]) #imprimimos el nombre del equipo y sus jugadores

print("Estos son los integrantes del equipo Tigres:")
print(equipos["Tigres"]) #imprimimos los jugadores del equipo Tigres