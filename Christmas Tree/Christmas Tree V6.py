# -- coding: utf-8 --
#Christmas Tree
#Lysandre LE BIGOT et Jérémy BARRE
#17/12/2020
#Python 3.7.9 (64-bit)

toplevel = int(input("Entrez la taille du premier étage : "))
middlelevel = int(input("Entrez la taille du second étage : "))
bottomlevel = int(input("Entrez la taille du troisième étage : "))
topgarlands = int(((toplevel//2.5)-1.5)*1.14)
middlegarlands = int(((middlelevel//2.5)-2)*1.14)
bottomgarlands = int((bottomlevel - 6)//4)

"""
Star Function (Cette fonction décrit la forme de l'étoile du sapin de Noël)
"""
def print_star(): 
    print(((1 * "*")+(4 * " ")+(1 * "*")+(4 * " ")+(1 * "*")).center(bottomlevel))
    print(((1 * "*")+(2 * " ")+(1 * "*")+(2 * " ")+(1 * "*")).center(bottomlevel))
    print((1 * "*").center(bottomlevel))
    print((6 * "* ").center(bottomlevel))
    print((1 * "*").center(bottomlevel))
    print(((1 * "*")+(2 * " ")+(1 * "|")+(2 * " ")+(1 * "*")).center(bottomlevel))
    print(((1 * "*")+(4 * " ")+(1 * "|")+(4 * " ")+(1 * "*")).center(bottomlevel))

"""
Tree Function (Cette fonction décrit la taille des branches du sapin de Noël)
"""
def print_tree(n1, n2, n3, n4):
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
Trunk Function (Cette fonction décrit la taille du tronc du sapin de Noël)
"""
def print_trunk(n):
    for size in range(5, n, 20):
        print((((bottomgarlands * "| ")+(5 * "*")+(bottomgarlands * " |")).center(bottomlevel)))
    for size in range(5, n, 15):
        print(((bottomgarlands * "0 ")+(5 * "*")+(bottomgarlands * " 0")).center(bottomlevel))
    for size in range(5, n, 20):
        print((5* "*").center(bottomlevel))

print_star()      
print_tree(toplevel, 2, middlelevel, bottomlevel)
print_trunk(20)