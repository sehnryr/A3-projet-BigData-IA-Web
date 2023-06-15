# Desccription : Calculate linear regressions on the evolution of number of accidents per month 
# and per week 

# Load the preparation.r file to have the data processed
source("preparation.r")


# Prepare a dataframe with the count of accidents sorted by month
data_month <- data %>%
  group_by(month) %>%
  summarise(count = n())

# Make the cumulative sum of the counts to have a linear correlation between time and count
data_month$count <- cumsum(data_month$count)

# Calculate the linear regression between cumulative count according to the months an then print the
# details 
lm_data_month <- lm(count ~ month, data = data_month)
print(summary(lm_data_month))


# Same as before but according to weeks instead of months
data_week <- data %>%
  group_by(week) %>%
  summarise(count = n())

data_week$count <- cumsum(data_week$count)

lm_data_week <- lm(count ~ week, data = data_week)
print(summary(lm_data_week))

# Regression performance analysis
r_squared_month <- summary(lm_data_month)$r.squared
r_squared_week <- summary(lm_data_week)$r.squared

cat("R² pour les mois : ",r_squared_month, "\n")
cat("R² pour les semaines : ",r_squared_week, "\n")

# Analysis of standard errors associated with estimators
standard_errors_month <- summary(lm_data_month)$coefficients[, "Std. Error"]
standard_errors_week <- summary(lm_data_week)$coefficients[, "Std. Error"]

cat(
  "Erreurs types associées au estimateurs pour les mois : ",
  standard_errors_month,
  "\n"
)
cat(
  "Erreurs types associées au estimateurs pour les semaines : ",
  standard_errors_week,
  "\n"
)


# Calculation of 95% confidence intervals of estimators
confidence_interval_month <- confint(lm_data_month)
confidence_interval_week <- confint(lm_data_week)

cat(
  "Intervalles de confiance pour les estimateurs (mois) : ",
  confidence_interval_month,
  "\n"
)
cat(
  "Intervalles de confiance pour les estimateurs (semaines) : ",
  confidence_interval_week,
  "\n"
)

#Visualisation of cumulative sum

# Create the month names
data_month$month_name <- c(
  "Janvier",
  "Février",
  "Mars",
  "Avril",
  "Mai",
  "Juin",
  "Juillet",
  "Août",
  "Septembre",
  "Octobre",
  "Novembre",
  "Décembre"
)[data_month$month]

# Create the graph
g <- ggplot(data_month, aes(x = reorder(month_name, month), y = count)) +
  geom_point() +
  labs(
    title = "Somme cumulative des accidents par tranche de mois",
    x = "Mois",
    y = "Accidents"
  ) +
  theme(plot.title = element_text(hjust = 0.5)) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))

# Save the graph to png
ggsave(g, file="export/graph_acc_month_cum.png", width = 7, height = 7, dpi = 300)









