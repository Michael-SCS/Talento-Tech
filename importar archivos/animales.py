import matplotlib.pyplot as plt

#Datos a graficar
animales = ['Gatos', 'Perros', 'Peces', 'Aves', 'Reptiles']
valores = [50,65,72,14,42]

#Crear el gráfico
plt.pie(valores, labels=animales, autopct='%1.1f%%')

#Añadir título
plt.title('Este es un gráfico de pastel')

#mostrar el gráfico en pantalla
plt.show()