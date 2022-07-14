#Class Pile permettant de crée une pile.
class Pile:
    def __init__(self):
        self.pile = []

    def estVide(self):
        return self.pile == []

    def empiler(self, element):
        self.pile.append(element)

    def depiler(self):
        return self.pile.pop()

    def lireSommet(self):
        return self.pile[-1]


