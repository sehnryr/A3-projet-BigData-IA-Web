from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from statistics import mode

from distance import *


class KNeighborsClassifierScratch:
    def __init__(self, n_neighbors=5, dist_metric=manhattan_distance):
        self.n_neighbors = n_neighbors
        self.dist_metric = dist_metric

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        # Liste des voisins les plus proches pour chaque point de test
        neighbors = []

        # Parcours de tous les points de test
        for x in X_test.values:
            # Calcul des distances entre le point de test et tous les points d'entrainement
            distances = self.dist_metric(x, self.X_train)
            # Tri des distances par ordre croissant
            y_sorted = [y for _, y in sorted(zip(distances, self.y_train))]
            # Ajout des k plus proches voisins
            neighbors.append(y_sorted[: self.n_neighbors])

        # Retourne le mode de chaque liste de voisins
        return [mode(n) for n in neighbors]


# Classifieur KNN manuel
def knn_scratch(X_train, y_train, k=5, dist_metric=manhattan_distance):
    knn = KNeighborsClassifierScratch(n_neighbors=k, dist_metric=dist_metric)
    knn.fit(X_train, y_train)
    return knn


# Classifieur KNN sklearn
def knn_sklearn(X_train, y_train, k=5):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    return knn


if __name__ == "__main__":
    from read import data
    from repartition import *

    data = data[
        [
            "latitude",
            "longitude",
            "descr_athmo",
            "descr_lum",
            "descr_etat_surf",
            "descr_dispo_secu",
            "descr_grav",
        ]
    ]

    # Reduction de la taille de data en prenant 10% de chaque classe
    # pour chaque label
    data = data.groupby("descr_grav").apply(lambda x: x.sample(frac=0.1))

    # for data_train, data_test in repartition_leave_one_out_sklearn(data):
    for data_train, data_test in repartition_holdout_sklearn(data):
        X_train = data_train.drop(columns=["descr_grav"])
        y_train = data_train["descr_grav"]

        X_test = data_test.drop(columns=["descr_grav"])
        y_test = data_test["descr_grav"]

        knn = knn_sklearn(X_train, y_train, k=15)
        knn_score = accuracy_score(y_test, knn.predict(X_test))
        print("SciKit-Learn", round(knn_score, 4))

        knn_hamming = knn_scratch(X_train, y_train, k=15, dist_metric=hamming_distance)
        knn_hamming_score = accuracy_score(y_test, knn_hamming.predict(X_test))
        print("Scratch Hamming", round(knn_hamming_score, 4))

        knn_manhattan = knn_scratch(X_train, y_train, k=15, dist_metric=manhattan_distance)
        knn_manhattan_score = accuracy_score(y_test, knn_manhattan.predict(X_test))
        print("Scratch Manhattan", round(knn_manhattan_score, 4))

        knn_euclidean = knn_scratch(X_train, y_train, k=15, dist_metric=euclidean_distance)
        knn_euclidean_score = accuracy_score(y_test, knn_euclidean.predict(X_test))
        print("Scratch Euclidean", round(knn_euclidean_score, 4))

        knn_minkowski = knn_scratch(X_train, y_train, k=15, dist_metric=minkowski_distance)
        knn_minkowski_score = accuracy_score(y_test, knn_minkowski.predict(X_test))
        print("Scratch Minkowski", round(knn_minkowski_score, 4))

        break
