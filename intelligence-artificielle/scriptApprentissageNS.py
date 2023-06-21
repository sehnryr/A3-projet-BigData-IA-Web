import sys
import numpy as np
from sklearn.cluster import KMeans
import json

# Charger les coordonnées de latitude et de longitude de l'accident à partir des arguments en ligne de commande
latitude = float(sys.argv[1])
longitude = float(sys.argv[2])

# Calculer le nombre de clusters
num_clusters = (len(sys.argv) - 3) // 2

# Charger les coordonnées des centroides des clusters à partir des arguments en ligne de commande
centroids = []
for i in range(num_clusters):
    centroid_lat = float(sys.argv[i*2 + 3])
    centroid_lon = float(sys.argv[i*2 + 4])
    centroids.append([centroid_lat, centroid_lon])

# Effectuer le clustering en utilisant l'algorithme K-means
kmeans = KMeans(n_clusters=num_clusters, init=np.array(centroids))
kmeans.fit(np.array(centroids)) 

# Prédire le cluster d'appartenance de l'accident
cluster_label = kmeans.predict([[latitude, longitude]])

# Conversion du résultat en format JSON
result = {'cluster_label': cluster_label.tolist()}

# Écriture du résultat au format JSON dans un fichier
with open('result.json', 'w') as json_file:
    json.dump(result, json_file)

print("Résultat enregistré dans le fichier 'result.json'.")
