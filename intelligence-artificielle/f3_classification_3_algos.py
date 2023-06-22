import os
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from statistics import mean
import joblib
import multiprocessing

from utils import current_path


CPU_COUNT = multiprocessing.cpu_count()
ALLOWED_CORES = CPU_COUNT - 1 if CPU_COUNT > 1 else 1

SVM_GRID_SEARCH_MODEL_PATH = f"{current_path}/models/svm_grid_search.joblib"
RF_GRID_SEARCH_MODEL_PATH = f"{current_path}/models/rf_grid_search.joblib"
MLP_GRID_SEARCH_MODEL_PATH = f"{current_path}/models/mlp_grid_search.joblib"


def svm_grid_search(X_train, y_train) -> GridSearchCV:
    """Retourne les meilleurs paramètres pour le classifieur SVM"""
    clf_svm = SVC(probability=True)
    param_grid_svm = {
        "C": [1, 3, 5, 7, 11],
        "gamma": ["auto", 1, 0.5, 0.1, 0.05],
        "kernel": ["rbf", "sigmoid"],
    }
    grid_svm = GridSearchCV(
        clf_svm,
        param_grid_svm,
        verbose=2,
        cv=5,
        n_jobs=ALLOWED_CORES,
    )
    grid_svm.fit(X_train, y_train)

    # Sauvegarde du modèle pour éviter de le recalculer à chaque fois
    if not os.path.exists(f"{current_path}/models"):
        os.mkdir(f"{current_path}/models")
    joblib.dump(grid_svm, SVM_GRID_SEARCH_MODEL_PATH)

    return grid_svm


def rf_grid_search(X_train, y_train) -> GridSearchCV:
    """Retourne les meilleurs paramètres pour le classifieur Random Forest"""
    clf_rf = RandomForestClassifier()
    param_grid_rf = {
        "n_estimators": [50, 100, 150, 200, 250, 300, 350, 400],
        "max_depth": [None, 5, 10, 15, 20, 25, 30, 35, 40],
        "max_features": ["sqrt", "log2", None],
    }
    grid_rf = GridSearchCV(
        clf_rf,
        param_grid_rf,
        verbose=2,
        cv=5,
        n_jobs=ALLOWED_CORES,
    )
    grid_rf.fit(X_train, y_train)

    # Sauvegarde du modèle pour éviter de le recalculer à chaque fois
    if not os.path.exists(f"{current_path}/models"):
        os.mkdir(f"{current_path}/models")
    joblib.dump(grid_rf, RF_GRID_SEARCH_MODEL_PATH)

    return grid_rf


def mlp_grid_search(X_train, y_train) -> GridSearchCV:
    """Retourne les meilleurs paramètres pour le classifieur MLP"""
    clf_mlp = MLPClassifier()
    param_grid_mlp = {
        "hidden_layer_sizes": [(100,), (100, 100), (100, 100, 100)],
        "activation": ["identity", "logistic", "tanh", "relu"],
        "solver": ["lbfgs", "sgd", "adam"],
    }
    grid_mlp = GridSearchCV(
        clf_mlp,
        param_grid_mlp,
        verbose=2,
        cv=5,
        n_jobs=ALLOWED_CORES,
    )
    grid_mlp.fit(X_train, y_train)

    # Sauvegarde du modèle pour éviter de le recalculer à chaque fois
    if not os.path.exists(f"{current_path}/models"):
        os.mkdir(f"{current_path}/models")
    joblib.dump(grid_mlp, MLP_GRID_SEARCH_MODEL_PATH)

    return grid_mlp


def clf_svm_best_params(X_train, y_train) -> SVC:
    """Retourne le classifieur SVM avec les meilleurs paramètres"""
    # On cherche si le modèle a déjà été calculé
    if os.path.exists(SVM_GRID_SEARCH_MODEL_PATH):
        # Chargement du modèle
        model = joblib.load(SVM_GRID_SEARCH_MODEL_PATH)
        return model.best_estimator_

    # Sinon, on le calcule
    return svm_grid_search(X_train, y_train).best_estimator_


def clf_rf_best_params(X_train, y_train) -> RandomForestClassifier:
    """Retourne le classifieur Random Forest avec les meilleurs paramètres"""
    # On cherche si le modèle a déjà été calculé
    if os.path.exists(RF_GRID_SEARCH_MODEL_PATH):
        # Chargement du modèle
        model = joblib.load(RF_GRID_SEARCH_MODEL_PATH)
        return model.best_estimator_

    # Sinon, on le calcule
    return rf_grid_search(X_train, y_train).best_estimator_


def clf_mlp_best_params(X_train, y_train) -> MLPClassifier:
    """Retourne le classifieur MLP avec les meilleurs paramètres"""
    # On cherche si le modèle a déjà été calculé
    if os.path.exists(MLP_GRID_SEARCH_MODEL_PATH):
        # Chargement du modèle
        model = joblib.load(MLP_GRID_SEARCH_MODEL_PATH)
        return model.best_estimator_

    # Sinon, on le calcule
    return mlp_grid_search(X_train, y_train).best_estimator_


