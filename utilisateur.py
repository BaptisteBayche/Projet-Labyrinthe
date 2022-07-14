# Créé par FAUX Clément, le 10/02/2021 en Python 3.7
import pygame
import options
class Utilisateur(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.deplacement = options.get_vitesse_deplacement()
        self.personnage = options.get_indexPerso()
        self.image = pygame.image.load('images/Personnage'+str(self.personnage)+'_arret.png')

        self.rect = self.image.get_rect()
        self.rect.y = options.get_taille_carre() + (options.get_taille_carre()//8)



    def deplacement_droite(self):
        self.rect.x += self.deplacement
        self.image = pygame.image.load('images/Personnage'+str(self.personnage)+'_droite.png')

    def deplacement_gauche(self):
        self.rect.x -= self.deplacement
        self.image = pygame.image.load('images/Personnage'+str(self.personnage)+'_gauche.png')
    def deplacement_haut(self):
        self.rect.y -= self.deplacement
        self.image = pygame.image.load('images/Personnage'+str(self.personnage)+'_haut.png')
    def deplacement_bas(self):
        self.rect.y += self.deplacement
        self.image = pygame.image.load('images/Personnage'+str(self.personnage)+'_bas.png')
    def deplacement_arret(self):
        self.image = pygame.image.load('images/Personnage'+str(self.personnage)+'_arret.png')
