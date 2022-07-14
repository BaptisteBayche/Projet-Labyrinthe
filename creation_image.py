# Créé par FAUX Clément, le 10/02/2021 en Python 3.7
from PIL import Image
from random import randint
import options




couleur_1 = [randint(0,255),randint(0,255),randint(0,255)]
couleur_2 = [randint(0,255),randint(0,255),randint(0,255)]
couleur_3 = [randint(0,255),randint(0,255),randint(0,255)]

def get_couleur():
    return couleur_2

def get_couleur2():
    return couleur_2


def carre(x ,y, nb_px, couleur, im):
    for i in range(nb_px):
        for j in range(nb_px):
            im.putpixel((x+i,y+j),couleur)

def image(largeur, hauteur, matrice, nom_image, longueur_carre, im, solution = False):
    y = 0
    for a in range(len(matrice)):
        ym = y//longueur_carre
        xm = 0
        x = 0
        for b in range(len(matrice[0])):
            if matrice[ym][xm] == 1:
                if solution == False:
                    carre(x,y,longueur_carre,(couleur_2[0],couleur_2[1],couleur_2[2]), im)
                else:
                    carre(x+10,y+10,longueur_carre-20,(couleur_3[0],couleur_3[1],couleur_3[2]), im)
            x += longueur_carre
            xm += 1
        y += longueur_carre
    im.save("images/"+nom_image+".png","png")


def creer_image(matrice, matrice_sol):
    longueurm = options.get_taille_carre()
    largeur = longueurm*len(matrice)
    hauteur = longueurm*len(matrice)
    taille_image = options.get_taille_fenetre()
    im = Image.new('RGB',(taille_image, taille_image),(couleur_1[0], couleur_1[1], couleur_1[2]))
    im.save("images/fond"+".png","png")
    image(largeur, hauteur, matrice, "background", longueurm, im)
    image(largeur, hauteur, matrice_sol, "background_sol", longueurm, im, True)


