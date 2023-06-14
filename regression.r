source("preparation.r")

data_month <- data %>%
  group_by(month) %>%
  summarise(count = n())

lm_data_month <- lm(count ~ month, data = data_month)
summary(lm_data_month)

data_week <- data %>%
  group_by(week) %>%
  summarise(count = n())

lm_data_week <- lm(count ~ week, data = data_week)
summary(lm_data_week)

# x <- c( 420, 380, 350, 400, 440, 380, 450, 420)   
# y <- c( 5.5, 6, 6.5, 6, 5, 6.5, 4.5, 5)


# plot(x, y)
