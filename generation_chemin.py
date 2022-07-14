import Piles
import random


def voisin(coordonnee, taille):
    listeVoisins = []
    i, j = coordonnee[0], coordonnee[1]
    # Pourcours l'intervalle [-1; 2] de 2 en 2.
    for d in range(-1, 2, 2):
        if -1 < i + d and i + d < taille:
            listeVoisins.append((i + d, j))
        if -1 < j + d and j + d < taille:
            listeVoisins.append((i, j + d))
    return listeVoisins


def creation_chemin(taille):
    P = {(0, 0): (0, 0)}
    Q = Piles.Pile()
    Q.empiler((0, 0))
    while not (Q.estVide()):
        print("P: " + str(P))
        print("Q: " + str(Q))
        u = Q.lireSommet()
        print("u: " + str(u))
        R = [y for y in voisin(u, taille) if y not in P]
        if R:
            print("R: " + str(R))
            v = random.choice(R)
            P[v] = u
            print("P: " + str(P))
            Q.empiler(v)
        else:
            Q.depiler()
        print("Q: " + str(Q))
        print("===\n===")
    return P
