def sum_numbers(*args : float) -> float:
    """
    Sum a number of arguments. It takes and returns float numbers.

    :param args: the numbers
    :return: the sum of it
    """
    sum = 0

    for num in args:
        sum += num

    return sum

print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
