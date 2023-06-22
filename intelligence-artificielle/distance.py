import numpy as np


def hamming_distance(x, y):
    """
    Distance Hamming entre deux points x et y
    (nombre de positions où les symboles correspondants sont différents)
    https://en.wikipedia.org/wiki/Hamming_distance
    """
    return np.sum(x != y, axis=1)


def manhattan_distance(x, y):
    """
    Distance Manhattan entre deux points x et y
    (somme des valeurs absolues)
    https://en.wikipedia.org/wiki/Taxicab_geometry
    """
    return np.sum(np.abs(x - y), axis=1)


def euclidean_distance(x, y):
    """
    Distance Euclidienne entre deux points x et y
    (racine carrée de la somme des carrés)
    https://en.wikipedia.org/wiki/Euclidean_distance
    """
    return np.sqrt(np.sum((x - y) ** 2, axis=1))


def minkowski_distance(x, y, p=2):
    """
    Distance Minkowski entre deux points x et y
    (généralisation des distances Euclidienne et Manhattan)
    https://en.wikipedia.org/wiki/Minkowski_distance
    """
    return np.sum(np.abs(x - y) ** p, axis=1) ** (1 / p)


def haversine_distance(x, y):
    """
    Distance Haversine entre deux points x et y
    (distance sur la surface d'une sphère)
    https://en.wikipedia.org/wiki/Haversine_formula
    """
    # Conversion en radians
    x = np.radians(x)
    y = np.radians(y)

    # Extraction des latitudes et longitudes
    x_lat, x_lon = x[0], x[1]
    y_lat, y_lon = y[:, 0], y[:, 1]

    # Calcul des distances
    dlon = y_lon - x_lon
    dlat = y_lat - x_lat

    # Application de la formule de Haversine
    a = np.sin(dlat / 2) ** 2 + np.cos(x_lat) * np.cos(y_lat) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371  # Rayon de la Terre en km
    return c * r
