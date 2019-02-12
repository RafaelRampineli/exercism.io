global total


def square_of_sum(count):
    total = 0

    # Python range start on 0
    for number in range(count+1):
        if number > 0:
            total += number

    return total*total


def sum_of_squares(count):
    total = 0

    for number in range(count+1):
        if number > 0:
            total += number * number

    return total


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
