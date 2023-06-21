import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import json
# Récupérer les arguments de la ligne de commande
code_region = sys.argv[1]
descr_athmo = sys.argv[2]
descr_lum = sys.argv[3]
descr_etat_surf = sys.argv[4]
descr_dispo_secu = sys.argv[5]
csv_filename = sys.argv[6]

# Charger les données
data = pd.read_csv(csv_filename)

data.dropna(inplace=True)

selected_columns = ["code_region", "descr_athmo", "descr_lum", "descr_etat_surf", "descr_dispo_secu"]
X = data[selected_columns]
y = data['descr_grav']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) # 20% des données pour le test

# Entraîner le modèle KNN
model = KNeighborsClassifier(n_neighbors=15)
model.fit(X_train, y_train)

# Préparer les données de l'accident donné en entrée
new_accident = pd.DataFrame([[code_region, descr_athmo, descr_lum, descr_etat_surf, descr_dispo_secu]], columns=selected_columns)

y_pred = model.predict(new_accident)

print("Prédiction de la grabité de l'accident:", y_pred)

# Évaluer les performances du modèle
y_pred_test = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred_test)
print("Précision du modèle:", accuracy)

# Écriture du résultat au format JSON dans un fichier
with open('result.json', 'w') as json_file:
    json.dump(y_pred.tolist(), json_file)

print("Résultat enregistré dans le fichier 'result.json'.")
