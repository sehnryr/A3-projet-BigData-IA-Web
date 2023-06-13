data_month <- data %>%
  group_by(month) %>%
  summarise(count = n())

plot(data_month[month], data_month[count])

# x <- c( 420, 380, 350, 400, 440, 380, 450, 420)   
# y <- c( 5.5, 6, 6.5, 6, 5, 6.5, 4.5, 5)


# plot(x, y)