def fizz_buzz(number : int):
    """
    Returns a value corresponding to the result of the
    well-known Fizz Buzz game.

    :param number: the number
    :return: the Fizz Buzz game result
    """

    if number % 3 == 0:

        if number % 5 == 0:
            retValue = "fizz buzz"
        else:
            retValue = "fizz"

    elif number % 5 == 0:
        retValue = "buzz"
    else:
        retValue = str(number)

    return retValue

for i in range(1, 101):
    print(fizz_buzz(i))
