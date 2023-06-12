sample <- read.csv("stat_acc_V3.csv", sep = ";")

#  [1] "Utilisation d'une ceinture de sécurité "
#  [2] "Utilisation d'un casque "
#  [3] "Présence d'une ceinture de sécurité - Utilisation non déterminable"
#  [4] "Présence de ceinture de sécurité non utilisée "
#  [5] "Autre - Non déterminable"
#  [6] "Présence d'un équipement réfléchissant non utilisé"
#  [7] "Présence d'un casque non utilisé "
#  [8] "Utilisation d'un dispositif enfant"
#  [9] "Présence d'un casque - Utilisation non déterminable"
# [10] "Présence dispositif enfant - Utilisation non déterminable"
# [11] "Autre - Utilisé"
# [12] "Utilisation d'un équipement réfléchissant "
# [13] "Autre - Non utilisé"
# [14] "Présence équipement réfléchissant - Utilisation non déterminable"
# [15] "Présence d'un dispositif enfant non utilisé"

valeurs_descr_dispo_secu <- c(
  "Utilisation d'une ceinture de sécurité " = 1,
  "Utilisation d'un casque " = 2,
  "Présence d'une ceinture de sécurité - Utilisation non déterminable" = 3,
  "Présence de ceinture de sécurité non utilisée " = 4,
  "Autre - Non déterminable" = 5,
  "Présence d'un équipement réfléchissant non utilisé" = 6,
  "Présence d'un casque non utilisé " = 7,
  "Utilisation d'un dispositif enfant" = 8,
  "Présence d'un casque - Utilisation non déterminable" = 9,
  "Présence dispositif enfant - Utilisation non déterminable" = 10,
  "Autre - Utilisé" = 11,
  "Utilisation d'un équipement réfléchissant " = 12,
  "Autre - Non utilisé" = 13,
  "Présence équipement réfléchissant - Utilisation non déterminable" = 14,
  "Présence d'un dispositif enfant non utilisé" = 15
)

# Remplacer les valeurs par leurs valeurs numériques attribuées
sample$descr_dispo_secu <- factor(sample$descr_dispo_secu, levels = names(valeurs_descr_dispo_secu), labels = valeurs_descr_dispo_secu)

#  [1] "PL seul > 7,5T"
#  [2] "VU seul 1,5T <= PTAC <= 3,5T avec ou sans remorque "
#  [3] "VL seul"
#  [4] "Autocar"
#  [5] "PL > 3,5T + remorque"
#  [6] "Cyclomoteur <50cm3"
#  [7] "Motocyclette > 125 cm3"
#  [8] "Tracteur routier + semi-remorque"
#  [9] "Tracteur agricole"
# [10] "PL seul 3,5T <PTCA <= 7,5T"
# [11] "Autobus"
# [12] "Scooter > 50 cm3 et <= 125 cm3"
# [13] "Train"
# [14] "Scooter > 125 cm3"
# [15] "Scooter < 50 cm3"
# [16] "Voiturette (Quadricycle à moteur carrossé) (anciennement \"voiturette ou tricycle à moteur\")"
# [17] "Autre véhicule"
# [18] "Bicyclette"
# [19] "Motocyclette > 50 cm3 et <= 125 cm3"
# [20] "Engin spécial"
# [21] "Quad lourd > 50 cm3 (Quadricycle à moteur non carrossé)"
# [22] "Tramway"
# [23] "Tracteur routier seul"
# [24] "Quad léger <= 50 cm3 (Quadricycle à moteur non carrossé)"



valeurs_descr_cat_veh <- c(
  "PL seul > 7,5T" = 1,
  "VU seul 1,5T <= PTAC <= 3,5T avec ou sans remorque " = 2,
  "VL seul" = 3,
  "Autocar" = 4,
  "PL > 3,5T + remorque" = 5,
  "Cyclomoteur <50cm3" = 6,
  "Motocyclette > 125 cm3" = 7,
  "Tracteur routier + semi-remorque" = 8,
  "Tracteur agricole" = 9,
  "PL seul 3,5T <PTCA <= 7,5T" = 10,
  "Autobus" = 11,
  "Scooter > 50 cm3 et <= 125 cm3" = 12,
  "Train" = 13,
  "Scooter > 125 cm3" = 14,
  "Scooter < 50 cm3" = 15,
  "Voiturette (Quadricycle à moteur carrossé) (anciennement \"voiturette ou tricycle à moteur\")" = 16,
  "Autre véhicule" = 17,
  "Bicyclette" = 18,
  "Motocyclette > 50 cm3 et <= 125 cm3" = 19,
  "Engin spécial" = 20,
  "Quad lourd > 50 cm3 (Quadricycle à moteur non carrossé)" = 21,
  "Tramway" = 22,
  "Tracteur routier seul" = 23
)

# Remplacer les valeurs par leurs numéros associés
sample$descr_cat_veh <- factor(sample$descr_cat_veh, levels = names(valeurs_descr_cat_veh), labels = valeurs_descr_cat_veh)

# [1] "Indemne"
# [2] "Tué"
# [3] "Blessé hospitalisé"
# [4] "Blessé léger

sample$descr_grav <- factor(sample$descr_grav, levels = unique(sample$descr_grav))

