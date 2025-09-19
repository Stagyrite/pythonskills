def pay(howMuch):

    for amount in (20, 10, 5, 2, 1):
        amountSpent = howMuch // amount

        if amountSpent > 0:
            print(amount, " x ", amountSpent)
            howMuch %= amount

pay(123)
