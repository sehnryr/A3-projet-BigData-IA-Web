
# Description: This script make chi2 independence tests between the different variables of the dataframe.

# Load the preparation.r script to read and prepare data for use
source("preparation.r")

library(vcd)
library(ggplot2)

# Créer une colonne tranche_age à partir de la colonne age
data$tranche_age <- cut(
  data$age,
  breaks = c(0, 17, 24, 39, 59, 74, 100, 200),
  labels = c("0-17", "18-24", "25-39", "40-59", "60-74", "75-100", "100+")
)

suppressWarnings({
    dir.create("mosaic_plots")
    dir.create("resultat_chi2")
})

variable <- c(
  "code_departement",
  "descr_cat_veh",
  "descr_agglo",
  "descr_athmo",
  "descr_lum",
  "descr_etat_surf",
  "description_intersection",
  "tranche_age",
  "place",
  "descr_dispo_secu",
  "descr_grav",
  "descr_motif_traj",
  "descr_type_col",
  "month",
  "week",
  "hour"
)

# Parcourir toutes les combinaisons de variables
for(i in 1:length(variable))
{
    if(i != length(variable))
    {
        for(j in (i+1):length(variable))
        {
            suppressWarnings({
                chi2 <- chisq.test(data[, variable[i]], data[, variable[j]])
            })

            # Generate the mosaic plot
            png(paste("mosaic_plots/", variable[i], "_", variable[j], ".png"))
            mosaicplot(data[,variable[i]] ~ data[, variable[j]], shade = TRUE, las = 1, main = "Mosaic plot des résidus de notre Chi²", xlab = variable[i], ylab = variable[j])
            dev.off()

            # Créer le fichier vide
            file.create(paste("resultat_chi2/", variable[i], "_", variable[j], ".txt"))
            
            # Rediriger la sortie vers le fichier
            sink(paste("resultat_chi2/", variable[i], "_", variable[j], ".txt"))

            # Afficher les résultats du test
            print(chi2)

            # Rétablir la sortie par défaut
            sink()
        }
    }
}
