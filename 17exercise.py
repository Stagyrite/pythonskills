def factorial(number : int):
    """
    Computes a factorial for a given number.

    :param number: the number
    :return: its factorial
    """

    result = 1

    for i in range(2, number + 1):
        result *= i

    return result

for i in range(1, 36):
    print("{} {}".format(i, factorial(i)))
