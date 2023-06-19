import os

import pandas as pd

if __name__ == "__main__":
    # Recupération du chemin du dossier courant
    # (le dossier contenant le fichier main.py)
    current_path = os.path.dirname(os.path.realpath(__file__))

    # Lecture du fichier CSV exporté depuis le projet Big Data
    data = pd.read_csv(f"{current_path}/export_IA.csv")

    # Les valeurs cible sont les valeurs de gravité d'un accident.
    # Il y a 4 valeurs possibles : 1, 2, 3 et 4.
    # 1 correspond à un accident sans gravité, 2 à un accident léger,
    # 3 à un accident grave et 4 à un accident mortel.
    print("Valeurs cible :", data["gravite"].unique())

    # On affiche le nombre d'instances du dataset (nombre de lignes)
    print("Nombre d'instances :", len(data))

    # On affiche le nombre d'instances du dataset pour chaque valeur de gravité
    print(
        "Nombre d'instances pour chaque valeur de gravité :",
        data["gravite"].value_counts().to_dict(),
    )

    # On affiche la taille des features (nombre de colonnes)
    print("Nombre de features :", len(data.columns))
