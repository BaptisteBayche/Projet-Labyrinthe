import pygame

import options
import time


def start_menu():
    # === Initilisation de la fenetre ===
    pygame.init()
    largeur, hauteur = 700, 700
    screen = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("Menu")

    # === Importation images ===
    b_start = pygame.image.load('images/bouton_start.png').convert_alpha()
    b_lvl1 = pygame.image.load('images/bouton_lvl1_b.png').convert_alpha()
    b_lvl2 = pygame.image.load('images/bouton_lvl2_b.png').convert_alpha()
    b_lvl3 = pygame.image.load('images/bouton_lvl3_b.png').convert_alpha()
    b_fleche_g = pygame.image.load('images/bouton_fleche_g.png').convert_alpha()
    b_fleche_d = pygame.image.load('images/bouton_fleche_d.png').convert_alpha()
    b_music = pygame.image.load('images/bouton_music_on.png').convert_alpha()
    _music = pygame.transform.scale(b_music, (85, 85))

    personnage_1 = pygame.image.load('images/Personnage' + str(options.get_indexPerso()) + '_arret.png').convert_alpha()
    personnage_1 = pygame.transform.scale(personnage_1, (250, 250))

    # === Création des hitbox ===
    b_start_rect = b_start.get_rect()
    b_start_rect.move_ip(275, 100)
    b_lvl1_rect = b_lvl1.get_rect()
    b_lvl1_rect.move_ip(50, 450)
    b_lvl2_rect = b_lvl2.get_rect()
    b_lvl2_rect.move_ip(275, 450)
    b_lvl3_rect = b_lvl3.get_rect()
    b_lvl3_rect.move_ip(500, 450)
    b_fleche_g_rect = b_fleche_g.get_rect()
    b_fleche_g_rect.move_ip(185, 280)
    b_fleche_d_rect = b_fleche_d.get_rect()
    b_fleche_d_rect.move_ip(475, 280)
    b_music_rect = b_music.get_rect()
    b_start_rect.move_ip(10,10)

    # === Creation des polices ===
    font = pygame.font.Font(None, 24)
    font2 = pygame.font.Font(None, 40)

    t_record1 = font2.render(options.get_score(1), 1, (1, 1, 1))
    t_record2 = font2.render(options.get_score(2), 1, (1, 1, 1))
    t_record3 = font2.render(options.get_score(3), 1, (1, 1, 1))
    t_meilleur_score = font.render("Meilleur Temps", 1, (1, 1, 1))

    background = [255, 255, 255]


    b_lvl_clique = {"b1": False, "b2": False, "b3": False}
    liste_personnage = ["Personnage0_arret.png", "Personnage1_arret.png", "Personnage2_arret.png"]
    running = True

    while running:

        screen.fill(background)
        screen.blit(b_start, (275, 100))
        screen.blit(personnage_1, (225, 180))

        screen.blit(b_fleche_d, (475, 280))
        screen.blit(b_fleche_g, (185, 280))

        screen.blit(b_lvl1, (50, 450))
        screen.blit(b_lvl2, (275, 450))
        screen.blit(b_lvl3, (500, 450))

        screen.blit(t_record1, (90, 555))
        screen.blit(t_meilleur_score, (67, 525))
        screen.blit(t_record2, (315, 555))
        screen.blit(t_meilleur_score, (292, 525))
        screen.blit(t_record3, (540, 555))
        screen.blit(t_meilleur_score, (517, 525))
        screen.blit(b_music, (10, 10))
        if options.get_musique() == "True":
            b_music = pygame.image.load('images/bouton_music_on.png').convert_alpha()
        elif options.get_musique() == "False":
            b_music = pygame.image.load('images/bouton_music_off.png').convert_alpha()

        screen.blit(b_music, (10, 10))

        for event in pygame.event.get():
            if pygame.mouse.get_focused():
                x, y = pygame.mouse.get_pos()

                if b_lvl1_rect.collidepoint(x, y):
                    b_lvl1 = pygame.image.load('images/bouton_lvl1_v.png')
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        options.set_taille(5)
                        options.set_taille_fenetre(682)
                        options.set_taille_carre(62)
                        options.set_vitesse_deplacement(3)
                        b_lvl_clique["b1"] = True
                        b_lvl_clique["b3"] = False
                        b_lvl_clique["b2"] = False
                elif b_lvl2_rect.collidepoint(x, y):
                    b_lvl2 = pygame.image.load('images/bouton_lvl2_v.png')
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        options.set_taille(7)
                        options.set_taille_fenetre(690)
                        options.set_taille_carre(46)
                        options.set_vitesse_deplacement(3)
                        b_lvl_clique["b2"] = True
                        b_lvl_clique["b3"] = False
                        b_lvl_clique["b1"] = False
                elif b_lvl3_rect.collidepoint(x, y):
                    b_lvl3 = pygame.image.load('images/bouton_lvl3_v.png')
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        options.set_taille(8)
                        options.set_taille_fenetre(680)
                        options.set_taille_carre(40)
                        options.set_vitesse_deplacement(2)
                        b_lvl_clique["b3"] = True
                        b_lvl_clique["b1"] = False
                        b_lvl_clique["b2"] = False

                else:
                    if b_lvl_clique["b1"] == False:
                        b_lvl1 = pygame.image.load('images/bouton_lvl1_b.png')
                    if b_lvl_clique["b2"] == False:
                        b_lvl2 = pygame.image.load('images/bouton_lvl2_b.png')
                    if b_lvl_clique["b3"] == False:
                        b_lvl3 = pygame.image.load('images/bouton_lvl3_b.png')

                if b_start_rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if True in b_lvl_clique.values():
                        running = False
                        pygame.quit()
                        return True
                if b_fleche_d_rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    personnage = changer_personnage(liste_personnage, options.get_indexPerso(), "droite")
                    personnage_1 = pygame.image.load('images/' + str(personnage))
                    personnage_1 = pygame.transform.scale(personnage_1, (250, 250))

                if b_fleche_g_rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    personnage = changer_personnage(liste_personnage, options.get_indexPerso(), "gauche")
                    personnage_1 = pygame.image.load('images/' + str(personnage))
                    personnage_1 = pygame.transform.scale(personnage_1, (250, 250))

                if b_music_rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if options.get_musique() == "True":
                        options.set_musique("False")
                    elif options.get_musique() == "False":
                        options.set_musique("True")




                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

        pygame.display.flip()
        if running:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()


def changer_personnage(liste_personnage, index_personnage, direction):
    if direction == "droite":
        if len(liste_personnage) - 1 == index_personnage:
            options.set_indexPerso(0)
            return liste_personnage[0]
        else:
            options.set_indexPerso(index_personnage + 1)
            return liste_personnage[index_personnage + 1]
    else:
        if index_personnage == 0:
            options.set_indexPerso(len(liste_personnage) - 1)
            return liste_personnage[len(liste_personnage) - 1]
        else:
            options.set_indexPerso(index_personnage - 1)
            return liste_personnage[index_personnage - 1]
