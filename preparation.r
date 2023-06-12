# Description: This script prepares the data for the analysis.

# Load the read.r script to read the data
source("read.r")

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
laposte_hexasmal <- read.csv("laposte_hexasmal.csv", header = TRUE, sep = ";")
# Split coordonnees_geographiques column into latitude and longitude columns
laposte_hexasmal$latitude <- as.numeric(sapply(strsplit(as.character(laposte_hexasmal$coordonnees_geographiques), ","), head, 1))
laposte_hexasmal$longitude <- as.numeric(sapply(strsplit(as.character(laposte_hexasmal$coordonnees_geographiques), ","), tail, 1))

data$latitude <- laposte_hexasmal$latitude[match(data$id_code_insee, laposte_hexasmal$code_commune_insee)]
data$longitude <- laposte_hexasmal$longitude[match(data$id_code_insee, laposte_hexasmal$code_commune_insee)]

# Convert columns to numeric
data$Num_Acc <- as.numeric(data$Num_Acc)
data$id_usa <- as.numeric(data$id_usa)
data$latitude <- as.numeric(data$latitude)
data$longitude <- as.numeric(data$longitude)

# Convert the date column to a date format
data$date <- strptime(data$date, format = "%Y-%m-%d %H:%M:%S")

# Add a month column to the data frame
data$month <- as.numeric(format(data$date, "%m"))

# Add a week column to the data frame
data$week <- as.numeric(format(data$date, "%W"))
