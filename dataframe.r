insee <- read.csv("correspondance-code-insee-code-postal.csv", sep = ";")
print
insee <- insee[, c("CodeINSEE", "CodeRégion")]
# => Code insée / code région

region <- read.csv("region2009.csv")
# => Code région / nom région

population <- read.csv("population.csv")
# => Nom région / population

sample <- read.csv("output.csv")
sample <- sample[, c("id_code_insee", "descr_grav")]
# => Code insée / gravité

sample_insee <- merge(sample, insee, by.x = "id_code_insee", by.y = "CodeINSEE")
# => Code insée / gravité / code région

# affiche le nombre de ligne avec le même numéro de région et même numéro de gravité
sample_insee <- aggregate(sample_insee$descr_grav, by = list(sample_insee$CodeRégion, sample_insee$descr_grav), FUN = length)
colnames(sample_insee) <- c("CodeRégion", "Gravité", "Nombre")
sample_insee <- sample_insee[order(sample_insee$CodeRégion), ]

sample_insee_region <- merge(sample_insee, region, by.x = "CodeRégion", by.y = "region_region")

sample_insee_region <- sample_insee_region[, c("region_nom", "Gravité", "Nombre")]
colnames(sample_insee_region) <- c("Région", "Gravité", "Nombre")

sample_insee_region_population <- merge(sample_insee_region, population, by.x = "Région", by.y = "population_region")

sample_insee_region_population$NbAccident <- sample_insee_region_population$Nombre / sample_insee_region_population$population * 100000
sample_insee_region_population <- sample_insee_region_population[, c("Région", "Gravité", "NbAccidentPour100000")]

write.csv(sample_insee_region_population, "dataframeACP.csv", row.names = FALSE, quote=F)