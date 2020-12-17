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
def print_trunk(n):
    for size in range(n):
        print((5 * "*").center(23))
print_trunk(3)