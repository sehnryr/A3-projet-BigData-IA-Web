# Desccription : Calculate linear regressions on the evolution of number of accidents per month 
# and per week 

#Load the preparation.r file to have the data processed
source("preparation.r")


#Prepare a dataframe with the count of accidents sorted by month
data_month <- data %>%
  group_by(month) %>%
  summarise(count = n())

#Make the cumulative sum of the counts to have a linear correlation between time and count
data_month$count <- cumsum(data_month$count)

#Calculate the linear regression between cumulative count according to the months an then print the
#details 
lm_data_month <- lm(count ~ month, data = data_month)
print(summary(lm_data_month))

#Same as before but according to weeks instead of months
data_week <- data %>%
  group_by(week) %>%
  summarise(count = n())

data_week$count <- cumsum(data_week$count)

lm_data_week <- lm(count ~ week, data = data_week)
print(summary(lm_data_week))