# if __name__ == "__main__":
#     from read import data
#     from f3_repartition import *
#     from time import time

#     data = data[
#         [
#             "latitude",
#             "longitude",
#             "descr_athmo",
#             "descr_lum",
#             "descr_etat_surf",
#             "descr_dispo_secu",
#             "descr_grav",
#         ]
#     ]

#     # Reduction de la taille de data en prenant 10% de chaque classe
#     # pour chaque label
#     data = data.groupby("descr_grav").apply(lambda x: x.sample(frac=0.1))

#     scores = {
#         "svm": [],
#         "rf": [],
#         "mlp": [],
#     }

#     # Compte du nombre de folds
#     i = 0
#     time_start = time()

#     for data_train, data_test in repartition_holdout_sklearn(data):
#         time_end = time()
#         print(f"Fold {i + 1} {round(time_end - time_start, 3)}s", end="\r")
#         time_start = time_end
#         i += 1

#         # Séparation des features et de la target
#         X_train = data_train.drop(columns=["descr_grav"])
#         y_train = data_train["descr_grav"]

#         X_test = data_test.drop(columns=["descr_grav"])
#         y_test = data_test["descr_grav"]

#         clf_svm = clf_svm_best_params(X_train, y_train)
#         clf_svm.fit(X_train, y_train)
#         scores["svm"].append(accuracy_score(y_test, clf_svm.predict(X_test)))

#         clf_rf = clf_rf_best_params(X_train, y_train)
#         clf_rf.fit(X_train, y_train)
#         scores["rf"].append(accuracy_score(y_test, clf_rf.predict(X_test)))

#         clf_mlp = clf_mlp_best_params(X_train, y_train)
#         clf_mlp.fit(X_train, y_train)
#         scores["mlp"].append(accuracy_score(y_test, clf_mlp.predict(X_test)))

#     print("SVM:", round(mean(scores["svm"]), 4))
#     print("RF:", round(mean(scores["rf"]), 4))
#     print("MLP:", round(mean(scores["mlp"]), 4))

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    # Recuperation des modèles des classifieurs avec les meilleurs paramètres
    gs_svm = joblib.load(SVM_GRID_SEARCH_MODEL_PATH)
    gs_rf = joblib.load(RF_GRID_SEARCH_MODEL_PATH)
    gs_mlp = joblib.load(MLP_GRID_SEARCH_MODEL_PATH)

    # Recuperation des paramètres donnés aux gridsearch
    params_svm = gs_svm.cv_results_["params"]
    params_rf = gs_rm.cv_results_["params"]
    params_mlp = gs_mlp.cv_results_["params"]

    # On recupere les scores moyens pour les paramètres "C" et "gamma" du SVM
    grid_param_C = np.unique([d["C"] for d in params_svm])
    grid_param_gamma = np.unique([d["gamma"] for d in params_svm])
    score_avg = gs_svm.cv_results_["mean_test_score"]
    score_avg = score_avg[gs_svm.cv_results_["param_kernel"] == "rbf"]
    score_avg = np.array(score_avg).reshape(
        len(grid_param_C),
        len(grid_param_gamma),
    )

    plt.imshow(score_avg, cmap=plt.get_cmap("viridis"))
    plt.title("SVM\nscore moyen avec un kernel rbf")
    plt.xlabel("gamma")
    plt.ylabel("C")
    plt.xticks(np.arange(len(grid_param_gamma)), grid_param_gamma)
    plt.yticks(np.arange(len(grid_param_C)), grid_param_C)
    plt.colorbar()

    scores_avg = round(np.mean(score_avg), 3)
    for (j, i), label in np.ndenumerate(score_avg):
        plt.text(
            i,
            j,
            round(label, 3),
            ha="center",
            va="center",
            color="white" if label < scores_avg else "black",
        )

    plt.show()
    plt.close()

# if __name__ == "__main__":
#     from read import data
#     from f3_repartition import *

#     data = data[
#         [
#             "latitude",
#             "longitude",
#             "descr_athmo",
#             "descr_lum",
#             "descr_etat_surf",
#             "descr_dispo_secu",
#             "descr_grav",
#         ]
#     ]

#     # Reduction de la taille de data en prenant 10% de chaque classe
#     # pour chaque label
#     data = data.groupby("descr_grav").apply(lambda x: x.sample(frac=0.1))

#     data_train, _ = next(repartition_holdout_sklearn(data))

#     # Séparation des features et de la target
#     X_train = data_train.drop(columns=["descr_grav"])
#     y_train = data_train["descr_grav"]

#     svm_grid_search(X_train, y_train)
