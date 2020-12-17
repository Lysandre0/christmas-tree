"""
Tree Function (Cette fonction décrit la forme des branches du sapin de Noël)
"""
def print_tree(n1, n2, n3):
    for size in range(1, n1, 2):
        print((size * "*").center(23))
    for size in range(3, n2, 4):
        print((size * "*").center(23))
    for size in range(5, n3, 6):
        print((size * "*").center(23))
print_tree(8, 16, 24)

"""
Trunk Function (Cette fonction décrit la forme du tronc du sapin de Noël)
"""
def print_trunk(n1, n2, n3):
    for size in range(5, n1, 20):
        print(((4 * "| ")+(5 * "*")+(4 * " |")).center(23))
    for size in range(5, n2, 20):
        print(((4 * "0 ")+(5 * "*")+(4 * " 0")).center(23))
    for size in range(5, n3, 20):
        print((5* "*").center(23))
print_trunk(20, 20, 20)