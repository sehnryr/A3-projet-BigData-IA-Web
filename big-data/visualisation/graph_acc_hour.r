# Number of accidents per hour
data_hour <- data %>%
  group_by(hour) %>%
  summarise(count = n())

# Create the graph
g <- ggplot(data_hour, aes(x = hour, y = count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_text(aes(label = count), vjust = -0.3, size = 3.5) +
  labs(title = "Accidents par tranches d'heures", x = "Heure", y = "Accidents") +
  theme(plot.title = element_text(hjust = 0.5)) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))

# Save the graph to png
ggsave(g, file="export/graph_acc_hour.png", width = 7, height = 7, dpi = 300)
