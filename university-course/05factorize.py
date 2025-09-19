
def rozklad(n):
    result = []
    current = n

    for i in range(2, n + 1):

        if i * i > n:
            break

        howMany = 0

        while current % i == 0:
            current //= i
            howMany += 1

        if howMany > 0:
            result.append((i, howMany))

    return result

print(rozklad(756))
