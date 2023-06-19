import os

import pandas as pd

# Recupération du chemin du dossier courant
# (le dossier contenant le fichier main.py)
current_path = os.path.dirname(os.path.realpath(__file__))

# Lecture du fichier CSV exporté depuis le projet Big Data
data = pd.read_csv(f"{current_path}/../big-data/export_IA.csv")

# Suppression manuelle des features inutiles
data = data.drop(
    columns=[
        "Num_Acc",
        "num_veh",
        "id_usa",
        "id_code_insee",
        "code_departement",
        "ville",
    ]
)

# Conversion de la colonne "date" en datetime
data["date"] = pd.to_datetime(data["date"])
