# Number of accidents per surface condition
data_surface_condition <- data %>%
  group_by(descr_etat_surf) %>%
  summarise(count = n())

# Create the graph
g <- ggplot(data_surface_condition, aes(x = descr_etat_surf, y = count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  geom_text(aes(label = count), vjust = -0.3, size = 3.5) +
  labs(title = "Accidents en fonction de la description de la surface", x = "Description de la surface", y = "Accidents") +
  theme(plot.title = element_text(hjust = 0.5)) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1)) +
  scale_x_discrete(labels = setNames(names(valeurs_descr_etat_surf), valeurs_descr_etat_surf))

# Save the graph to png
ggsave(g, file="export/graph_acc_surf.png", width = 7, height = 7, dpi = 300)
