import math
class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
           ( can not init undefined (0/0) )
        """
        self.numerator = numerator
        self.denominator = denominator
        if (self.denominator == 0):
            if (self.numerator >= 0):
                self.numerator = math.inf
                self.denominator = 1
            else:
                self.numerator = -math.inf
                self.denominator = 1
        else:
            self.gcd = math.gcd(self.numerator, self.denominator)
            # make proper form
            self.numerator = int(self.numerator / self.gcd)
            self.denominator = int(self.denominator / self.gcd)

            # move negative sign to numerator
            if (self.denominator < 0):
                self.numerator = -self.numerator
                self.denominator = -self.denominator

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
           ( inf + (-inf) is undefined )
        """
        if (self.numerator == math.inf and frac.numerator == math.inf):
            return Fraction(1,0)
        elif (self.numerator == -math.inf and frac.numerator == -math.inf):
            return Fraction(-1,0)

        elif (self.numerator == math.inf or frac.numerator == math.inf):
            return Fraction(1,0)
        elif (self.numerator == -math.inf or frac.numerator == -math.inf):
            return Fraction(-1,0)

        numerator = (self.numerator * frac.denominator) + (frac.numerator * self.denominator)
        denominator = self.denominator * frac.denominator
        return Fraction(numerator,denominator)

    def __mul__(self, frac):
        """Return the multiplication of two fraction as a new fraction.
        """
        if (self.numerator == math.inf and frac.numerator == math.inf):
            return Fraction(1,0)
        elif (self.numerator == -math.inf and frac.numerator == -math.inf):
            return Fraction(1,0)
        elif (self.numerator == math.inf and frac.numerator == -math.inf):
            return Fraction(-1,0)
        elif (self.numerator == -math.inf and frac.numerator == +math.inf):
            return Fraction(-1,0)

        elif ((self.numerator == math.inf and frac.numerator > 0) or (frac.numerator == math.inf and self.numerator > 0)):
            return Fraction(1,0)
        elif ((self.numerator == math.inf and frac.numerator < 0) or (frac.numerator == math.inf and self.numerator < 0)):
            return Fraction(-1,0)
        elif ((self.numerator == -math.inf and frac.numerator < 0) or (frac.numerator == -math.inf and self.numerator < 0)):
            return Fraction(1,0)
        elif ((self.numerator == -math.inf and frac.numerator > 0) or (frac.numerator == -math.inf and self.numerator > 0)):
            return Fraction(-1,0)


        numerator = self.numerator * frac.numerator
        denominator = self.denominator * frac.denominator
        return Fraction(numerator,denominator)

    def __str__(self):
        """Return string of fraction integer or proper form
        """

    # Divided by zero
        if (self.numerator == math.inf):
            return str(math.inf)
        elif (self.numerator == -math.inf):
            return str(-math.inf)
        elif (self.numerator % self.denominator == 0):
             return str(int(self.numerator / self.denominator))
        else:
             return f'{self.numerator}/{self.denominator}'

            

    #Optional have fun and overload other operators such as 
    # __sub__ for f-g
    # __gt__  for f > g
    # __neg__ for -f (negation)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        
        return self.numerator == frac.numerator and self.denominator == frac.denominator
