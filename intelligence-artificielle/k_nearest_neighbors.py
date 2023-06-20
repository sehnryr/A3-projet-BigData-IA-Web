from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from statistics import mode

from read import data
from repartition import *
from distance import *


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
    for data_train, data_test in repartition_holdout_scratch(data):
        X_train = data_train.drop(columns=["descr_grav"])
        y_train = data_train["descr_grav"]

        X_test = data_test.drop(columns=["descr_grav"])
        y_test = data_test["descr_grav"]

        knn = knn_sklearn(X_train, y_train, k=15)
        print("SciKit-Learn", round(accuracy_score(y_test, knn.predict(X_test)), 4))

        knn_hamming = knn_scratch(X_train, y_train, k=15, dist_metric=hamming_distance)
        print(
            "Scratch Hamming",
            round(accuracy_score(y_test, knn_hamming.predict(X_test)), 4),
        )

        break
