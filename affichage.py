import turtle

def carre(pixel, couleur, x, y):
    turtle.fillcolor(couleur)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

    turtle.begin_fill()
    for cote in range(4):
        turtle.forward(pixel)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(pixel)


def affichage_lab(matrice):
    for i in range(len(matrice)):
        for y in range(len(matrice)):
            if matrice[i][y] == 0:
                carre(50, "yellow", (y*50)-900,(i*-50)+450)
            else:
                carre(50, "blue", (y*50)-900, (i*-50)+450)




G = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],'
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


if __name__  == "__main__":
    turtle.speed(0)
    affichage_lab(G)
    turtle.exitonclick()