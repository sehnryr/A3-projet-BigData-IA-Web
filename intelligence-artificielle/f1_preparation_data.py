import pandas as pd

from utils import current_path
from f1_lecture import data


# Suppression manuelle des features inutiles
data = data.drop(
    columns=[
        "Num_Acc",
        "num_veh",
        "id_usa",
        "id_code_insee",
        "ville",
    ]
)

# Remplacement des valeurs de departement 2A et 2B par 100 et 101
data["code_departement"] = data["code_departement"].replace({"2A": 100, "2B": 101})

# Conversion de la colonne code_departement en int
data["code_departement"] = data["code_departement"].astype(int)

# Conversion de la colonne "date" en datetime
data["date"] = pd.to_datetime(data["date"])
