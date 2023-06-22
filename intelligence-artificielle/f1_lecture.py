import pandas as pd

from utils import current_path

# Lecture du fichier CSV exporté depuis le projet Big Data
data = pd.read_csv(f"{current_path}/../big-data/export_IA.csv")
