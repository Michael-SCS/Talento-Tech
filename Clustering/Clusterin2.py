#Este ejercicio genera puntos aleatorios y los agrupa en 4 clusters utilizando el algoritmo de K-means
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

#Generar datos de ejemplo
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0) 
#La función make_blobs nos permite generar datos de ejemplo, en este caso se generan 300 puntos distribuidos en 4 clusters con una desviación estándar de 0.60 y el random_state es para que los datos sean reproducibles, osea la semilla

#Crear el modelo de K-means con 4 clusters
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
#El fit nos permite entrenar el modelo, es decir, encontrar los clusters, en este caso se están buscando 4 clusters

#Predecir los clusters
y_kmeans = kmeans.predict(X)
#El predict nos devuelve un arreglo con los clusters a los que pertenece cada punto,osea, nos dice a que cluster pertenece cada punto

#Graficar los datos y los clusters
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
#c hace referencia a la variable que se va a utilizar para colorear los puntos, s es el tamaño de los puntos y cmap es el mapa de colores

#Graficar los centros de los clusters
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75)
plt.title('Clustering con K-means')
plt.show()
#centers nos devuelve los centros de los clusters, es decir, los puntos que representan el centro de cada cluster


