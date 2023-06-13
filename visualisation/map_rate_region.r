# Severe accidents rate per region
data_severe <- data %>%
  group_by(code_region) %>%
  summarise(count = n(), severe = sum(descr_grav == 3 | descr_grav == 4))
data_severe$rate <- data_severe$severe / data_severe$count

# Merge the data with the france map data
france$rate <- data_severe$rate[match(france$code_region, data_severe$code_region)]

# Create the map
g <- ggplot(france, aes(x=long, y=lat, group=group, fill=rate)) +
  labs(title = "Taux d'accident grave par région", x = "Longitude", y = "Latitude") +
  geom_polygon(colour="black") +
  coord_map("mercator") +
  scale_fill_gradient(low="blue",high="red", limits = c(0, 1))

# Save the map as png
ggsave(g, file="export/map_rate_region.png", width = 7, height = 7, dpi = 300)
