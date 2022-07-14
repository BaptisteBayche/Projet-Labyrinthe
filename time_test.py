import generation_matrice
import random
import Piles


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


ch = creation_chemin(5)


def matrice(chemin, taille):
    labyrinthe = [[0 for j in range(2 * taille + 1)] for i in range(2 * taille + 1)]

    for i, j in chemin:
        print(i,j)
        labyrinthe[2 * i + 1][2 * j + 1] = 1
        if (i, j) != (0, 0):
            k, l = chemin[(i, j)]
            print("==" + str(k) +" " + str(l))
            labyrinthe[2 * k + 1][2 * l + 1] = 1
            labyrinthe[i + k + 1][j + l + 1] = 1

    labyrinthe[1][0] = 1
    labyrinthe[2 * taille - 1][2 * taille] = 1

    for i in labyrinthe:
        print(i)

matrice(ch,5)
