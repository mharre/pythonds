def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return f'{self.num} / {self.den}'

    def __add__(self, other):
        newnum = self.num*other.den + self.den*other.num
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __sub__(self, other):
        newnum = self.num * other.den - self.den*other.num
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)       

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __gt__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.den 
        newnum1 = other.num * self.den
        newden1 = other.den * self.den
        if (newnum,newden) > (newnum1,newden1):
            return True
        return False

    def __lt__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.den 
        newnum1 = other.num * self.den
        newden1 = other.den * self.den
        if (newnum,newden) < (newnum1,newden1):
            return True
        return False

def main():
    x = Fraction(2,3)
    y = Fraction(1,4)

    print(x+y)
    print(x == y)
    print(x * y)
    print(x / y)
    print(x-y)
    print(x>y)
    print(x<y)

main()