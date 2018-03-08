import random
NUM_INT = 10

class MinMaxQueue:
    def __init__(self, l=None):
        l.sort()
        self.sorted_q = l

    def pop_min(self):

        #perform on the min
    
        return self.sorted_q.pop(0)

    def pop_max(self):
        #perform on the max

        return self.sorted_q.pop()

def main():
    #create the lists of integers and signs, respectively
    li = [random.randint(0, 20) for i in range(NUM_INT)]
    li = list(set(li))
    sign_array = ["<" if random.randint(0, 1) else ">" for i in range(len(li) - 1)]
    mmq = MinMaxQueue(li)
    result = []
    for j in sign_array:
        if j == '<':
            result.append(mmq.pop_min())
            result.append(j)
        else:
            result.append(mmq.pop_max())
            result.append(j)
    #decide if you'd take out the min or max of the integer list
    #and append corresponding sign after it

    print(result[:-1])

main()


