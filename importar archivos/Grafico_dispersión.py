import matplotlib.pyplot as plt

#datos a graficar
x = [2,4,6,8,10,12]
y = [5,10,115,220,230,325]

#Crear el gráfico
plt.scatter(x,y)

#añadir titulos
plt.title('Gráfico de dispersión')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

#Mostrar el gráfico
plt.show()