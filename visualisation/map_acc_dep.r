# Number of accidents per department
data$code_departement <- substr(data$id_code_insee, 1, 2)
data_departement <- data %>%
  group_by(code_departement) %>%
  summarise(count = n())

# Merge the data with the france map data
france$count <- data_departement$count[match(france$code_departement, data_departement$code_departement)]

# Create the map
g <- ggplot(france, aes(x=long, y=lat, group=group, fill=count)) +
  labs(title = "Accidents par départements", x = "Longitude", y = "Latitude") +
  geom_polygon(colour="black") +
  coord_map("mercator") +
  scale_fill_gradient(low="blue",high="red")

# Save the map as png
ggsave(g, file="export/map_acc_dep.png", width = 7, height = 7, dpi = 300)