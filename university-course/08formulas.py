class FormulaUnallowedException(BaseException):

    def __str__(self):
        return "Formula is too general."


class Formula():
    def __str__(self):
        return "Formula"

    def oblicz(self, zmienne):
        raise FormulaUnallowedException

class ConstantTrue(Formula):
    def __str__(self):
        return "Constant True"

    def oblicz(self, zmienne):
        return True

class ConstantFalse(Formula):
    def __str__(self):
        return "Constant False"

    def oblicz(self, zmienne):
        return False

class UnboundVariableException(BaseException):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Variable " + self.name + " can't be bound."


class Zmienna(Formula):
    def __init__(self, name):
        self.name = name

    def oblicz(self, zmienne):

        if self.name in zmienne:
            return zmienne[self.name]
        else:
            raise UnboundVariableException(self.name)

    def __str__(self):
        return "Variable(" + self.name + ")"

class Impl(Formula):
    def __init__(self, protasis: Formula, apodosis: Formula):
        self.protasis = protasis
        self.apodosis = apodosis

    def oblicz(self, zmienne):
        a = self.protasis.oblicz(zmienne)
        b = self.apodosis.oblicz(zmienne)
        return not a or b

    def __str__(self):
        return "Implication(" + str(self.protasis) + ", " + str(self.apodosis) + ")"

class And(Formula):
    def __init__(self, conjunctA: Formula, conjunctB: Formula):
        self.conjunctA = conjunctA
        self.conjunctB = conjunctB

    def oblicz(self, zmienne):
        a = self.conjunctA.oblicz(zmienne)
        b = self.conjunctB.oblicz(zmienne)
        return a and b

    def __str__(self):
        return "Conjunction(" + str(self.conjunctA) + ", " + str(self.conjunctB) + ")"

class Or(Formula):
    def __init__(self, disjunctA: Formula, disjunctB: Formula):
        self.disjunctA = disjunctA
        self.disjunctB = disjunctB

    def oblicz(self, zmienne):
        a = self.disjunctA.oblicz(zmienne)
        b = self.disjunctB.oblicz(zmienne)
        return a or b

    def __str__(self):
        return "Conjunction(" + str(self.disjunctA) + ", " + str(self.disjunctB) + ")"

class Not(Formula):
    def __init__(self, formula: Formula):
        self.formula = formula

    def oblicz(self, zmienne):
        p = self.formula.oblicz(zmienne)
        return not p

    def __str__(self):
        return "Not(" + str(self.formula) + ")"

expression = Impl(Zmienna("x"), And(Zmienna("y"), ConstantTrue()))
print(expression)
print(expression.oblicz({ 'x' : True, 'y' : False}))

def isTautology(formula, variables, depth=0, assignment={}):

    if depth == len(variables):
        return formula.oblicz(assignment)

    variableName = variables[depth]
    assignment[variableName] = False
    deeper = depth + 1

    if not isTautology(formula, variables, deeper, assignment):
        return False

    assignment[variableName] = True
    return isTautology(formula, variables, deeper, assignment)

print(isTautology(expression, ["x", "y"]))
expression = Or(Impl(Zmienna("x"), Zmienna("y")), Impl(Zmienna("x"), Not(Zmienna("y"))))
print(isTautology(expression, ["x", "y"]))
