
# Description: This script make chi2 independence tests between the different variables of the dataframe.

# Load the preparation.r script to read and prepare data for use
source("preparation.r")
source("visualisation/main.r")

library(vcd)
library(ggplot2)

# Créer une colonne tranche_age à partir de la colonne age
data$tranche_age <- cut(data$age, breaks = c(0, 17, 24, 39, 59, 74, 100, 200), labels = c("0-17", "18-24", "25-39", "40-59", "60-74", "75-100", "100+"))

variable <- c("code_departement", "descr_cat_veh", "descr_agglo", "descr_athmo", "descr_lum", "descr_etat_surf", "description_intersection", "tranche_age", "place", "descr_dispo_secu", "descr_grav", "descr_motif_traj", "descr_type_col", "month", "week", "hour")

# Parcourir toutes les combinaisons de variables
for(i in 1:length(variable))
{
    if(i != length(variable))
    {
        for(j in (i+1):length(variable))
        {
            chi2 <- chisq.test(data[, variable[i]], data[, variable[j]])
            
            # Generate the mosaic plot
            png(paste("mosaic_plots/", variable[i], "_", variable[j], ".png"))
            mosaicplot(data[,variable[i]] ~ data[, variable[j]], shade = TRUE, las = 1, main = "Mosaic plot des résidus de notre Chi²", xlab = variable[i], ylab = variable[j])
            dev.off()

            # Chemin et nom de fichier de sortie
            chemin_fichier <- paste("resultat_chi2/", variable[i], "_", variable[j], ".txt")

            # Créer le fichier vide
            file.create(chemin_fichier)

            # Effectuer le test du chi2
            chi2 <- chisq.test(data$code_departement, data$descr_cat_veh)

            # Rediriger la sortie vers le fichier
            sink(chemin_fichier)

            # Afficher les résultats du test
            print(chi2)

            # Rétablir la sortie par défaut
            sink()
        }
    }
}



