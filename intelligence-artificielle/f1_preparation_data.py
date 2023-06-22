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
        "code_departement",
        "ville",
    ]
)

# Conversion de la colonne "date" en datetime
data["date"] = pd.to_datetime(data["date"])
