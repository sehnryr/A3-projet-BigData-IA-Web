from sklearn.model_selection import LeaveOneOut, train_test_split

# Répartition des données en base d'apprentissage et base de test via
# l'algorithme holdout (5 fois) avec une implémentation manuelle
def repartition_holdout_scratch(data, train_size=0.8, test_size=0.2):
    for _ in range(5):
        # Copie des données pour ne pas les modifier
        data_copy = data.copy()

        # Base d'apprentissage aléatoire
        train = data_copy.sample(frac=train_size)

        # Base de test = données restantes
        test = data_copy.drop(train.index)

        # Retourner les bases d'apprentissage et de test
        yield train, test

# Répartition des données en base d'apprentissage et base de test via
# l'algorithme leave-one-out avec une implémentation manuelle
def repartition_leave_one_out_scratch(data):
    for i, row in enumerate(data):
        # Copie des données pour ne pas les modifier
        data_copy = data.copy()

        # Base de test = ligne i
        test = data_copy.iloc[[i]]

        # Base d'apprentissage = données restantes
        train = data_copy.drop(test.index)

        # Retourner les bases d'apprentissage et de test
        yield train, test

# Répartition des données en base d'apprentissage et base de test via
# l'algorithme holdout (5 fois) avec la librairie scikit-learn
def repartition_holdout_sklearn(data, train_size=0.8, test_size=0.2):
    for _ in range(5):
        yield train_test_split(data, train_size=train_size, test_size=test_size)

# Répartition des données en base d'apprentissage et base de test via
# l'algorithme leave-one-out avec la librairie scikit-learn
def repartition_leave_one_out_sklearn(data):
    loo = LeaveOneOut()
    for train_index, test_index in loo.split(data):
        yield data.iloc[train_index], data.iloc[test_index]
