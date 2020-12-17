def print_tree1(n):
    for size in range(1, n, 2):
        print((size * "*").center(23))
print_tree1(8)

def print_tree2(n):
    for size in range(3, n, 4):
        print((size * "*").center(23))
print_tree2(16)

def print_tree3(n):
    for size in range(5, n, 6):
        print((size * "*").center(23))
print_tree3(24)

def print_trunk(n):
    for size in range(n):
        print((5 * "*").center(23))
print_trunk(3)

