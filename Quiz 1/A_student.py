
def print_one_unit(sym_array):
    # replace the line below
    print(''.join(sym_array), end='')

def print_triangle(n, a_block=['*']):
    for i in range(n):
        for j in range(i + 1):
            print_one_unit(a_block)
        print_one_unit(['\n'])

print_triangle(4)
print_triangle(5, a_block=['o', 'r', 'z'])
print_triangle(6, a_block=['/', '_', '\\', ' '])