valeurs_descr_grav <- c(
  "Indemne" = 1,
  "Blessé léger" = 2,
  "Blessé hospitalisé" = 3,
  "Tué" = 4
)

sample$descr_grav <- factor(sample$descr_grav, levels = names(valeurs_descr_grav), labels = valeurs_descr_grav)

# [1] "Hors agglomération"
# [2] "En agglomération"

valeur_descr_agglo <- c(
  "Hors agglomération" = 1,
  "En agglomération" = 2
)

sample$descr_agglo <- factor(sample$descr_agglo, levels = names(valeur_descr_agglo), labels = valeur_descr_agglo)

# [1] "Brouillard – fumée"
# [2] "Neige – grêle"
# [3] "Pluie forte"
# [4] "Normale"
# [5] "Autre"
# [6] "Temps éblouissant"
# [7] "Pluie légère"
# [8] "Temps couvert"
# [9] "Vent fort – tempête"

valeur_descr_athmo <- c(
    "Brouillard – fumée" = 1,
    "Neige – grêle" = 2,
    "Pluie forte" = 3,
    "Normale" = 4,
    "Autre" = 5,
    "Temps éblouissant" = 6,
    "Pluie légère" = 7,
    "Temps couvert" = 8,
    "Vent fort – tempête" = 9
)

sample$descr_athmo <- factor(sample$descr_athmo, levels = names(valeur_descr_athmo), labels = valeur_descr_athmo)

# [1] "Crépuscule ou aube"
# [2] "Plein jour"
# [3] "Nuit sans éclairage public"
# [4] "Nuit avec éclairage public allumé"
# [5] "Nuit avec éclairage public non allumé"

valeur_descr_lum <- c(
    "Crépuscule ou aube" = 1,
    "Plein jour" = 2,
    "Nuit sans éclairage public" = 3,
    "Nuit avec éclairage public allumé" = 4,
    "Nuit avec éclairage public non allumé" = 5
)

sample$descr_lum <- factor(sample$descr_lum, levels = names(valeur_descr_lum), labels = valeur_descr_lum)

# [1] "Verglacée"
# [2] "Enneigée"
# [3] "Mouillée"
# [4] "Normale"
# [5] "Autre"
# [6] "Corps gras – huile"
# [7] "Boue"
# [8] "Flaques"
# [9] "Inondée"

valeurs_descr_etat_surf <- c(
    "Verglacée" = 1,
    "Enneigée" = 2,
    "Mouillée" = 3,
    "Normale" = 4,
    "Autre" = 5,
    "Corps gras – huile" = 6,
    "Boue" = 7,
    "Flaques" = 8,
    "Inondée" = 9
)

sample$descr_etat_surf <- factor(sample$descr_etat_surf, levels = names(valeurs_descr_etat_surf), labels = valeurs_descr_etat_surf)
 
# [1] "Hors intersection"                 "Intersection en X"
# [3] "Giratoire"                         "Intersection en T"
# [5] "Intersection à plus de 4 branches" "Autre intersection"
# [7] "Intersection en Y"                 "Passage à niveau"
# [9] "Place"

valeurs_description_intersection <- c(
    "Hors intersection" = 1,
    "Intersection en X" = 2,
    "Giratoire" = 3,
    "Intersection en T" = 4,
    "Intersection à plus de 4 branches" = 5,
    "Autre intersection" = 6,
    "Intersection en Y" = 7,
    "Passage à niveau" = 8,
    "Place" = 9
)

sample$description_intersection <- factor(sample$description_intersection, levels = names(valeurs_description_intersection), labels = valeurs_description_intersection)

# [1] "Utilisation professionnelle" "Promenade – loisirs"        
# [3] "Domicile – travail"          "Domicile – école"
# [5] "Courses – achats"            "Autre"

valeurs_descr_motif_traj <- c(
    "Utilisation professionnelle" = 1,
    "Promenade – loisirs" = 2,
    "Domicile – travail" = 3,
    "Domicile – école" = 4,
    "Courses – achats" = 5,
    "Autre" = 6
)

sample$descr_motif_traj <- factor(sample$descr_motif_traj, levels = names(valeurs_descr_motif_traj), labels = valeurs_descr_motif_traj)

# [1] "Deux véhicules - Frontale"
# [2] "Deux véhicules – Par l’arrière"
# [3] "Deux véhicules – Par le coté"
# [4] "Trois véhicules et plus – En chaîne"
# [5] "Trois véhicules et plus – Collisions multiples"
# [6] "Autre collision"
# [7] "Sans collision"

valeurs_descr_type_col <- c(
    "Deux véhicules - Frontale" = 1,
    "Deux véhicules – Par l’arrière" = 2,
    "Deux véhicules – Par le coté" = 3,
    "Trois véhicules et plus – En chaîne" = 4,
    "Trois véhicules et plus – Collisions multiples" = 5,
    "Autre collision" = 6,
    "Sans collision" = 7
)

sample$descr_type_col <- factor(sample$descr_type_col, levels = names(valeurs_descr_type_col), labels = valeurs_descr_type_col)

# Écrire les données dans le fichier CSV
write.csv(sample, file = "output.csv")
