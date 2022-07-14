# === Importation fichiers python ===

import generation_chemin
import generation_matrice
import resolution
import creation_image
import script
import menu
import options


# Si True on relance si False le programme s'arrete
jouer = True

multiplicateur_temps = {5: 1, 7: 0.7, 8: 0.75}
while jouer:

    jouer = menu.start_menu()
    if jouer:
        # === Création labyrinthe ===
        taille = options.get_taille()
        couleur = creation_image.get_couleur()

        chemin_lab = generation_chemin.creation_chemin(taille)
        matrice_lab = generation_matrice.matrice(chemin_lab, taille)

        chemin_resolution = resolution.cherche_chemin(chemin_lab)
        matrice_resolution = generation_matrice.matrice(chemin_resolution, taille)

        creation_image.creer_image(matrice_lab, matrice_resolution)

        # === On lance le jeu ===
        # Renvoi False si :
        #   Le joueur perd - Le joueur ferme le programme
        # Renvoi True si:
        #   Le joueur gagne - Le joueur fait retour

        if script.start_jeu(couleur, int(len(chemin_resolution) * multiplicateur_temps[taille]), taille) == False:
            jouer = False
