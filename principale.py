# Créé par FAUX Clément, le 10/02/2021 en Python 3.7
import pygame
from utilisateur import Utilisateur

class Principale():
    def __init__(self):
        self.utilisateur = Utilisateur()
        self.appuyee = {}
    def get_utilisateur(self):
        return self.utilisateur
