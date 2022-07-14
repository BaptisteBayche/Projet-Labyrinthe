fichier_r = open("option.txt", "r")


ligne = fichier_r.readlines()




def lire(ligne):
    i = 0
    while ligne[i] != ":":
        i = i + 1
    return ligne[i+1:]


def replace(ligne, replace):
    i = 0
    while ligne[i] != ":":
        i = i + 1
    remplacer = ligne[:i+1] + replace +"\n"
    return remplacer



def get_taille():
    return int(lire(ligne[0]))


def set_taille(taille):
    fichier_w = open("option.txt", "w")
    ligne[0] = replace(ligne[0], str(taille))
    fichier_w.writelines(ligne)
    fichier_w.close()
    fichier_r.close()

def get_score(niveau):
    return lire(ligne[niveau][:-1])

def get_indexPerso():
    return int(lire(ligne[4][:-1]))

def get_taille_fenetre():
    return int(lire(ligne[5][:-1]))

def get_taille_carre():
    return int(lire(ligne[6][:-1]))

def get_vitesse_deplacement():
    return int(lire(ligne[7][:-1]))

def get_musique():
    return str(lire(ligne[8][:-1]))


def set_taille_fenetre(taille):
    fichier_w = open("option.txt", "w")
    ligne[5] = replace(ligne[5], str(taille))
    fichier_w.writelines(ligne)
    fichier_w.close()
    fichier_r.close()

def set_taille_carre(taille):
    fichier_w = open("option.txt", "w")
    ligne[6] = replace(ligne[6], str(taille))
    fichier_w.writelines(ligne)
    fichier_w.close()
    fichier_r.close()


def set_indexPerso(index):
    fichier_w = open("option.txt", "w")
    ligne[4] = replace(ligne[4], str(index))
    fichier_w.writelines(ligne)
    fichier_w.close()
    fichier_r.close()

def set_vitesse_deplacement(taille):
    fichier_w = open("option.txt", "w")
    ligne[7] = replace(ligne[7], str(taille))
    fichier_w.writelines(ligne)
    fichier_w.close()
    fichier_r.close()

def set_record(record, niveau):
    fichier_w = open("option.txt", "w")
    ligne[niveau] = replace(ligne[niveau], str(record))
    fichier_w.writelines(ligne)
    fichier_w.close()
    fichier_r.close()

def set_musique(statut):
    fichier_w = open("option.txt", "w")
    ligne[8] = replace(ligne[8], str(statut))
    fichier_w.writelines(ligne)
    fichier_w.close()
    fichier_r.close()





fichier_r.close()
