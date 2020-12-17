"""
Tree Function (Cette fonction décrit la forme des branches du sapin de Noël)
"""
def print_tree(n1, n2, n3, n4):
    for tree in range(1, n1, 2):
        print((tree * "*").center(23))
    for tree in range(1, n2, 2):
        print(((tree * "0")+(1 * " ")+(3 * "*")+(1 * " ")+(tree * "0")).center(23))
    for tree in range(7, n3, 4):
        print((tree * "*").center(23))
    for tree in range(1, n2, 2):
        print(((tree * "0")+(4 * " ")+(5 * "*")+(4 * " ")+(tree * "0")).center(23))
    for tree in range(11, n4, 6):
        print((tree * "*").center(23))
print_tree(8, 2, 16, 24)

"""
Trunk Function (Cette fonction décrit la forme du tronc du sapin de Noël)
"""
def print_trunk(n1, n2, n3):
    for trunk in range(5, n1, 20):
        print(((4 * "| ")+(5 * "*")+(4 * " |")).center(23))
    for trunk in range(5, n2, 20):
        print(((4 * "0 ")+(5 * "*")+(4 * " 0")).center(23))
    for trunk in range(5, n3, 20):
        print((5* "*").center(23))      
print_trunk(20, 20, 20)