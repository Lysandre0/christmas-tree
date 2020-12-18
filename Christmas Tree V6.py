# -- coding: utf-8 --
#Christmas Tree
#Lysandre LE BIGOT et Jérémy BARRE
#17/12/2020
#Python 3.7.9 (64-bit)

toplevel = int(input("Entrez la taille du premier étage : "))
middlelevel = int(input("Entrez la taille du second étage : "))
bottomlevel = int(input("Entrez la taille du troisième étage : "))
topgarlands = int((toplevel)//2.6)
middlegarlands = int((middlelevel)//2.6)
bottomgarlands = int((bottomlevel - 5)//4)

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
    for tree in range(1, n1, 2):
        print((tree * "*").center(bottomlevel))
    for tree in range(1, n2, 2):
        print(((tree * "0")+(topgarlands * " ")+(3 * "*")+(topgarlands * " ")+(tree * "0")).center(bottomlevel))
    for tree in range(7, n3, 4):
        print((tree * "*").center(bottomlevel))
    for tree in range(1, n2, 2):
        print(((tree * "0")+(middlegarlands * " ")+(5 * "*")+(middlegarlands * " ")+(tree * "0")).center(bottomlevel))
    for tree in range(11, n4, 6):
        print((tree * "*").center(bottomlevel))

"""
Trunk Function (Cette fonction décrit la taille du tronc du sapin de Noël)
"""
def print_trunk(n):
    for trunk in range(5, n, 20):
        print((((bottomgarlands * "| ")+(5 * "*")+(bottomgarlands * " |")).center(bottomlevel)))
    for trunk in range(5, n, 20):
        print(((bottomgarlands * "0 ")+(5 * "*")+(bottomgarlands * " 0")).center(bottomlevel))
    for trunk in range(5, n, 20):
        print((5* "*").center(bottomlevel))

print_star()      
print_tree(toplevel, 2, middlelevel, bottomlevel)
print_trunk(20)