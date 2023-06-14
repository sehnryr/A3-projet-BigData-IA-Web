# Number of accidents per region
data_region <- data %>%
  group_by(code_region) %>%
  summarise(count = n())

# Merge the data with the france map data
france$count <- data_region$count[match(france$code_region, data_region$code_region)]

# Create the map
g <- ggplot(france, aes(x=long, y=lat, group=group, fill=count)) +
  labs(title = "Accidents par région", x = "Longitude", y = "Latitude") +
  geom_polygon(colour="black") +
  coord_map("mercator") +
  scale_fill_gradient(low="blue",high="red")

# Save the map as png
ggsave(g, file="export/map_acc_region.png", width = 7, height = 7, dpi = 300)
