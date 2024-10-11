import pandas as pd
from sklearn.preprocessing import StandardScaler 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
#Cargar los datos del formato .csv clientes
df = pd.read_csv('Clustering/clientes.csv', delimiter=';')
#Seleccionar las caracteristicas para el clustering
features = df[['edad','frecuencia_compra','gasto_compra']]
#Normalizar datos
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
#Aplicar el algoritmo de kmeans
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(scaled_features)
#añadir etiquetas de cluster al dataframe
df['Cluster'] = clusters
#Visualizar los resultados en gráficos
plt.figure(figsize=(10,6))
sns.scatterplot(x=df['edad'],y=df['gasto_compra'], hue= df['Cluster'], palette='viridis')
plt.xlabel('Edad')
plt.ylabel('Gasto promedio de compra')
plt.title("Segmentación de clientes")
plt.legend(title='Cluster')
plt.show()