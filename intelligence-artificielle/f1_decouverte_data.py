import pandas as pd
import matplotlib.pyplot as plt

from read import data, current_path

if __name__ == "__main__":
    # Les valeurs cible sont les valeurs de gravité d'un accident.
    # Il y a 4 valeurs possibles : 1, 2, 3 et 4.
    # 1 correspond à un accident sans gravité, 2 à un accident léger,
    # 3 à un accident grave et 4 à un accident mortel.
    print("Valeurs cible :", data["descr_grav"].unique())

    # On affiche le nombre d'instances du dataset (nombre de lignes)
    print("Nombre d'instances :", len(data))

    # On affiche le nombre d'instances du dataset pour chaque valeur de gravité
    print(
        "Nombre d'instances pour chaque valeur de gravité :",
        data["descr_grav"].value_counts().to_dict(),
    )

    # On affiche la taille des features (nombre de colonnes)
    print("Nombre de features :", len(data.columns))

    # Graphique du nombre d'instances pour chaque niveau de gravité
    plt.bar(
        ["Sans gravité", "Léger", "Grave", "Mortel"],
        data["descr_grav"].value_counts().values,
    )
    plt.title("Nombre d'instances pour chaque niveau de gravité")
    plt.xlabel("Gravité")
    plt.ylabel("Nombre d'instances")
    plt.savefig(f"{current_path}/export/graph_acc_gravite.png")

    # Conversion de la colonne date en datetime
    data["date"] = pd.to_datetime(data["date"])
