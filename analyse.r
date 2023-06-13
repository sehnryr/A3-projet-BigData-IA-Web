
# Description: This script make chi2 independence tests between the different variables of the dataframe.

# Load the preparation.r script to read and prepare data for use
source("preparation.r")
library(vcd)
library(ggplot2)

data$departement <- 

variable <- c("departement", "descr_cat_veh", "descr_agglo", "descr_athmo", "descr_lum", "descr_etat_surf", "description_intersection", "tranche_age", "place", "descr_dispo_secu", "descr_grav", "descr_motif_traj", "descr_type_col", "month", "week")

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
            print(variable[i])
            print(variable[j])
            print(chi2)
            print("------------------------------------")
        }
    }
}
