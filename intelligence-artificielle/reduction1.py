import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from read import data

# Calculer la matrice de corrélation entre les attributs
corr_matrix = data.corr()
print(corr_matrix)

# Définir une valeur seuil de corrélation à partir de laquelle une paire d'attributs est considérée comme fortement corrélée
seuil_correlation = 0.8

paire = np.where(np.abs(corr_matrix) > seuil_correlation)
paire = list(zip(paire[0], paire[1]))

forte_correlation = []
for x, y in paire:
    if x != y and x < y:
        forte_correlation.append((corr_matrix.index[x], corr_matrix.columns[y]))

# Afficher les paires d'attributs fortement corrélées
for pair in forte_correlation:
    # On supprime la variable la moins corrélée avec la gravité
    corr_gravite = abs(corr_matrix.loc[pair[0], 'descr_grav']), abs(corr_matrix.loc[pair[1], 'descr_grav'])
    if corr_gravite[0] < corr_gravite[1]:
        variable_suppr = pair[0]
        print(pair[0])
    else:
        variable_suppr = pair[1]
        print(pair[1])

# Supprimer les caractéristiques sélectionnées du DataFrame
data_reduced = data.drop(columns=variable_suppr)

# Afficher toutes les colonnes de data_reduced
print(data_reduced.columns)

# Calculer le pourcentage de réduction
pourcentage_reduction = (1 - len(data_reduced.columns) / len(data.columns)) * 100

# Afficher les colonnes avant et après la réduction
print("Colonnes avant la réduction :")
print(data.columns)
print("\nColonnes après la réduction :")
print(data_reduced.columns)

# Afficher les graphiques de visualisation avant et après la réduction
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.heatmap(data.corr(), cmap='viridis', vmin=-1, vmax=1)
plt.title('Matrice de corrélation avant la réduction')

plt.subplot(1, 2, 2)
sns.heatmap(data_reduced.corr(), cmap='viridis', vmin=-1, vmax=1)
plt.title('Matrice de corrélation après la réduction')

plt.tight_layout()
plt.show()

# Afficher le pourcentage de réduction
print(f"Pourcentage de réduction : {pourcentage_reduction}%")