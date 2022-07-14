# Créé par FAUX Clément, le 09/02/2021 en Python 3.7
import pygame
from PIL import Image
import record
from generation_chemin import creation_chemin
from principale import Principale
import creation_image
import options
import time


def start_jeu(couleur1, longueur_chemin, niveau):
    pygame.init()
    couleur = (couleur1[0],couleur1[1],couleur1[2])


    largeur,hauteur = 1000, 700

    image = Image.open('images/background.png')

    background = pygame.image.load('images/background.png')
    bouton_retour_menu = pygame.image.load('images/bouton_retour.png')
    bouton_play = pygame.image.load('images/bouton_reprendre.png')

    bouton_retour_menu_rect = bouton_retour_menu.get_rect()
    bouton_retour_menu_rect.move_ip(((options.get_taille_fenetre()+1000)/2)-75,350)
    bouton_play_rect = bouton_play.get_rect()
    bouton_play_rect.move_ip(((options.get_taille_fenetre()+1000)/2)-75,500)

    principale = Principale()


    counter = longueur_chemin
    if counter > 9:
        text = "00:"+str(counter)
    else:
        text = "00:0"+str(counter)

    font = pygame.font.SysFont('Consolas', 30)
    font2 = pygame.font.SysFont('Consolas', 60)

    file = 'images/Dee Yan-Key - old house.mp3'

    if options.get_musique() == "True":
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)




    screen = pygame.display.set_mode((largeur,hauteur))
    pygame.display.set_caption("Pj labyrinthe")
    running = True
    chrono = True
    rebours = 4
    texte_fdp = ""
    texte_couleur = (0,0,0)
    gagner = False
    vitesse = options.get_vitesse_deplacement()


    while running:

        while rebours > 0:
            screen.fill([255, 255, 255])
            screen.blit(font.render(text, True, (0, 0, 0)), (((options.get_taille_fenetre() + 1000) / 2) - 37, 50))
            screen.blit(pygame.image.load('images/fond.png'), (0, 0))

            if rebours == 1:
                screen.blit(font2.render(str('GO!'), True, (0, 0, 0)), (((options.get_taille_fenetre() + 1000) / 2) - 37, 150))
            else:
                screen.blit(font2.render(str(rebours - 1), True, (0, 0, 0)),(((options.get_taille_fenetre() + 1000) / 2) - 15, 150))
            pygame.display.flip()
            pygame.time.wait(1000)
            rebours = rebours -1
            if rebours ==0:
                pygame.time.set_timer(pygame.USEREVENT, 1000)



        screen.fill([255, 255, 255])
        screen.blit(background, (0, 0))
        screen.blit(bouton_retour_menu, (((options.get_taille_fenetre() + 1000) / 2) - 75, 350))
        screen.blit(bouton_play, (((options.get_taille_fenetre() + 1000) / 2) - 75, 500))
        if chrono == True:
            screen.blit(principale.utilisateur.image, principale.utilisateur.rect)
        taille_fenetre = options.get_taille_fenetre()
        taille_carre = options.get_taille_carre()
        screen.blit(font.render(text, True, (0, 0, 0)), (((options.get_taille_fenetre() + 1000) / 2) - 37, 50))
        screen.blit(font.render(" ESPACE pour PAUSE !", True, (0, 0, 0)),(((options.get_taille_fenetre() + 1000) / 2)-163, 150))
        screen.blit(font.render(texte_fdp, True, texte_couleur),(((options.get_taille_fenetre() + 1000) / 2) - 145, 250))
        pygame.display.flip()

        if gagner:
            pygame.time.wait(3000)
            return True









        keys = pygame.key.get_pressed()
        if running:
            if chrono == 0:
                background =  pygame.image.load('images/background_sol.png')
            else:
                background = pygame.image.load('images/background.png')
            if principale.appuyee.get(pygame.K_RIGHT):
                if image.getpixel((principale.utilisateur.rect.x+30, principale.utilisateur.rect.y)) == couleur  and \
                    image.getpixel((principale.utilisateur.rect.x+30, principale.utilisateur.rect.y+30)) == couleur  and \
                    principale.utilisateur.rect.x < taille_fenetre - (30 + options.get_vitesse_deplacement()):
                    principale.utilisateur.deplacement_droite()
                elif image.getpixel((principale.utilisateur.rect.x+30, principale.utilisateur.rect.y)) != couleur  and \
                    image.getpixel((principale.utilisateur.rect.x+30, principale.utilisateur.rect.y+30)) != couleur:
                    for recul in range(vitesse+1):
                        principale.utilisateur.deplacement_gauche()
            elif principale.appuyee.get(pygame.K_LEFT):
                if image.getpixel((principale.utilisateur.rect.x, principale.utilisateur.rect.y)) == couleur  and \
                    image.getpixel((principale.utilisateur.rect.x, principale.utilisateur.rect.y+30)) == couleur  and \
                    principale.utilisateur.rect.x > 0:
                    principale.utilisateur.deplacement_gauche()
                elif image.getpixel((principale.utilisateur.rect.x, principale.utilisateur.rect.y)) != couleur  and \
                    image.getpixel((principale.utilisateur.rect.x, principale.utilisateur.rect.y+30)) != couleur:
                    for recul in range(vitesse+1):
                        principale.utilisateur.deplacement_droite()
            elif principale.appuyee.get(pygame.K_UP):
                if image.getpixel((principale.utilisateur.rect.x, principale.utilisateur.rect.y)) == couleur  and \
                    image.getpixel((principale.utilisateur.rect.x+30, principale.utilisateur.rect.y)) == couleur:
                    principale.utilisateur.deplacement_haut()
                elif image.getpixel((principale.utilisateur.rect.x, principale.utilisateur.rect.y)) != couleur  and \
                    image.getpixel((principale.utilisateur.rect.x+30, principale.utilisateur.rect.y)) != couleur:
                    for recul in range(vitesse+1):
                        principale.utilisateur.deplacement_bas()
            elif principale.appuyee.get(pygame.K_DOWN):
                if image.getpixel((principale.utilisateur.rect.x, principale.utilisateur.rect.y+30)) == couleur  and \
                    image.getpixel((principale.utilisateur.rect.x+30, principale.utilisateur.rect.y+30)) == couleur:
                    principale.utilisateur.deplacement_bas()
                elif image.getpixel((principale.utilisateur.rect.x, principale.utilisateur.rect.y+30)) != couleur  and \
                    image.getpixel((principale.utilisateur.rect.x+30, principale.utilisateur.rect.y+30)) != couleur:
                    for recul in range(vitesse+1):
                        principale.utilisateur.deplacement_haut()
            elif principale.utilisateur.rect.x+15 > taille_fenetre - taille_carre and principale.utilisateur.rect.x < taille_fenetre and \
                 principale.utilisateur.rect.y+15 > taille_fenetre - 2 * taille_carre and principale.utilisateur.rect.y < taille_fenetre - taille_carre:
                    texte_fdp = "Vous avez gagné !"
                    texte_couleur = (34, 173, 36)
                    temps =  longueur_chemin - counter
                    record.battue(niveau,temps)
                    gagner = True




            elif keys[pygame.K_SPACE] or chrono == False:
                if chrono == True:
                    background = pygame.image.load('images/fond.png')
                screen.blit(background, (0, 0))
                pygame.display.flip()
                appuie_espace = True
                while appuie_espace == True:
                    for event in pygame.event.get():
                        if pygame.mouse.get_focused():
                            x, y = pygame.mouse.get_pos()
                            if bouton_play_rect.collidepoint(x, y):
                                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                    appuie_espace = False
                            if bouton_retour_menu_rect.collidepoint(x, y):
                                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                    running = False
                                    appuie_espace = False
                                    pygame.quit()
                        if event.type == pygame.QUIT:
                            running = False
                            pygame.quit()
                            return False




            else:
                principale.utilisateur.deplacement_arret()


        if running:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    return False
                elif event.type == pygame.KEYDOWN:
                    principale.appuyee[event.key] = True
                elif event.type == pygame.KEYUP:
                    principale.appuyee[event.key] = False
                if event.type == pygame.USEREVENT and chrono == True:
                    counter -= 1
                    if  counter < 10:
                        text = '00:0' + str(counter)
                    else:
                        text = '00:' + str(counter)
                if counter == 0:
                    chrono = False
                    background = pygame.image.load('images/background_sol.png')
                    texte_fdp = "Vous avez perdu !"
                    texte_couleur = (244,33,33)