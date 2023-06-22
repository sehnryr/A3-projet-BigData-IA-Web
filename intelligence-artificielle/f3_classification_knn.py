from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from statistics import mode, mean

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
            # Tri des gravités par distance croissante
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
    from f2_reduction import data
    from f3_repartition import *
    from time import time

    # Reduction de la taille de data en prenant 10% de chaque classe
    # pour chaque label
    data = data.groupby("descr_grav").apply(lambda x: x.sample(frac=0.1))

    # Stockage des scores pour chaque classifieur et chaque métrique pour
    # faire des moyennes
    k_scores = [[[] for _ in range(5)] for _ in range(5)]

    k_values = [1, 5, 10, 15, 20]
    clf_values = [
        "sklearn",
        "scratch-hamming",
        "scratch-manhattan",
        "scratch-euclidean",
        "scratch-minkowski",
    ]

    # Compte du nombre de folds
    i = 0
    time_start = time()

    # for data_train, data_test in repartition_leave_one_out_sklearn(data):
    for data_train, data_test in repartition_holdout_sklearn(data):
        time_end = time()
        print(f"Fold {i + 1} {round(time_end - time_start, 3)}s", end="\r")
        time_start = time_end
        i += 1

        X_train = data_train.drop(columns=["descr_grav"])
        y_train = data_train["descr_grav"]

        X_test = data_test.drop(columns=["descr_grav"])
        y_test = data_test["descr_grav"]

        for k in k_values:
            knn = knn_sklearn(X_train, y_train, k=k)
            knn_score = accuracy_score(y_test, knn.predict(X_test))
            k_scores[0][i - 1].append(knn_score)

            knn_hamming = knn_scratch(X_train, y_train, k=k, dist_metric=hamming_distance)
            knn_hamming_score = accuracy_score(y_test, knn_hamming.predict(X_test))
            k_scores[1][i - 1].append(knn_hamming_score)

            knn_manhattan = knn_scratch(X_train, y_train, k=k, dist_metric=manhattan_distance)
            knn_manhattan_score = accuracy_score(y_test, knn_manhattan.predict(X_test))
            k_scores[2][i - 1].append(knn_manhattan_score)

            knn_euclidean = knn_scratch(X_train, y_train, k=k, dist_metric=euclidean_distance)
            knn_euclidean_score = accuracy_score(y_test, knn_euclidean.predict(X_test))
            k_scores[3][i - 1].append(knn_euclidean_score)

            knn_minkowski = knn_scratch(X_train, y_train, k=k, dist_metric=minkowski_distance)
            knn_minkowski_score = accuracy_score(y_test, knn_minkowski.predict(X_test))
            k_scores[4][i - 1].append(knn_minkowski_score)

    # k_scores_mean = [[0.518479293957909, 0.4719076714188731, 0.4940122199592668, 0.4913509843856076, 0.4913509843856076], [0.518479293957909, 0.4719076714188731, 0.4940122199592668, 0.4913509843856076, 0.4913509843856076], [0.518479293957909, 0.4719076714188731, 0.4940122199592668, 0.4913509843856076, 0.4913509843856076], [0.518479293957909, 0.4719076714188731, 0.4940122199592668, 0.4913509843856076, 0.4913509843856076], [0.518479293957909, 0.4719076714188731, 0.4940122199592668, 0.4913509843856076, 0.4913509843856076]]

    k_scores_mean = [[mean(d) for d in k_score] for k_score in k_scores]

    print(k_scores_mean)

    import matplotlib.pyplot as plt

    from utils import current_path

    plt.imshow(k_scores_mean, cmap=plt.get_cmap("viridis"))
    plt.title("Score moyen pour chaque classifieur et k")
    plt.xlabel("k")
    plt.xticks(range(len(k_values)), k_values)
    plt.yticks(range(len(clf_values)), clf_values)
    plt.colorbar()
    plt.tight_layout()

    scores_avg = round((np.max(k_scores_mean) + np.min(k_scores_mean)) / 2, 3)
    for (j, i), label in np.ndenumerate(k_scores_mean):
        plt.text(
            i,
            j,
            round(label, 3),
            ha="center",
            va="center",
            color="white" if label < scores_avg else "black",
        )

    plt.savefig(f"{current_path}/export/knn_scores.png")
    plt.close()
