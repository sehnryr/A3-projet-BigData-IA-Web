if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import multiprocessing
    import numpy as np

    from f3_classification_3_algos import *
    from f3_repartition import *
    from utils import current_path
    from f1_preparation_data import data

    CPU_COUNT = multiprocessing.cpu_count()
    ALLOWED_CORES = CPU_COUNT - 1 if CPU_COUNT > 1 else 1

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

    # Repartition des données en base d'apprentissage et de test
    data_train, data_test = next(repartition_holdout_sklearn(data))

    # Séparation des features et de la target
    X_train = data_train.drop(columns=["descr_grav"])
    y_train = data_train["descr_grav"]

    X_test = data_test.drop(columns=["descr_grav"])
    y_test = data_test["descr_grav"]

    # Affichage de la courbe d'apprentissage pour chaque algorithme
    from sklearn.model_selection import LearningCurveDisplay
    for clf in [clf_svm_best_params, clf_rf_best_params, clf_mlp_best_params]:
        clf = clf(None, None)
        print(f"Affichage de la courbe d'apprentissage pour le {clf.__class__.__name__}")
        LearningCurveDisplay.from_estimator(
            clf,
            data_train.drop(columns=["descr_grav"]),
            data_train["descr_grav"],
            cv=5,
            n_jobs=ALLOWED_CORES,
            score_type="both",
            std_display_style="fill_between",
            train_sizes=np.linspace(0.1, 1.0, 10),
        )
        plt.title(f"Courbe d'apprentissage pour le {clf.__class__.__name__}")
        plt.xlabel("Taille de l'échantillon d'apprentissage")
        plt.ylabel("Score")
        plt.savefig(f"{current_path}/export/learning_curve_{clf.__class__.__name__.lower()}.png")
        plt.close()

    # Affichage de la matrice de confusion pour chaque algorithme
    from sklearn.metrics import ConfusionMatrixDisplay
    for clf in [clf_svm_best_params, clf_rf_best_params, clf_mlp_best_params]:
        clf = clf(None, None)
        print(f"Affichage de la matrice de confusion pour le {clf.__class__.__name__}")
        ConfusionMatrixDisplay.from_estimator(
            clf,
            data_train.drop(columns=["descr_grav"]),
            data_train["descr_grav"],
            cmap=plt.cm.Blues,
            normalize="true",
        )
        plt.title(f"Matrice de confusion pour le {clf.__class__.__name__}")
        plt.xlabel("Prédiction")
        plt.ylabel("Vraie valeur")
        plt.savefig(f"{current_path}/export/confusion_matrix_{clf.__class__.__name__.lower()}.png")
        plt.close()
