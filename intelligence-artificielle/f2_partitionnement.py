import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import normalized_mutual_info_score
from distance import *


class KMeansScrach:
    cluster_centers_ = None

    def __init__(
        self,
        n_clusters=4,
        n_init=10,
        max_iter=300,
        random_state=0,
        dist_metric=euclidean_distance,
    ):
        self.n_clusters = n_clusters
        self.n_init = n_init
        self.max_iter = max_iter
        self.random_state = random_state
        self.dist_metric = dist_metric
        np.random.seed(random_state)

    def fit(self, X_train):
        # Initialisation des centres de cluster
        min_lat, max_lat = np.min(X_train[:, 0]), np.max(X_train[:, 0])
        min_long, max_long = np.min(X_train[:, 1]), np.max(X_train[:, 1])
        self.cluster_centers_ = np.random.uniform(
            [min_lat, min_long], [max_lat, max_long], (self.n_clusters, 2)
        )

        # Attribution des points aux clusters
        distances = [self.dist_metric(x, self.cluster_centers_) for x in X_train]
        points = np.argmin(distances, axis=1)

        # Iterations de l'algorithme jusqu'à convergence ou max_iter
        iteration = 0
        prev_centroids = None
        while (
            np.not_equal(self.cluster_centers_, prev_centroids).any()
            and iteration < self.max_iter
        ):
            self.cluster_centers_ = []
            for i in range(self.n_clusters):
                temp_centroid = X_train[points == i].mean(axis=0)
                self.cluster_centers_.append(temp_centroid)

            self.cluster_centers_ = np.vstack(self.cluster_centers_)

            distances = [self.dist_metric(x, self.cluster_centers_) for x in X_train]
            points = np.argmin(distances, axis=1)

            prev_centroids = self.cluster_centers_
            iteration += 1
            print(f"Iteration {iteration} / {self.max_iter}")

        self.indexes = points

        return self

    def fit_predict(self, X_train):
        return self.indexes


# Fonction de calcul des k-means à la main
def k_means_scratch(
    X,
    n_clusters=4,
    n_init=10,
    max_iter=300,
    random_state=0,
    dist_metric=euclidean_distance,
):
    kmeans = KMeansScrach(
        n_clusters=n_clusters,
        n_init=n_init,
        max_iter=max_iter,
        random_state=random_state,
        dist_metric=dist_metric,
    ).fit(X)
    indexes = kmeans.fit_predict(X)
    return (kmeans, indexes)


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


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from sklearn.metrics.pairwise import haversine_distances

    from f1_preparation_data import data
    from utils import current_path

    def save_map(kmeans, indexes, title_name, file_name):
        # Graphique scatter des accidents sur une carte de France
        plt.figure(figsize=(10, 10))
        plt.title("Accidents en France - " + title_name)
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.scatter(X[:, 0], X[:, 1], c=indexes, s=2)
        plt.scatter(
            kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c="red", s=100
        )
        plt.savefig(f"{current_path}/export/kmeans-{file_name.lower()}.png")
        plt.close()

    # Preparation des données pour le clustering
    # Recuperation des longitudes et latitudes par gravité d'accident
    X = data[["longitude", "latitude"]].values

    # On ne garde que les accidents qui se sont produits en France
    X = X[(X[:, 0] > -5) & (X[:, 0] < 10) & (X[:, 1] > 40) & (X[:, 1] < 52)]

    k = 4

    # On effectue le clustering
    kmeans, indexes = k_means_sklearn(X, n_clusters=k)
    save_map(kmeans, indexes, f"Sklearn, k={k}", f"sklearn-k{k}")

    # On effectue le clustering
    kmeans, indexes = k_means_scratch(
        X,
        n_clusters=k,
        max_iter=100,
        random_state=10,
        dist_metric=manhattan_distance,
    )
    save_map(kmeans, indexes, f"Scratch-L1, k={k}", f"scratch-l1-k{k}")

    # On effectue le clustering
    kmeans, indexes = k_means_scratch(
        X,
        n_clusters=k,
        max_iter=100,
        random_state=10,
        dist_metric=euclidean_distance,
    )
    save_map(kmeans, indexes, f"Scratch-L2, k={k}", f"scratch-l2-k{k}")

    # On effectue le clustering
    kmeans, indexes = k_means_scratch(
        X,
        n_clusters=k,
        max_iter=100,
        random_state=10,
        dist_metric=haversine_distance,
    )
    save_map(kmeans, indexes, f"Scratch-Haversine, k={k}", f"scratch-haversine-k{k}")
