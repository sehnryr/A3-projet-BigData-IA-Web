source("preparation.r")


variable <- c("id_code_insee", "descr_cat_veh", "descr_agglo", "descr_athmo", "descr_lum", "descr_etat_surf", "description_intersection", "age", "place", "descr_dispo_secu", "descr_grav", "descr_motif_traj", "descr_type_col", "month", "week")
# Parcourir toutes les combinaisons de variables
for(i in 1:length(variable))
{
    if(i != length(variable))
    {
        for(j in (i+1):length(variable))
        {
            tableau <- table(data[, variable[i]], data[, variable[j]])
            chi2 <- chisq.test(data[, variable[i]], data[, variable[j]])
            print(variable[i])
            print(variable[j])
            print(tableau)
            print("")
            print(chi2)
            print("------------------------------------")
        }
    }
}

