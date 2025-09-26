
def rozklad(n):
    result = []
    current = n

    for i in range(2, n + 1):

        if i * i > n:
            break

        how_many = 0

        while current % i == 0:
            current //= i
            how_many += 1

        if how_many > 0:
            result.append((i, how_many))

    return result

print(rozklad(756))
