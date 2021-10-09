"""
Write the function quadratic_equation with arguments a, b ,c that solution to quadratic equation without comlex solution.
Write unit tests for this function with QuadraticEquationTest class
Minimum 3 tests: discriminant < 0, discriminant > 0, discriminant = 0

Test	                                    Expected	Got	
print(quadratic_equation(2, 1, -1))         (0.5, -1.0)
print(quadratic_equation(1, -4, 4))         2.0
print(quadratic_equation(4, 1, 2))          None
try:
    quadratic_equation(0, 0, 0)
except ValueError:
    print('error')                          error
"""

import math


def quadratic_equation(a, b, c):

    d = b**2 - 4*a*c
    sqrt_d = math.sqrt(abs(d))

    if a == 0:
        return "error"
    elif d == 0:
        x = (-b / (2 * a))
        return x
    elif d > 0:
        x1 = ((-b + sqrt_d)/(2 * a))
        x2 = ((-b - sqrt_d)/(2 * a))
        return x1, x2
    else:
        return None


class TestQuadraticEquation:
    def test_1(self):
        assert quadratic_equation(2, 1, -1) == (0.5, -1.0)

    def test_2(self):
        assert quadratic_equation(1, -4, 4) == (2.0)

    def test_3(self):
        assert quadratic_equation(4, 1, 2) == None

    def test_4(self):
        assert quadratic_equation(0, 0, 0) == 'error'
