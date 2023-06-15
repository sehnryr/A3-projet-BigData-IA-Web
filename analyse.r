
# Description: This script make chi2 independence tests between the different variables of the dataframe.

# Load the preparation.r script to read and prepare data for use
source("preparation.r")
source("visualisation/main.r")

library(vcd)
library(ggplot2)

# # Créer une colonne tranche_age à partir de la colonne age
# analyse <- data

# analyse$tranche_age <- cut(analyse$age, breaks = c(0, 24, 39, 59, 74, 200), labels = c("0-24", "25-39", "40-59", "60-74", "75+"))

# dir.create("mosaic_plots")
# dir.create("resultat_chi2")

# variable <- c("code_departement", "descr_cat_veh", "descr_agglo", "descr_athmo", "descr_lum", "descr_etat_surf", "description_intersection", "tranche_age", "place", "descr_dispo_secu", "descr_grav", "descr_motif_traj", "descr_type_col", "month", "week", "hour")

# # Parcourir toutes les combinaisons de variables
# for(i in 1:length(variable))
# {
#     if(i != length(variable))
#     {
#         for(j in (i+1):length(variable))
#         {
#             suppressWarnings({
#                 chi2 <- chisq.test(analyse[, variable[i]], analyse[, variable[j]])
#             })

#             # Generate the mosaic plot
#             png(paste("mosaic_plots/", variable[i], "_", variable[j], ".png"))
#             mosaicplot(analyse[,variable[i]] ~ analyse[, variable[j]], shade = TRUE, las = 1, main = "Mosaic plot des résidus de notre Chi²", xlab = variable[i], ylab = variable[j])
#             dev.off()

#             # Créer le fichier vide
#             file.create(paste("resultat_chi2/", variable[i], "_", variable[j], ".txt"))
            
#             # Rediriger la sortie vers le fichier
#             sink(paste("resultat_chi2/", variable[i], "_", variable[j], ".txt"))

#             # Afficher les résultats du test
#             print(chi2)

#             # Rétablir la sortie par défaut
#             sink()
#         }
#     }
# }

# filtered_data <- data[data$descr_dispo_secu == 2 | data$descr_dispo_secu == 7 ,]
# filtered_data$descr_dispo_secu <- factor(filtered_data$descr_dispo_secu, levels = c(2, 7))
# png("casque.png")
# mosaicplot(filtered_data$descr_dispo_secu ~ filtered_data$descr_grav , shade = TRUE, las = 1, main = "Mosaic plot des résidus de notre Chi²", xlab = "Sécurité", ylab = "Gravité")
# dev.off()

# filtered_data <- data[data$descr_dispo_secu == 3 | data$descr_dispo_secu == 19 ,]
# filtered_data$descr_dispo_secu <- factor(filtered_data$descr_dispo_secu, levels = c(3, 19))
# png("casque.png")
# mosaicplot(filtered_data$descr_dispo_secu ~ filtered_data$descr_grav , shade = TRUE, las = 1, main = "Mosaic plot des résidus de notre Chi²", xlab = "Sécurité", ylab = "Gravité")
# dev.off()


# png("casque.png")
# mosaicplot(data$descr_cat_veh ~ data$descr_grav , shade = TRUE, las = 1, main = "Mosaic plot des résidus de notre Chi²", xlab = "Sécurité", ylab = "Gravité")
# dev.off()

