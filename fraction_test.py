import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        f = Fraction(-9, 0)
        self.assertEqual("-inf", f.__str__())
        f = Fraction(6, 0)
        self.assertEqual("inf", f.__str__())
        f = Fraction(0, 0)
        self.assertEqual("0", f.__str__())

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        self.assertEqual(Fraction(0), Fraction(-6, 12) + Fraction(1, 2))
        self.assertEqual(Fraction(0), Fraction(0, 12) + Fraction(0))
        self.assertEqual(Fraction(1,-2), Fraction(-1, 8) + Fraction(-3, 8))
        self.assertEqual(Fraction(99999999, 555), Fraction(66666666, 555) + Fraction(33333333, 555))
        self.assertEqual(Fraction(10, 0) ,  Fraction(1, 0) + Fraction(7, 6))  #inf == inf + int
        self.assertEqual(Fraction(0, 1), Fraction(1, 0) + Fraction(-1, 0))   #suppose 0 == inf - inf
        self.assertEqual(Fraction(-7, 0), Fraction(-13, 0) + Fraction(-2, 0)) #-inf == -inf - inf



    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        #TODO write more tests using other cases.
        i = Fraction(0)
        j = Fraction(0, -1)
        k = Fraction(0, 0)
        l = Fraction(34, 0)
        m = Fraction(1,0)
        n = Fraction(-1,0)
        # Consider special values like 0, 1/0, -1/0
        self.assertTrue(i.__eq__(j))
        self.assertTrue(j.__eq__(k))
        self.assertTrue(l.__eq__(m))
        self.assertFalse(m.__eq__(n))


    def test_mul(self):
        f = Fraction(7,4)
        g = Fraction(1)
        h = Fraction(3,1)
        i = Fraction(0)
        j = Fraction(4,0)
        k = Fraction(-16,0)
        l = Fraction(-1, 0)
        
        self.assertEqual(f, f * g)
        self.assertEqual(i, f * i)
        self.assertEqual(0, g * i)
        self.assertEqual(l, k * f)
        self.assertEqual(j, k * l)
        self.assertEqual(0, i * k)
        self.assertEqual(0, j * i)

    def test_init(self):
        f = Fraction(21, 7)
        g = Fraction(64, -8)
        h = Fraction(0)
        i = Fraction(9, 0)
        j = Fraction(-4, 0)
        k = Fraction(6, 0)
        self.assertEqual(3, f.numerator)
        self.assertEqual(1, f.denominator)
        self.assertEqual(1, g.denominator)
        self.assertEqual(7, f.gcd)
        self.assertEqual(8, g.gcd)
        self.assertEqual(math.inf, k.numerator)
        self.assertEqual(-math.inf, j.numerator)
        self.assertEqual(1, k.denominator)

a= 20
b = 30