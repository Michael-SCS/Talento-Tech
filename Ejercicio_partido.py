import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

partidos = {
    'Equipos':['Argentina','Colombia','Urugua','Brasil','Ecuador','Venezuela','Bolivia','Paraguay','Peru','Chile'],
    'Puntaje':[22,19,16,13,13,12,12,11,6,5],
    'Diferencia de goles':[9,7,7,2,2,-1,-5,-1,-7,-13],
}
df = pd.DataFrame(partidos)

# Seleccionar solo las columnas numéricas
correlation_mat = df[['Puntaje', 'Diferencia de goles']].corr()

# Graficar el heatmap
sns.heatmap(correlation_mat, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlación entre Puntaje y Diferencia de goles')
plt.show()

