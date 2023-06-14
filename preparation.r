# Description: This script prepares the data for the analysis.

# Load the read.r script to read the data
source("read.r")

# Load the libraries
suppressPackageStartupMessages(library(dplyr)) # for data manipulation
suppressPackageStartupMessages(library(ggplot2)) # for plotting graphs
suppressPackageStartupMessages(library(ggmap)) # for plotting maps
suppressPackageStartupMessages(library(mapproj)) # for scaling maps

# Convert "Null" values to NA
data[data == "NULL"] <- NA

# Convert the an_nais column to numeric
# and replace the NA values with the median of the an_nais column
data$an_nais <- as.numeric(data$an_nais)
data$an_nais[is.na(data$an_nais)] <- median(data$an_nais, na.rm = TRUE)

# Convert the age column to numeric
# and replace the NA values with the median of the age column
data$age <- as.numeric(data$age)
data$age[is.na(data$age)] <- median(data$age, na.rm = TRUE)

# Convert the place column to numeric
# and replace the NA values with the median of the place column
data$place <- as.numeric(data$place)
data$place[is.na(data$place)] <- median(data$place, na.rm = TRUE)

# Replace the latitude and longitude values with the values of laposte_hexasmal.csv file
laposte_hexasmal <- read.csv("datasets/laposte_hexasmal.csv", header = TRUE, sep = ";")
# Split coordonnees_geographiques column into latitude and longitude columns
laposte_hexasmal$latitude <- as.numeric(sapply(strsplit(
  as.character(laposte_hexasmal$coordonnees_geographiques), ","), head, 1))
laposte_hexasmal$longitude <- as.numeric(sapply(strsplit(
  as.character(laposte_hexasmal$coordonnees_geographiques), ","), tail, 1))

data$latitude <- laposte_hexasmal$latitude[
  match(data$id_code_insee, laposte_hexasmal$code_commune_insee)]
data$longitude <- laposte_hexasmal$longitude[
  match(data$id_code_insee, laposte_hexasmal$code_commune_insee)]

# Convert columns to numeric
data$Num_Acc <- as.numeric(data$Num_Acc)
data$id_usa <- as.numeric(data$id_usa)
data$latitude <- as.numeric(data$latitude)
data$longitude <- as.numeric(data$longitude)

# Convert the date column to a date format
data$date <- strptime(data$date, format = "%Y-%m-%d %H:%M:%S")

# Add a month column to the data frame
data$month <- as.integer(format(data$date, "%m"))

# Add a week column to the data frame
data$week <- as.integer(format(data$date, "%W"))

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
data$descr_dispo_secu <- factor(
  data$descr_dispo_secu,
  levels = names(valeurs_descr_dispo_secu),
  labels = valeurs_descr_dispo_secu
)

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
data$descr_cat_veh <- factor(
  data$descr_cat_veh,
  levels = names(valeurs_descr_cat_veh),
  labels = valeurs_descr_cat_veh
)

# [1] "Indemne"
# [2] "Tué"
# [3] "Blessé hospitalisé"
# [4] "Blessé léger

data$descr_grav <- factor(
  data$descr_grav,
  levels = unique(data$descr_grav)
)

valeurs_descr_grav <- c(
  "Indemne" = 1,
  "Blessé léger" = 2,
  "Blessé hospitalisé" = 3,
  "Tué" = 4
)

data$descr_grav <- factor(
  data$descr_grav,
  levels = names(valeurs_descr_grav),
  labels = valeurs_descr_grav
)

# [1] "Hors agglomération"
# [2] "En agglomération"

valeur_descr_agglo <- c(
  "Hors agglomération" = 1,
  "En agglomération" = 2
)

data$descr_agglo <- factor(
  data$descr_agglo,
  levels = names(valeur_descr_agglo),
  labels = valeur_descr_agglo
)

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

data$descr_athmo <- factor(
  data$descr_athmo,
  levels = names(valeur_descr_athmo),
  labels = valeur_descr_athmo
)

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

data$descr_lum <- factor(
  data$descr_lum,
  levels = names(valeur_descr_lum),
  labels = valeur_descr_lum
)

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

data$descr_etat_surf <- factor(
  data$descr_etat_surf,
  levels = names(valeurs_descr_etat_surf),
  labels = valeurs_descr_etat_surf
)
 
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

data$description_intersection <- factor(
  data$description_intersection,
  levels = names(valeurs_description_intersection),
  labels = valeurs_description_intersection
)

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

data$descr_motif_traj <- factor(
  data$descr_motif_traj,
  levels = names(valeurs_descr_motif_traj),
  labels = valeurs_descr_motif_traj
)

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

data$descr_type_col <- factor(
  data$descr_type_col,
  levels = names(valeurs_descr_type_col),
  labels = valeurs_descr_type_col
)

# Retrieve the department names with the corresponding code because the map_data
# function does not provide the department codes
departements <- read.csv("datasets/v_departement_2023.csv", header = TRUE, sep = ",")
departements$NCC <- gsub(" ", "", departements$NCC)

# Add departement code and region code to data
data$code_departement <- substr(data$id_code_insee, 1, 2)
data$code_region <- departements$REG[match(data$code_departement, departements$DEP)]
