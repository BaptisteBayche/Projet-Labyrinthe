def matrice(chemin, taille):
    labyrinthe = [[0 for j in range(2 * taille + 1)] for i in range(2 * taille + 1)]

    for i, j in chemin:
        labyrinthe[2 * i + 1][2 * j + 1] = 1
        if (i, j) != (0, 0):
            k, l = chemin[(i, j)]
            labyrinthe[2 * k + 1][2 * l + 1] = 1
            labyrinthe[i + k + 1][j + l + 1] = 1

    labyrinthe[1][0] = 1
    labyrinthe[2 * taille - 1][2 * taille] = 1

    return labyrinthe