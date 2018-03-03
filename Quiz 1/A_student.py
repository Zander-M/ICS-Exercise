
def print_one_unit(sym_array):
    ls = ''
    for i in sym_array:
        ls += i
    print(ls, end='')
    return


def print_triangle(n, a_block=['*']):
    for i in range(n):
        i += 1
        for j in range(i) :
            print_one_unit(a_block)
        print("\n")

print_triangle(4)
print_triangle(5, a_block=['o', 'r', 'z'])
print_triangle(6, a_block=['/', '_', '\\', ' '])

