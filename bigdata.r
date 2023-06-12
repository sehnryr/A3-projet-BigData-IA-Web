# Read stat_acc_V3.csv for data preparation
data <- read.csv("stat_acc_V3.csv", header = TRUE, sep = ";")

# Convert "Null" values to NA
data[data == "NULL"] <- NA

# Convert the place column to numeric
# and replace the NA values with the median of the place column
data$place <- as.numeric(data$place)
data$place[is.na(data$place)] <- median(data$place, na.rm = TRUE)

# Convert the date column to date format
data$date <- as.Date(data$date, format = "%Y-%m-%d %H:%M:%S")

# Add a month column to the data frame
data$month <- as.numeric(format(data$date, "%m"))

# Add a week column to the data frame
data$week <- as.numeric(format(data$date, "%W"))
