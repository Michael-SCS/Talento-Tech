import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Crear el Dataframe
data = {
    'Edad':[25,35,47,51,60,22,35,41],
    'Salario':[30000,45000,70000,65000,85000,25000,50000,62000],
    'Años_experiencia':[2,5,20,18,25,1,8,15]
}

df = pd.DataFrame(data)

#Calcular la matriz de corelación
correlation_matrix = df.corr()
#Visualizar el mapa de calor
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Mapa de calor de la matriz de correlación')
plt.show()
