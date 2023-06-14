# Load the preparation.r script to prepare the data
source("preparation.r")

# Load the libraries
suppressPackageStartupMessages(library(dplyr)) # for data manipulation
suppressPackageStartupMessages(library(ggplot2)) # for plotting graphs
suppressPackageStartupMessages(library(ggmap)) # for plotting maps
suppressPackageStartupMessages(library(mapproj)) # for scaling maps

# Number of accidents per atmospheric condition
source("visualisation/graph_acc_atmo.r")

# Number of accidents per surface condition
source("visualisation/graph_acc_surf.r")

# Number of accidents per gravity of the accident
source("visualisation/graph_acc_grav.r")

# Number of accidents per hour
source("visualisation/graph_acc_hour.r")

# Number of accidents per city
source("visualisation/graph_acc_city.r")

# Number of accidents per age
source("visualisation/graph_acc_age.r")

# Number of accidents per month
source("visualisation/graph_acc_month.r")

# Get France map data and merge it with the department names
# and the region names
france <- map_data("france")
france$region <- gsub(" ", "", gsub("-", "", toupper(france$region)))
france$code_departement <- departements$DEP[match(france$region, departements$NCC)]
france$code_region <- departements$REG[match(france$region, departements$NCC)]

# Number of accidents per department
source("visualisation/map_acc_dep.r")

# Number of accidents per region
source("visualisation/map_acc_region.r")

# Severe accidents rate per department
source("visualisation/map_rate_dep.r")

# Severe accidents rate per region
source("visualisation/map_rate_region.r")
