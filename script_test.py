# Créé par FAUX Clément, le 09/02/2021 en Python 3.7
import pygame

from PIL import Image

from generation_chemin import creation_chemin
from principale import Principale
import creation_image
import options


def start_jeu(couleur1):

    pygame.init()
    couleur = (couleur1[0],couleur1[1],couleur1[2])


    largeur,hauteur = 1000, 700

    image = Image.open('images/background.png')
    background = pygame.image.load('images/background.png')
    principale = Principale()
    clock = pygame.time.Clock()

    counter, text = 15, '00:15'
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

#    file = 'images/djadja.mp3'
#    pygame.mixer.init()
#    pygame.mixer.music.load(file)
#    pygame.mixer.music.play(-1)



    screen = pygame.display.set_mode((largeur,hauteur))
    pygame.display.set_caption("Pj labyrinthe")
    running = True
    while running:

        screen.fill([255,255,255])
        screen.blit(background, (0,0))
        screen.blit(principale.utilisateur.image, principale.utilisateur.rect)
        taille_fenetre = options.get_taille_fenetre()
        taille_carre = options.get_taille_carre()

        screen.blit(font.render(text, True, (0, 0, 0)), (900, 50))


        if principale.appuyee.get(pygame.K_RIGHT):
            if image.getpixel((principale.utilisateur.rect.x+30, principale.utilisateur.rect.y)) == couleur  and \
                image.getpixel((principale.utilisateur.rect.x+30, principale.utilisateur.rect.y+30)) == couleur  and \
                principale.utilisateur.rect.x < taille_fenetre - (30 + options.get_vitesse_deplacement()):
                principale.utilisateur.deplacement_droite()
            elif image.getpixel((principale.utilisateur.rect.x+30, principale.utilisateur.rect.y)) != couleur  and \
                image.getpixel((principale.utilisateur.rect.x+30, principale.utilisateur.rect.y+30)) != couleur:
                principale.utilisateur.deplacement_gauche()
                principale.utilisateur.deplacement_gauche()
        elif principale.appuyee.get(pygame.K_LEFT):
            if image.getpixel((principale.utilisateur.rect.x, principale.utilisateur.rect.y)) == couleur  and \
                image.getpixel((principale.utilisateur.rect.x, principale.utilisateur.rect.y+30)) == couleur  and \
                principale.utilisateur.rect.x > 0:
                principale.utilisateur.deplacement_gauche()
            elif image.getpixel((principale.utilisateur.rect.x, principale.utilisateur.rect.y)) != couleur  and \
                image.getpixel((principale.utilisateur.rect.x, principale.utilisateur.rect.y+30)) != couleur:
                principale.utilisateur.deplacement_droite()
                principale.utilisateur.deplacement_droite()
        elif principale.appuyee.get(pygame.K_UP):
            if image.getpixel((principale.utilisateur.rect.x, principale.utilisateur.rect.y)) == couleur  and \
                image.getpixel((principale.utilisateur.rect.x+30, principale.utilisateur.rect.y)) == couleur:
                principale.utilisateur.deplacement_haut()
            elif image.getpixel((principale.utilisateur.rect.x, principale.utilisateur.rect.y)) != couleur  and \
                image.getpixel((principale.utilisateur.rect.x+30, principale.utilisateur.rect.y)) != couleur:
                principale.utilisateur.deplacement_bas()
                principale.utilisateur.deplacement_bas()
        elif principale.appuyee.get(pygame.K_DOWN):
            if image.getpixel((principale.utilisateur.rect.x, principale.utilisateur.rect.y+30)) == couleur  and \
                image.getpixel((principale.utilisateur.rect.x+30, principale.utilisateur.rect.y+30)) == couleur:
                principale.utilisateur.deplacement_bas()
            elif image.getpixel((principale.utilisateur.rect.x, principale.utilisateur.rect.y+30)) != couleur  and \
                image.getpixel((principale.utilisateur.rect.x+30, principale.utilisateur.rect.y+30)) != couleur:
                principale.utilisateur.deplacement_haut()
                principale.utilisateur.deplacement_haut()
        elif principale.utilisateur.rect.x+15 > taille_fenetre - taille_carre and principale.utilisateur.rect.x < taille_fenetre and \
             principale.utilisateur.rect.y+15 > taille_fenetre - 2 * taille_carre and principale.utilisateur.rect.y < taille_fenetre - taille_carre:
                running = False
                pygame.quit()
        else:
            principale.utilisateur.deplacement_arret()



        if running:
            pygame.display.flip()
            clock.tick(60)
            for event in pygame.event.get() :
                if event.type == pygame.QUIT or counter <= 0:
                    running = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    principale.appuyee[event.key] = True
                elif event.type == pygame.KEYUP:
                    principale.appuyee[event.key] = False
                if event.type == pygame.USEREVENT:
                    counter -= 1
                    if  counter < 10:
                        text = '00:0' + str(counter)
                    else:
                        text = '00:' + str(counter)




