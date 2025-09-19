def zaszyfruj(tekst, klucz):
    encoded = ''

    for c in tekst:
        encoded += chr(ord(c) ^ klucz)

    return encoded

def odszyfruj(szyfr, klucz):
    return zaszyfruj(szyfr, klucz)

# print 'Python' encoded
print(zaszyfruj("Python", 7))

# print 'Python' decoded
print(odszyfruj("W~sohi", 7))
