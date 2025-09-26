def pay(how_much):

    for amount in (20, 10, 5, 2, 1):
        amountSpent = how_much // amount

        if amountSpent > 0:
            print(amount, " x ", amountSpent)
            how_much %= amount

pay(123)
