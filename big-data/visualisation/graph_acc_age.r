# Number of accidents per age
data_age <- data %>%
  group_by(age) %>%
  summarise(count = n())
data_age$age <- as.numeric(data_age$age - (2023 - 2009))

# Create the graph
g <- ggplot(data_age, aes(x = age, y = count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(title = "Accidents par tranche d'age", x = "Age", y = "Accidents") +
  theme(plot.title = element_text(hjust = 0.5)) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))

# Save the graph to png
ggsave(g, file="export/graph_acc_age.png", width = 7, height = 7, dpi = 300)