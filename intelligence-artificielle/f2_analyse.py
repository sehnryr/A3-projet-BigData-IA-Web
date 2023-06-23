if __name__ == "__main__":
    from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
    from time import time

    from f1_preparation_data import data
    from f2_partitionnement import k_means_scratch, k_means_sklearn

    # Reduction de la taille de data en prenant 10% de chaque classe
    # pour chaque label
    data = data.groupby("descr_grav").apply(lambda x: x.sample(frac=0.1))

    # Preparation des données pour le clustering
    # Recuperation des longitudes et latitudes par gravité d'accident
    X = data[["longitude", "latitude"]].values

    # On ne garde que les accidents qui se sont produits en France
    X = X[(X[:, 0] > -5) & (X[:, 0] < 10) & (X[:, 1] > 40) & (X[:, 1] < 52)]

    k_values = [5, 10, 15, 20, 25]
    k_means_values = [
        "sklearn",
        "scratch_l1",
        "scratch_l2",
        "scratch_haversine",
    ]

    scores_silhouette_score = [
        [0 for _ in range(len(k_values))]
        for _ in range(len(k_means_values))
    ]
    scores_calinski_harabasz_score = [
        [0 for _ in range(len(k_values))]
        for _ in range(len(k_means_values))
    ]
    scores_davies_bouldin_score = [
        [0 for _ in range(len(k_values))]
        for _ in range(len(k_means_values))
    ]

    # Compte le nombre de fois que l'on a effectué le clustering
    i = 0
    time_start = time()

    for k in k_values:
        time_end = time()
        print(f"Fold {i + 1} {round(time_end - time_start, 3)}s", end="\r")
        time_start = time_end
        i += 1

        _, indexes_sklearn = k_means_sklearn(X, n_clusters=k)
        _, indexes_scratch_l1 = k_means_scratch(X, n_clusters=k, max_iter=100)
        _, indexes_scratch_l2 = k_means_scratch(X, n_clusters=k, max_iter=100)
        _, indexes_scratch_haversine = k_means_scratch(X, n_clusters=k, max_iter=100)

        # Silhouette score
        scores_silhouette_score[0][k_values.index(k)] = silhouette_score(X, indexes_sklearn)
        scores_silhouette_score[1][k_values.index(k)] = silhouette_score(X, indexes_scratch_l1)
        scores_silhouette_score[2][k_values.index(k)] = silhouette_score(X, indexes_scratch_l2)
        scores_silhouette_score[3][k_values.index(k)] = silhouette_score(X, indexes_scratch_haversine)

        # Davies-Bouldin score
        scores_calinski_harabasz_score[0][k_values.index(k)] = calinski_harabasz_score(X, indexes_sklearn)
        scores_calinski_harabasz_score[1][k_values.index(k)] = calinski_harabasz_score(X, indexes_scratch_l1)
        scores_calinski_harabasz_score[2][k_values.index(k)] = calinski_harabasz_score(X, indexes_scratch_l2)
        scores_calinski_harabasz_score[3][k_values.index(k)] = calinski_harabasz_score(X, indexes_scratch_haversine)

        # Davies-Bouldin score
        scores_davies_bouldin_score[0][k_values.index(k)] = davies_bouldin_score(X, indexes_sklearn)
        scores_davies_bouldin_score[1][k_values.index(k)] = davies_bouldin_score(X, indexes_scratch_l1)
        scores_davies_bouldin_score[2][k_values.index(k)] = davies_bouldin_score(X, indexes_scratch_l2)
        scores_davies_bouldin_score[3][k_values.index(k)] = davies_bouldin_score(X, indexes_scratch_haversine)

    # Affichage des résultats
    import matplotlib.pyplot as plt
    import numpy as np
    from utils import current_path

    def plot_scores(scores, title, filename):
        plt.imshow(scores, cmap=plt.get_cmap("viridis"))
        plt.title(title)
        plt.xlabel("k")
        plt.ylabel("Méthode K-means")
        plt.xticks(range(len(k_values)), k_values)
        plt.yticks(range(len(k_means_values)), k_means_values)
        plt.colorbar()
        plt.tight_layout()

        scores_avg = round(
            (np.max(scores) + np.min(scores)) / 2,
            3,
        )
        for (j, i), label in np.ndenumerate(scores):
            plt.text(
                i,
                j,
                round(label, 3) if label < 100 else int(label),
                ha="center",
                va="center",
                color="w" if label < scores_avg else "k",
            )
        
        plt.savefig(f"{current_path}/export/kmeans_{filename}.png")
        plt.close()

    # Silhouette score plot
    plot_scores(
        scores_silhouette_score,
        "Silhouette score",
        "score_silhouette",
    )

    # Calinski-Harabasz score plot
    plot_scores(
        scores_calinski_harabasz_score,
        "Calinski-Harabasz score",
        "score_calinski_harabasz",
    )

    # Davies-Bouldin score plot
    plot_scores(
        scores_davies_bouldin_score,
        "Davies-Bouldin score",
        "score_davies_bouldin",
    )
