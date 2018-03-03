N = 4


def sort_digit(d):
    ls = []
    ls.append(d // 100)
    ls.append((d - ls[0] * 100) // 10)
    ls.append(d - d // 10 * 10)
    ls.sort()
    num2 = ''.join(str(i) for i in ls)
    num1 = ''.join(str(j) for j in ls[:: -1])
    num2 = '{:<04}'.format(num2)
    print(int(num1), int(num2))
    return

def find_black_hole(x):
    return 42
sort_digit(324)

print(sort_digit(231))
print('Black hole = {}\n'.format(find_black_hole(231)))
print('Black hole = {}\n'.format(find_black_hole(111)))
