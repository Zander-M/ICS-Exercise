import random

random.seed(0)

SIZE = 10
LOGGING = True


class PancakeStack:
    def __init__(self, stack=None):
        self.stack = stack

    def get_size(self):
        return len(self.stack)

    # All of the pancakes are sorted after index
    # Returns the index of largest unsorted pancake
    def find_smallest_pancake(self, index):
        smallest_index = index
        smallest = self.stack[index]
        for i in range(index):
            if self.stack[i] < smallest:
                smallest = self.stack[i]
                smallest_index = i
        #write your code here

        return smallest_index

    # Slide the pan under pancake at desired index and flip to top
    def flip(self, index):
        #write your code here
        self.stack = self.stack[index::-1] + self.stack[index+1:]
        return

def sort_pancakes(pancakes):
    pancakes_size = pancakes.get_size()
    for i in reversed(range(pancakes_size)):
        flip_index = pancakes.find_smallest_pancake(i)
        pancakes.flip(flip_index)
        if LOGGING: print("Flip Up", pancakes.stack)
        pancakes.flip(i)
        if LOGGING: print("Flip Down", pancakes.stack)
    return pancakes.stack


if __name__ == "__main__":
    my_stack = random.sample(range(1, 20), SIZE)
    print("Unsorted pancakes:", my_stack)
    case_one = PancakeStack(my_stack)
    print("Final order of pancakes: ", sort_pancakes(case_one))

