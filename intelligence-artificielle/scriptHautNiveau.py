import sys
import json

from f3_classification_3_algos import *

SVM_GRID_SEARCH_MODEL_PATH = "svm_grid_search_model.pkl"  # Chemin du modèle sauvegardé

code_region = sys.argv[1]
descr_athmo = sys.argv[2]
descr_lum = sys.argv[3]
descr_etat_surf = sys.argv[4]
descr_dispo_secu = sys.argv[5]
methode_classification = sys.argv[6]

if methode_classification == "svm":
    # Utiliser la méthode SVM pour la classification
    clf = clf_svm_best_params(None, None)
    # Prédire la gravité de l'accident
    gravite = clf.predict([[code_region, descr_athmo, descr_lum, descr_etat_surf, descr_dispo_secu]])
    # Créer le dictionnaire JSON de sortie
    result = {"Gravité": gravite}

if methode_classification == "r":
    # Utiliser la méthode SVM pour la classification
    clf = clf_rf_best_params(None, None)
    # Prédire la gravité de l'accident
    gravite = clf.predict([[code_region, descr_athmo, descr_lum, descr_etat_surf, descr_dispo_secu]])
    # Créer le dictionnaire JSON de sortie
    result = {"Gravité": gravite}
    
if methode_classification == "mlp":
    # Utiliser la méthode SVM pour la classification
    clf = clf_mlp_best_params(None, None)
    # Prédire la gravité de l'accident
    gravite = clf.predict([[code_region, descr_athmo, descr_lum, descr_etat_surf, descr_dispo_secu]])
    # Créer le dictionnaire JSON de sortie
    result = {"Gravité": gravite}
    
# Écriture du résultat au format JSON dans un fichier
with open('result.json', 'w') as json_file:
    json.dump(result, json_file)

print("Résultat enregistré dans le fichier 'result.json'.")



