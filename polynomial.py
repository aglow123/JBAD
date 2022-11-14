class Polynomial:
    def __init__(self, n, factors):
        self.n = n  # stopien wielomianu
        self.factors = factors

    def __str__(self):
        polynomial = ""
        for i in range(self.n + 1):
            if self.factors[i] != 0:
                polynomial += str(self.factors[i]) + 'x^' + str(i)
                if i != self.n:
                    polynomial += '+'
        return polynomial
        # ajajajaj

    def __add__(self, other):
        if self.n >= other.n:
            new = list(self.factors)  # tworzymy kopie zeby nie zepsuc self
            for i in range(len(self.factors)):
                try:
                    new[i] += other.factors[i]
                except IndexError:
                    break
        else:
            new = other.factors
            for i in range(len(other.factors)):
                try:
                    new[i] += self.factors[i]
                except IndexError:
                    break
        return Polynomial(len(new) - 1, new)


pol1 = Polynomial(1, [0, 1])
pol2 = Polynomial(2, [0, 22, 0])
pol3 = pol1 + pol2
print(pol3)
