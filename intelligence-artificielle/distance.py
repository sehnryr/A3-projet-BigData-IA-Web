import numpy as np


# Manhattan distance between two points x and y (sum of absolute values)
# https://en.wikipedia.org/wiki/Taxicab_geometry
def manhattan_distance(x, y):
    return np.sum(np.abs(x - y))


# Euclidean distance between two points x and y (square root of sum of squares)
# https://en.wikipedia.org/wiki/Euclidean_distance
def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y) ** 2))


# Haversine distance between two points x and y (great-circle distance)
# https://en.wikipedia.org/wiki/Haversine_formula
def haversine_distance(x, y):
    # Convert to radians
    x = np.radians(x)
    y = np.radians(y)

    # Haversine formula
    x_lat, x_lon = x[:, 0], x[:, 1]
    y_lat, y_lon = y[:, 0], y[:, 1]
    dlon = y_lon - x_lon
    dlat = y_lat - x_lat
    a = np.sin(dlat / 2) ** 2 + np.cos(x_lat) * np.cos(y_lat) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371  # Radius of earth in kilometers
    return c * r
