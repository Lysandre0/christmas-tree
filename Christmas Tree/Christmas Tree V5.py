# -- coding: utf-8 --
"""
Christmas Tree
Lysandre LE BIGOT et Jérémy BARRE
17/12/2020
Python 3.7.9 (64-bit)
"""
INPUT: 
OUTPUT:Une chaine de symbole représentant l'étoile de la mort
"""
Star Function (Cette fonction décrit la forme de l'étoile du sapin de Noël)
"""
def star(): 
    print(((1 * "*")+(4 * " ")+(1 * "*")+(4 * " ")+(1 * "*")).center(23))
    print(((1 * "*")+(2 * " ")+(1 * "*")+(2 * " ")+(1 * "*")).center(23))
    print((1 * "*").center(23))
    print((6 * "* ").center(23))
    print((1 * "*").center(23))
    print(((1 * "*")+(2 * " ")+(1 * "|")+(2 * " ")+(1 * "*")).center(23))
    print(((1 * "*")+(4 * " ")+(1 * "|")+(4 * " ")+(1 * "*")).center(23))

"""
INPUT: 4 entier n1,n2,n3,n4
OUTPUT:Une chaine de symbole représentant les trois partis du sapin ainsi que les boules
"""
def tree(n1, n2, n3, n4):
    for size in range(1, n1, 2):
        print((size * "*").center(23))
    for size in range(1, n2, 2):
        print(((size * "0")+(1 * " ")+(3 * "*")+(1 * " ")+(size * "0")).center(23))
    for size in range(7, n3, 4):
        print((size * "*").center(23))
    for size in range(1, n2, 2):
        print(((size * "0")+(4 * " ")+(5 * "*")+(4 * " ")+(size * "0")).center(23))
    for size in range(11, n4, 6):
        print((size * "*").center(23))

"""
INPUT: 4 entier n1,n2,n3
OUTPUT:Une chaine de symbole représentant le tronc avec les guirlandes
"""
def trunk(n1, n2, n3):
    for trunk in range(5, n1, 20):
        print(((4 * "| ")+(5 * "*")+(4 * " |")).center(23))
    for trunk in range(5, n2, 20):
        print(((4 * "0 ")+(5 * "*")+(4 * " 0")).center(23))
    for trunk in range(5, n3, 20):
        print((5* "*").center(23))

star()      
tree(8, 2, 16, 24)
trunk(20, 20, 20)