# Sudan function with memoization
from functools import cache

@cache
def sudan(n, x, y):
    """
    Computes a value of the Sudan function for the given parameters.

    :param n: the 'n' parameter
    :param x: the 'x' parameter
    :param y: the 'y' parameter
    :return: the value of the Sudan function
    """

    if n == 0:
        return x + y
    elif y == 0:
        return x
    else:
        value = sudan(n, x, y - 1)
        return sudan(n - 1, value, value + y)

print(sudan(2, 1, 2))
