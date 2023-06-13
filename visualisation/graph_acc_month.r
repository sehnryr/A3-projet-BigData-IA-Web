# Number of accidents per month
data_month <- data %>%
  group_by(month) %>%
  summarise(count = n())

# Create the month name
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
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_text(aes(label = count), vjust = -0.3, size = 3.5) +
  labs(title = "Accidents par tranche de mois", x = "Mois", y = "Accidents") +
  theme(plot.title = element_text(hjust = 0.5)) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))

# Save the graph to png
ggsave(g, file="export/graph_acc_month.png", width = 7, height = 7, dpi = 300)