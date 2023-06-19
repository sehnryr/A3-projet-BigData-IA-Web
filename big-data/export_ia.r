source("preparation.r")

export <- data %>%
  select(
    code_region,
    descr_cat_veh,
    descr_agglo,
    descr_athmo,
    descr_lum,
    descr_etat_surf,
    description_intersection,
    place,
    descr_dispo_secu,
    descr_grav,
    descr_motif_traj,
    descr_type_col,
    month,
    week,
    day, # [1] "lundi", [2] "mardi", [3] "mercredi", [4] "jeudi", [5] "vendredi", [6] "samedi", [7] "dimanche"
    hour,
    age,
    place
  )

export <- export %>% rename_at('code_region', ~ 'region')
export <- export %>% rename_at('descr_cat_veh', ~ 'categorie_vehicule')
export <- export %>% rename_at('descr_agglo', ~ 'agglomeration')
export <- export %>% rename_at('descr_athmo', ~ 'atmosphere')
export <- export %>% rename_at('descr_lum', ~ 'luminosite')
export <- export %>% rename_at('descr_etat_surf', ~ 'etat_surface')
export <- export %>% rename_at('description_intersection', ~ 'intersection')
export <- export %>% rename_at('descr_dispo_secu', ~ 'disposition_securite')
export <- export %>% rename_at('descr_grav', ~ 'gravite')
export <- export %>% rename_at('descr_motif_traj', ~ 'motif_deplacement')
export <- export %>% rename_at('descr_type_col', ~ 'type_collision')
export <- export %>% rename_at('month', ~ 'mois')
export <- export %>% rename_at('week', ~ 'semaine')
export <- export %>% rename_at('day', ~ 'jour')
export <- export %>% rename_at('hour', ~ 'heure')
export <- export %>% rename_at('age', ~ 'age')
export <- export %>% rename_at('place', ~ 'place')

write.csv(export, "export_IA.csv", quote = FALSE, row.names = FALSE)
