# Number of accidents per city
data_city <- data %>%
  group_by(ville) %>%
  summarise(count = n())

# Get the 20 cities with the most accidents
data_city <- data_city[order(-data_city$count),]
data_city <- data_city[1:20,]

# Create the graph
g <- ggplot(data_city, aes(x = reorder(ville, -count), y = count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_text(aes(label = count), vjust = -0.3, size = 3.5) +
  labs(title = "Accidents par ville (20 premières villes)", x = "Ville", y = "Accidents") +
  theme(plot.title = element_text(hjust = 0.5)) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))

# Save the graph to png
ggsave(g, file="export/graph_acc_city.png", width = 7, height = 7, dpi = 300)