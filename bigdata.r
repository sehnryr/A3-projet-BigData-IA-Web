# Read stat_acc_V3.csv for data preparation
data <- read.csv("stat_acc_V3.csv", header = TRUE, sep = ";")

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

# Convert the date column to date format
data$date <- as.Date(data$date, format = "%Y-%m-%d %H:%M:%S")

# Convert the latitude and longitude columns to numeric
data$latitude <- as.numeric(data$latitude)
data$longitude <- as.numeric(data$longitude)

# Add a month column to the data frame
data$month <- as.numeric(format(data$date, "%m"))

# Add a week column to the data frame
data$week <- as.numeric(format(data$date, "%W"))
