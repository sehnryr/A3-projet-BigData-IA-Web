source("preparation.r")

data_month <- data %>%
  group_by(month) %>%
  summarise(count = n())

lm_data_month <- lm(count ~ month, data = data_month)
print(summary(lm_data_month))

data_week <- data %>%
  group_by(week) %>%
  summarise(count = n())

lm_data_week <- lm(count ~ week, data = data_week)
print(summary(lm_data_week))

