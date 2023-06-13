# Number of accidents per gravity of the accident
data_gravity <- data %>%
  group_by(descr_grav) %>%
  summarise(count = n())

# Create the graph
g <- ggplot(data_gravity, aes(x = descr_grav, y = count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_text(aes(label = count), vjust = -0.3, size = 3.5) +
  labs(title = "Accidents selon la gravité", x = "Gravity", y = "Accidents") +
  theme(plot.title = element_text(hjust = 0.5)) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1)) +
  scale_x_discrete(labels = setNames(names(valeurs_descr_grav), valeurs_descr_grav))

# Save the graph to png
ggsave(g, file="export/graph_acc_grav.png", width = 7, height = 7, dpi = 300)
