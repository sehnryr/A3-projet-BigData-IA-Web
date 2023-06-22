from f1_preparation_data import data


# On ne conserve que les colonnes qui nous intéressent
data = data[
    [
        "descr_athmo",
        "descr_lum",
        "descr_etat_surf",
        "descr_dispo_secu",
        "descr_grav",
        "code_departement",
    ]
]
