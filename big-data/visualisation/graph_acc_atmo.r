# Number of accidents per atmospheric condition
data_atmospheric_condition <- data %>%
  group_by(descr_athmo) %>%
  summarise(count = n())

# Add the label to the data
data_atmospheric_condition$label <- names(valeur_descr_athmo)[
  data_atmospheric_condition$descr_athmo]

# Create the graph
g <- ggplot(data_atmospheric_condition, aes(x = reorder(label, descr_athmo), y = count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_text(aes(label = count), vjust = -0.3, size = 3.5) +
  labs(title = "Accidents en fonction des conditions atmosphériques", x = "Condition atmosphérique", y = "Accidents") +
  theme(plot.title = element_text(hjust = 0.5)) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))

# Save the graph to png
ggsave(g, file="export/graph_acc_atmo.png", width = 7, height = 7, dpi = 300)
