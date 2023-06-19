import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import normalized_mutual_info_score

from read import data

# Fonction de calcul des k-means à la main
def k_means_scratch(X, n_clusters=4, n_init=10, max_iter=300, random_state=0):
    pass


# Fonction de calcul des k-means avec scikit-learn
def k_means_sklearn(X, n_clusters=4, n_init=10, max_iter=300, random_state=0):
    kmeans = KMeans(
        n_clusters=n_clusters,
        n_init=n_init,
        max_iter=max_iter,
        random_state=random_state,
    ).fit(X)
    indexes = kmeans.fit_predict(X)
    return (kmeans, indexes)


# Preparation des données pour le clustering
# Recuperation des longitudes et latitudes par gravité d'accident
X = data[["longitude", "latitude"]].values

# On ne garde que les accidents qui se sont produits en France
X = X[(X[:, 0] > -5) & (X[:, 0] < 10) & (X[:, 1] > 40) & (X[:, 1] < 52)]

# On effectue le clustering
kmeans, indexes = k_means_sklearn(X, n_clusters=4)

# Graphique scatter des accidents sur une carte de France
plt.figure(figsize=(10, 10))
plt.title("Accidents en France")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.scatter(X[:, 0], X[:, 1], c=indexes, s=2)
plt.scatter(
    kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c="red", s=100
)
plt.show()
plt.close()
