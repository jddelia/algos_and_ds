#! /usr/bin/python3

# This program creates a fraction class.

class Fraction:
    
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        newnum = (self.num*other.den) + (other.num*self.den)
        newden = self.den*other.den
        gcd = Fraction(newnum, newden).gcd()
        if gcd == 0:
            return Fraction(newnum, newden)
        newnum = int(newnum / gcd)
        newden = int(newden / gcd)
        return Fraction(newnum, newden)


    def gcd(self):
        num = self.num
        den = self.den
        while den % abs(num) != 0:
            den1 = abs(num)
            num = den % abs(num)
            den = den1
        return num


fraction = Fraction(1, 4)
fraction2 = Fraction(1, 2)

print(fraction)

print(fraction2)

print(fraction + fraction2)
