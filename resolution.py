import Piles
import options

def creation_graphe(coord):
    arbre = {}
    for i, j in coord.items():
        if i != (0, 0):
            if j not in arbre:
                arbre[j] = [i]
            else:
                arbre[j] = arbre[j] + [i]
    return arbre


def cherche_chemin(coord):
    graphe = creation_graphe(coord)
    chemin_final = []
    coord_chemin = {}
    depart = (0, 0)
    c_arrive = options.get_taille()-1
    arrivee = (c_arrive, c_arrive)
    pile = Piles.Pile()
    pile.empiler((depart, [depart]))
    while not pile.estVide():
        sommet, chemin = pile.depiler()
        if sommet in graphe:
            liste_nouveaux_sommets_voisins = [voisin for voisin in graphe[sommet] if not (voisin in chemin)]
            for voisin in liste_nouveaux_sommets_voisins:
                if voisin == arrivee:
                    chemin_final =  chemin + [arrivee]
                pile.empiler((voisin, chemin + [voisin]))
    for i, j in coord.items():
        if i in chemin_final:
            coord_chemin[i] = j
    return coord_chemin



