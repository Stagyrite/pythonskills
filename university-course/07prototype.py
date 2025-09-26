class ExpressionUnallowedException(BaseException):

    def __str__(self):
        return "Expression is too general."


class Wyrazenie():
    def __str__(self):
        return "Expression"

    def oblicz(self, zmienne):
        raise ExpressionUnallowedException


class Stala(Wyrazenie):
    def __init__(self, value):
        self.value = value

    def oblicz(self, zmienne):
        return self.value

    def __str__(self):
        return "Constant(" + str(self.value) + ")"


class UnboundVariableException(BaseException):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Variable " + self.name + " can't be bound."


class Zmienna(Wyrazenie):
    def __init__(self, name):
        self.name = name

    def oblicz(self, zmienne):

        if self.name in zmienne:
            return zmienne[self.name]
        else:
            raise UnboundVariableException(self.name)

    def __str__(self):
        return "Variable(" + self.name + ")"


class Razy(Wyrazenie):
    def __init__(self, multiplicand: Wyrazenie, multiplier: Wyrazenie):
        self.multiplicand = multiplicand
        self.multiplier = multiplier

    def oblicz(self, zmienne):
        a = self.multiplicand.oblicz(zmienne)
        b = self.multiplier.oblicz(zmienne)
        return a * b

    def __str__(self):
        return "Multiply(" + str(self.multiplicand) + ", " + str(self.multiplier) + ")"


class Podziel(Wyrazenie):
    def __init__(self, dividend: Wyrazenie, divider: Wyrazenie):
        self.dividend = dividend
        self.divider = divider

    def oblicz(self, zmienne):
        a = self.dividend.oblicz(zmienne)
        b = self.divider.oblicz(zmienne)

        if b == 0:
            raise ZeroDivisionError

        return a / b

    def __str__(self):
        return "Divide(" + str(self.dividend) + ", " + str(self.divider) + ")"


class Dodaj(Wyrazenie):
    def __init__(self, factorA: Wyrazenie, factorB: Wyrazenie):
        self.factorA = factorA
        self.factorB = factorB

    def oblicz(self, zmienne):
        a = self.factorA.oblicz(zmienne)
        b = self.factorB.oblicz(zmienne)
        return a + b

    def __str__(self):
        return "Add(" + str(self.factorA) + ", " + str(self.factorB) + ")"


class Odejmij(Wyrazenie):
    def __init__(self, minuend: Wyrazenie, subtrahend: Wyrazenie):
        self.minuend = minuend
        self.subtrahend = subtrahend

    def oblicz(self, zmienne):
        a = self.minuend.oblicz(zmienne)
        b = self.subtrahend.oblicz(zmienne)
        return a - b

    def __str__(self):
        return "Subtract(" + str(self.minuend) + ", " + str(self.subtrahend) + ")"


# (x + 2) * y
expression = Razy(Dodaj(Zmienna("x"), Stala(2)), Zmienna("y"))

# x = 5, y = 10 => (x + 2) * y = 7 * 10 = 70
print(expression.oblicz({'x': 5, 'y': 10}))
print(expression)


class Instrukcja():
    def __str__(self):
        return "Instruction"

    def wykonaj(self, zmienne):
        None


class Przypisz(Instrukcja):
    def __init__(self, name: str, value):
        self.name = name
        self.value = value

    def wykonaj(self, zmienne):
        value = self.value.oblicz(zmienne)
        zmienne[self.name] = value
        return value

    def __str__(self):
        return "Assign(" + str(self.name) + ", " + str(self.value) + ")"


class Sekwencja(Instrukcja):
    def __init__(self, *expressions):
        self.expressions = expressions

    def wykonaj(self, zmienne):
        lastValue = None

        for expression in self.expressions:
            lastValue = expression.wykonaj(zmienne)

        return lastValue

    def __str__(self):
        toString = "Sequence("

        for expression in self.expressions:
            toString += str(expression) + ", "

        toString.removesuffix(", ")
        return toString + ")"


class Jezeli(Instrukcja):
    def __init__(self, booleanExpression: Wyrazenie, expression: Wyrazenie):
        self.booleanExpression = booleanExpression
        self.expression = expression

    def wykonaj(self, zmienne):
        a = self.booleanExpression.oblicz(zmienne)

        if a == 0:
            retValue = None
        else:
            retValue = self.expression.oblicz(zmienne)

        return retValue

    def __str__(self):
        return "If(" + str(self.booleanExpression) + ", " + str(self.expression) + ")"


class Dopoki(Instrukcja):
    def __init__(self, booleanExpression: Wyrazenie, expression: Wyrazenie):
        self.booleanExpression = booleanExpression
        self.expression = expression

    def wykonaj(self, zmienne):
        lastValue = None

        while self.booleanExpression.oblicz(zmienne) != 0:
            lastValue = self.expression.wykonaj(zmienne)

        return lastValue

    def __str__(self):
        return "While(" + str(self.booleanExpression) + ", " + str(self.expression) + ")"


program = Sekwencja(
    Przypisz("x", Stala(5)),
    Przypisz("y", Stala(10)),
    Jezeli(Stala(1), expression),
    Dopoki(Zmienna("x"),
           Sekwencja(Przypisz("x", Odejmij(Zmienna("x"), Stala(1))),
                     Przypisz("y", Dodaj(Zmienna("y"), Stala(2))))))
print(program)
print(program.wykonaj({}))
