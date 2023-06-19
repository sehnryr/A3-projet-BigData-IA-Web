import os

import pandas as pd

# Recupération du chemin du dossier courant
# (le dossier contenant le fichier main.py)
current_path = os.path.dirname(os.path.realpath(__file__))

# Lecture du fichier CSV exporté depuis le projet Big Data
data = pd.read_csv(f"{current_path}/../big-data/export_IA.csv")
