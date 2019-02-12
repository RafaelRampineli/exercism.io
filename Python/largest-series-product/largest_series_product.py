from functools import reduce


def largest_product(series, size):
    if size < 0:
        raise ValueError("Negative Number")
    elif len(series) < size:
        raise ValueError("Size sequence bigger than series")
    elif len(series) == 0 or size <= 0:
        return 1

    list1 = list(map(int, series))
    listfinal = list()

    while len(list1) >= size:
        result1 = reduce((lambda x, y: x * y), list1[slice(0, size, 1)]) # For each value in list, does a multiplication; slice is used to througt over list in limit range
        listfinal.append(result1)
        list1 = list1[1:]
        print(listfinal)

    return max(listfinal)




