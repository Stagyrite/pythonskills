def romb_half(n, start, stop, step):
    height = 2 * n - 1

    for i in range(start, stop, step):
        print(("#" * i).center(height))

def romb(n):
    n += 1
    height = 2 * n - 1
    romb_half(n, 1, height + 1, 2)
    romb_half(n, height - 2, 0, -2)

romb(4)
