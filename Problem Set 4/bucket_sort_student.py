import random
random.seed(0)


def bucket_sort(mylist):
    # initialize the buckets
    result = []# place the values to be sorted in the buckets
    mydict = {}
    for i in mylist:
        try:
            mydict[i // 10] += [i]
        except KeyError:
            mydict[i // 10] = [i]
    for key in sorted(mydict.keys()):
        mydict[key].sort()
        result += mydict[key]
    # sort each bucket
    # concatenate your bucket to the result
    return result


def main():
    """ this is not exactly relevant, but the following 4 lines of
    code can be replaced by one line:
    list_a = [random.randint(0, 1000) for i in range(100)]
    """
    list_a = []
    for i in range(1000):
        list_a.append(random.randint(0,100))
    print(list_a)

    list_a = bucket_sort(list_a)
    print("SORTED:", list_a)    


main()
