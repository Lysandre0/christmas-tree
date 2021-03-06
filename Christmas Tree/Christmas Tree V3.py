# -- coding: utf-8 --
"""
Christmas Tree
Lysandre LE BIGOT et Jérémy BARRE
17/12/2020
Python 3.7.9 (64-bit)
"""

"""
INPUT: 3 entier n1,n2,n3
OUTPUT: Une chaine de symbole représentant les 3 étages du sapin
"""
def tree(n1, n2, n3):
    for size in range(1, n1, 2):
        print((size * "*").center(23))
    for size in range(3, n2, 4):
        print((size * "*").center(23))
    for size in range(5, n3, 6):
        print((size * "*").center(23))
tree(8, 16, 24)

"""
INPUT: 1 nombre entier n
OUTPUT:Une chaine de symbole représentant les trois partis du sapin ainsi que les guirlandes
"""
def trunk(n1, n2, n3):
    for size in range(5, n1, 20):
        print(((4 * "| ")+(5 * "*")+(4 * " |")).center(23))
    for size in range(5, n2, 20):
        print(((4 * "0 ")+(5 * "*")+(4 * " 0")).center(23))
    for size in range(5, n3, 20):
        print((5* "*").center(23))
trunk(20, 20, 20)