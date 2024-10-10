import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
# Generar un conjunto de datos aleatorio
np.random.seed(0)
n_samples = 300
n_features = 2

# Crear datos aleatorios en forma de dos grupos
X = np.random.randn(n_samples, n_features)

# Aplicar K-means
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# Obtener etiquetas de los clusters
labels = kmeans.labels_

# Crear un DataFrame y fusionar los resultados
df = pd.DataFrame(X, columns=['Feature 1', 'Feature 2'])
df['Cluster'] = labels
# Mostrar los primeros 5 registros
print(df.head())
# Graficar los resultados
plt.scatter(df['Feature 1'], df['Feature 2'], c=df['Cluster'], cmap='viridis')
plt.title('Clustering con K-means')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Cluster')
plt.show()