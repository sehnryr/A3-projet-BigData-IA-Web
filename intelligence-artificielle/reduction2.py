import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Charger le fichier CSV dans un DataFrame pandas
data = pd.read_csv("export_IA.csv")

# Supprimer toutes les lignes contenant des valeurs NaN
data.dropna(inplace=True)

# Sélectionner les colonnes pertinentes pour l'analyse PCA
features = data.columns.tolist()
X = data[features]

# Normaliser les données
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Calculer le nombre initial de variables
num_features_initial = len(features)

# Appliquer l'analyse PCA avec 2 composantes principales
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Créer un DataFrame avec les composantes principales
result = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])

# Afficher un graphique du PCA
plt.figure(figsize=(10, 6))
plt.scatter(result['PC1'], result['PC2'])
plt.xlabel('Composante Principale 1')
plt.ylabel('Composante Principale 2')
plt.title('Analyse en Composantes Principales (PCA)')
plt.grid(True)
plt.show()