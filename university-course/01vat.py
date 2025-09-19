VAT = 0.23

def vat_faktura(lista):
    return sum(lista) * VAT

def vat_paragon(lista):
    sum = 0

    for x in lista:
        sum += x * VAT

    return sum

zakupy = [0.2, 0.5, 4.59, 6]
print(vat_faktura(zakupy) == vat_paragon(zakupy))
