from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

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
    def __init__(self, k=5, dist_metric=hamming_distance):
        self.k = k
        self.dist_metric = dist_metric

    def most_common(self, lst):
        """Retourne la valeur la plus fréquente d'une liste"""
        return max(set(lst), key=lst.count)

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        neighbors = []
        for x in X_test.values:
            distances = self.dist_metric(x, self.X_train)
            y_sorted = [y for _, y in sorted(zip(distances, self.y_train))]
            neighbors.append(y_sorted[: self.k])
        return [self.most_common(n) for n in neighbors]


# Classifieur KNN manuel
def knn_scratch(X_train, y_train, k=5):
    knn = KNeighborsClassifierScratch(k=k)
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

        knn = knn_scratch(X_train, y_train, k=10)
        y_pred = knn.predict(X_test)

        print(accuracy_score(y_test, y_pred))
