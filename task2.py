from math import gcd

class Rational:
    def __init__(self, numerator = 0, denominator = 1):

        if not denominator:
            raise ZeroDivisionError("Division by zero!")

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integer")

        self.numerator = numerator // gcd(numerator, denominator)
        self.denominator = denominator // gcd(numerator, denominator)


    def division(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def divisionFloat(self):
        return self.numerator / self.denominator


def main():
    firstFraction = Rational(2, 1)
    print(firstFraction.division())
    print(firstFraction.divisionFloat())

    secondFraction = Rational(4, 1)
    print(secondFraction.division())
    print(secondFraction.divisionFloat())


main()
