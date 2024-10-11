import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

#Generar el conjunto de datos con blobs(burbujas) o agrupaciones
#Las burbujas son un conjunto de puntos generados artificialmente que se agrupan en clusters

X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

#aplicar el algoritmo KMeans con 4 clusters
kmeans = KMeans(n_clusters=4)
y_kmeans = kmeans.fit_predict(X)

#Graficar los puntos y los centros de los clusters
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75)
plt.title('Clustering con K-means')
plt.show()