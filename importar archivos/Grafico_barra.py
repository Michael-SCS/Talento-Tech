#Importar libreria
import matplotlib.pyplot as plt

#Colocar los datos a graficar
a = ['A','B','C','D','E']
b = [1,2,3,4,5]

#Crear el gráfico
plt.plot(a,b)

#Crear los títulos
plt.title('Gráfico de barras')
plt.xlabel('Eje A')
plt.ylabel('Eje B')

#Mostrar el gráfico
plt.show()
