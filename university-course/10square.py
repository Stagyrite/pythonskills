# Square root and floor a number

def square_floor(n):
    """
    Computes a square root of a given number
    and return its floor.

    :param n: a number
    :return: the floor of the square root
    """
    current_sum = 0
    result = 0
    addend = 1

    while current_sum + addend <= n:
        current_sum += addend
        result += 1
        addend = 2 * result + 1

    return result

print(square_floor(1500100900))
