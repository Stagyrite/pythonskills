def tabliczka(x1, x2, y1, y2):
    max = x2 * y2
    width = len(str(max)) + 1

    for y in range(y1, y2 + 1):

        if y == 1:
            print(' ' * width, end='')
        else:
            print(f"{y:>{width}}", end='')

        for x in range(x1, x2 + 1):
            print(f"{str(x * y):>{width}}", end='')

        print('')

tabliczka(1, 9, 1, 5)
