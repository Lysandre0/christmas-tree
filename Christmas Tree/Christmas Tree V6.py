# -- coding: utf-8 --
"""
Christmas Tree
Lysandre LE BIGOT et Jérémy BARRE
17/12/2020
Python 3.7.9 (64-bit)
"""

toplevel = int(input("Entrez la taille du premier étage : "))
#toplevel prend en paramètre la taille du 1er étage
middlelevel = int(input("Entrez la taille du second étage : "))
#middlelevel prend en paramètre la taille du 2ème étages
bottomlevel = int(input("Entrez la taille du troisième étage : "))
<<<<<<< HEAD
#bottomlevel prend en paramètre la taille du 3ème étages
topgarlands = int(((toplevel//2.5)-1)*1.14)
#topgarlands est un calcul configurant les boules du 1ère étage
middlegarlands = int(((middlelevel//2.5)-1)*1.14)
#middlegarlands est un calcul configurant les boules du 2ème étages
bottomgarlands = int((bottomlevel - 5)//4 - 1)
#bottomgarlands est un calcul configurant la guirlande du 3ème étages

=======
topgarlands = int(((toplevel//2.5)-1.5)*1.14)
middlegarlands = int(((middlelevel//2.5)-2)*1.14)
bottomgarlands = int((bottomlevel - 6)//4)
>>>>>>> eb7b7e001789b24ad0e44c76b33cd9724c22f7c2

"""
INPUT: 
OUTPUT:Une chaine de symbole représentant l'étoile de la mort
"""
def star(): 
    print(((1 * "*")+(4 * " ")+(1 * "*")+(4 * " ")+(1 * "*")).center(bottomlevel))
    print(((1 * "*")+(2 * " ")+(1 * "*")+(2 * " ")+(1 * "*")).center(bottomlevel))
    print((1 * "*").center(bottomlevel))
    print((6 * "* ").center(bottomlevel))
    print((1 * "*").center(bottomlevel))
    print(((1 * "*")+(2 * " ")+(1 * "|")+(2 * " ")+(1 * "*")).center(bottomlevel))
    print(((1 * "*")+(4 * " ")+(1 * "|")+(4 * " ")+(1 * "*")).center(bottomlevel))

"""
INPUT: 4 entier n1,n2,n3,n4
OUTPUT:Une chaine de symbole représentant les trois partis du sapin ainsi que les boules
"""
def tree(n1, n2, n3, n4):
    for size in range(1, n1, 2):
        print((size * "*").center(bottomlevel))
    for size in range(1, n2, 2):
        print(((size * "0")+(topgarlands * " ")+(3 * "*")+(topgarlands * " ")+(size * "0")).center(bottomlevel))
    for size in range(7, n3, 4):
        print((size * "*").center(bottomlevel))
    for size in range(1, n2, 2):
        print(((size * "0")+(middlegarlands * " ")+(5 * "*")+(middlegarlands * " ")+(size * "0")).center(bottomlevel))
    for size in range(11, n4, 6):
        print((size * "*").center(bottomlevel))

"""
INPUT: 3 entier n1,n2,n3
OUTPUT:Une chaine de symbole représentant le tronc avec les guirlandes
"""
def trunk(n):
    for size in range(5, n, 20):
        print((((bottomgarlands * "| ")+(5 * "*")+(bottomgarlands * " |")).center(bottomlevel)))
    for size in range(5, n, 15):
        print(((bottomgarlands * "0 ")+(5 * "*")+(bottomgarlands * " 0")).center(bottomlevel))
    for size in range(5, n, 20):
        print((5* "*").center(bottomlevel))

star()      
tree(toplevel, 2, middlelevel, bottomlevel)
trunk(20)