def find_shortest(stops):
    li_x = []
    li_y = []

    for i in stops:
        li_x.append(i[0])
        li_y.append(i[1])

    x_min = min(li_x)
    x_max = max(li_x)
    y_min = min(li_y)
    y_max = max(li_y)

    final = {}

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            for j in stops:
                sum = abs(x - j[0]) + abs(y - j[1])
                if sum in final.keys():
                    final[sum].append([x , y])
                else:
                    final[sum] = [[x , y]]

    shortest = sorted(final)[0]
    return final[shortest]

def main():
    stops = [[1, 3], [2, 4], [3, 5], [4, 6]]
    print(find_shortest(stops))

main()