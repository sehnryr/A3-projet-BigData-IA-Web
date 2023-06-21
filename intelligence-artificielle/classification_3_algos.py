from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from statistics import mean
import joblib
import multiprocessing


CPU_COUNT = multiprocessing.cpu_count()
ALLOWED_CORES = CPU_COUNT - 1 if CPU_COUNT > 1 else 1


clf_best_params = {
    "svm": {"C": 10, "gamma": "auto", "kernel": "rbf"},
    "rf": {"max_depth": 5, "max_features": None, "n_estimators": 300},
    "mlp": {
        "activation": "logistic",
        "hidden_layer_sizes": (100, 100, 100),
        "solver": "adam",
    },
}


def svm_grid_search(X_train, y_train) -> GridSearchCV:
    """Retourne les meilleurs paramètres pour le classifieur SVM"""
    clf_svm = SVC()
    param_grid_svm = {
        "C": [0.1, 1, 10],
        "gamma": ["scale", "auto", 1, 0.1, 0.01],
        "kernel": ["poly", "rbf", "sigmoid"],
    }
    grid_svm = GridSearchCV(
        clf_svm,
        param_grid_svm,
        verbose=2,
        cv=3,
        n_jobs=ALLOWED_CORES,
    )
    grid_svm.fit(X_train, y_train)

    # grid_svm.best_params_ {'C': 1, 'gamma': 1, 'kernel': 'rbf'}
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
        cv=3,
        n_jobs=ALLOWED_CORES,
    )
    grid_rf.fit(X_train, y_train)

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
        cv=3,
        n_jobs=ALLOWED_CORES,
    )
    grid_mlp.fit(X_train, y_train)

    return grid_mlp


def clf_svm_best_params(X_train, y_train) -> SVC:
    """Retourne le classifieur SVM avec les meilleurs paramètres"""
    if clf_best_params["svm"]:
        return SVC(**clf_best_params["svm"])

    best_params = svm_grid_search(X_train, y_train).best_params_
    clf_best_params["svm"] = best_params
    return SVC(**best_params)


def clf_rf_best_params(X_train, y_train) -> RandomForestClassifier:
    """Retourne le classifieur Random Forest avec les meilleurs paramètres"""
    if clf_best_params["rf"]:
        return RandomForestClassifier(**clf_best_params["rf"])

    best_params = rf_grid_search(X_train, y_train).best_params_
    clf_best_params["rf"] = best_params
    return RandomForestClassifier(**best_params)


def clf_mlp_best_params(X_train, y_train) -> MLPClassifier:
    """Retourne le classifieur MLP avec les meilleurs paramètres"""
    if clf_best_params["mlp"]:
        return MLPClassifier(**clf_best_params["mlp"])

    best_params = mlp_grid_search(X_train, y_train).best_params_
    clf_best_params["mlp"] = best_params
    return MLPClassifier(**best_params)


if __name__ == "__main__":
    from read import data
    from repartition import *
    from time import time

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

    scores = {
        "svm": [],
        "rf": [],
        "mlp": [],
    }

    # Compte du nombre de folds
    i = 0
    time_start = time()

    for data_train, data_test in repartition_holdout_sklearn(data):
        time_end = time()
        print(f"Fold {i + 1} {round(time_end - time_start, 3)}s", end="\r")
        time_start = time_end
        i += 1

        # Séparation des features et de la target
        X_train = data_train.drop(columns=["descr_grav"])
        y_train = data_train["descr_grav"]

        X_test = data_test.drop(columns=["descr_grav"])
        y_test = data_test["descr_grav"]

        clf_svm = clf_svm_best_params(X_train, y_train)
        clf_svm.fit(X_train, y_train)
        scores["svm"].append(accuracy_score(y_test, clf_svm.predict(X_test)))

        clf_rf = clf_rf_best_params(X_train, y_train)
        clf_rf.fit(X_train, y_train)
        scores["rf"].append(accuracy_score(y_test, clf_rf.predict(X_test)))

        clf_mlp = clf_mlp_best_params(X_train, y_train)
        clf_mlp.fit(X_train, y_train)
        scores["mlp"].append(accuracy_score(y_test, clf_mlp.predict(X_test)))

    print(clf_best_params)

    print("SVM:", round(mean(scores["svm"]), 4))
    print("RF:", round(mean(scores["rf"]), 4))
    print("MLP:", round(mean(scores["mlp"]), 4))

    # # Séparation des données en train et test
    # data_train, data_test = next(repartition_holdout_sklearn(data))

    # # Séparation des features et de la target
    # X_train = data_train.drop(columns=["descr_grav"])
    # y_train = data_train["descr_grav"]

    # X_test = data_test.drop(columns=["descr_grav"])
    # y_test = data_test["descr_grav"]

    # clf_svm_best_params(X_train, y_train)
    # clf_rf_best_params(X_train, y_train)
    # clf_mlp_best_params(X_train, y_train)

    # print(clf_best_params)
