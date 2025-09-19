def sum_eo(n, t):
    result = 0

    if t == 'e':

        for i in range(0, n):

            if i % 2 == 0:
                result += i

    elif t == 'o':

        for i in range(0, n):

            if i % 2 == 1:
                result += i

    else:
        result = -1

    return result

# One can consider using the step argument.

print(sum_eo(10, 'e') == 20)
print(sum_eo(7, 'o') == 9)
print(sum_eo(11, 'spam') == -1)
