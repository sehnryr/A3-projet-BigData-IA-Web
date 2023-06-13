# Description: This script is used to visualise the data

# Load the preparation.r script to prepare the data
source("preparation.r")

# Load the libraries
suppressPackageStartupMessages(library(dplyr)) # for data manipulation
suppressPackageStartupMessages(library(ggplot2)) # for plotting graphs
suppressPackageStartupMessages(library(ggmap)) # for plotting maps
suppressPackageStartupMessages(library(mapproj)) # for scaling maps

# Number of accidents per atmospheric condition
data_atmospheric_condition <- data %>%
  group_by(descr_athmo) %>%
  summarise(count = n())

ggplot(data_atmospheric_condition, aes(x = descr_athmo, y = count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_text(aes(label = count), vjust = -0.3, size = 3.5) +
  labs(title = "Accidents by atmospheric condition", x = "Atmospheric condition", y = "Count") +
  theme(plot.title = element_text(hjust = 0.5)) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))

# Number of accidents per surface condition
data_surface_condition <- data %>%
  group_by(descr_etat_surf) %>%
  summarise(count = n())

ggplot(data_surface_condition, aes(x = descr_etat_surf, y = count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_text(aes(label = count), vjust = -0.3, size = 3.5) +
  labs(title = "Accidents by surface condition", x = "Surface condition", y = "Count") +
  theme(plot.title = element_text(hjust = 0.5)) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))

# Number of accidents per gravity of the accident
data_gravity <- data %>%
  group_by(descr_grav) %>%
  summarise(count = n())

ggplot(data_gravity, aes(x = descr_grav, y = count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_text(aes(label = count), vjust = -0.3, size = 3.5) +
  labs(title = "Accidents by gravity", x = "Gravity", y = "Count") +
  theme(plot.title = element_text(hjust = 0.5)) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))

# Number of accidents per hour
data$hour <- as.numeric(format(data$date, "%H"))
data_hour <- data %>%
  group_by(hour) %>%
  summarise(count = n())

ggplot(data_hour, aes(x = hour, y = count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_text(aes(label = count), vjust = -0.3, size = 3.5) +
  labs(title = "Accidents by hour", x = "Hour", y = "Count") +
  theme(plot.title = element_text(hjust = 0.5)) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))

# Number of accidents per city
data_city <- data %>%
  group_by(ville) %>%
  summarise(count = n())

# Get the 20 cities with the most accidents
data_city <- data_city[order(-data_city$count),]
data_city <- data_city[1:20,]

ggplot(data_city, aes(x = reorder(ville, -count), y = count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_text(aes(label = count), vjust = -0.3, size = 3.5) +
  labs(title = "Accidents by city", x = "City", y = "Count") +
  theme(plot.title = element_text(hjust = 0.5)) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))

data$age <- 2009 - as.integer(data$an_nais)
#crée un histogramme à partir en fonction du nombre d'accident par tranche d'age
hist(data$age, main = "Histogramme du nombre d'accident par année de naissance", xlab = "Année de naissance", ylab = "Nombre d'accidents")

accidentparmois <- list(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Calcul du nombre d'accidents par mois
for (i in 1:12) {
  AccidentparMois <- data[data$month == i,]
  nbAccident <- nrow(AccidentparMois)
  accidentparmois[[i]] <- nbAccident
}

barplot(unlist(accidentparmois), 
        names.arg = c("Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Août", "Sep", "Oct", "Nov", "Déc"),
        xlab = "Mois",
        ylab = "Nombre d'accidents",
        main = "Nombre d'accidents par mois")

# Retrieve the department names with the corresponding code because the map_data
# function does not provide the department codes
departements <- read.csv("datasets/v_departement_2023.csv", header = TRUE, sep = ",")
departements$NCC <- gsub(" ", "", departements$NCC)

# Number of accidents per department
data$code_departement <- substr(data$id_code_insee, 1, 2)
data_departement <- data %>%
  group_by(code_departement) %>%
  summarise(count = n())

# Merge the data with the department names
france <- map_data("france")
france$region <- gsub(" ", "", gsub("-", "", toupper(france$region)))
france$code_departement <- departements$DEP[match(france$region, departements$NCC)]
france$count <- data_departement$count[match(france$code_departement, data_departement$code_departement)]

# Plot the map
ggplot(france, aes(x=long, y=lat, group=group, fill=count)) +
  labs(title = "Accidents by department", x = "Longitude", y = "Latitude") +
  geom_polygon(colour="black") +
  coord_map("mercator") +
  scale_fill_gradient(low="blue",high="red")

# Number of accidents per region
data$code_region <- departements$REG[match(data$code_departement, departements$DEP)]
data_region <- data %>%
  group_by(code_region) %>%
  summarise(count = n())

# Merge the data with the region names
france$code_region <- departements$REG[match(france$region, departements$NCC)]
france$count <- data_region$count[match(france$code_region, data_region$code_region)]

# Plot the map
ggplot(france, aes(x=long, y=lat, group=group, fill=count)) +
  labs(title = "Accidents by region", x = "Longitude", y = "Latitude") +
  geom_polygon(colour="black") +
  coord_map("mercator") +
  scale_fill_gradient(low="blue",high="red")

# Severe accidents rate per department
data_severe <- data %>%
  group_by(code_departement) %>%
  summarise(count = n(), severe = sum(descr_grav == 3 | descr_grav == 4))

data_severe$rate <- data_severe$severe / data_severe$count

# Merge the data with the department names
france$rate <- data_severe$rate[match(france$code_departement, data_severe$code_departement)]

# Plot the map
ggplot(france, aes(x=long, y=lat, group=group, fill=rate)) +
  labs(title = "Severe accidents rate by department", x = "Longitude", y = "Latitude") +
  geom_polygon(colour="black") +
  coord_map("mercator") +
  scale_fill_gradient(low="blue",high="red", limits = c(0, 1))

# Severe accidents rate per region
data_severe <- data %>%
  group_by(code_region) %>%
  summarise(count = n(), severe = sum(descr_grav == 3 | descr_grav == 4))

data_severe$rate <- data_severe$severe / data_severe$count

# Merge the data with the region names
france$rate <- data_severe$rate[match(france$code_region, data_severe$code_region)]

# Plot the map
ggplot(france, aes(x=long, y=lat, group=group, fill=rate)) +
  labs(title = "Severe accidents rate by region", x = "Longitude", y = "Latitude") +
  geom_polygon(colour="black") +
  coord_map("mercator") +
  scale_fill_gradient(low="blue",high="red", limits = c(0, 1))
