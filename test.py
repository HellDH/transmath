from main import NumericalMethods

from sympy import symbols

o = NumericalMethods()

x = symbols('x')
expr = x ** 3 + 3 * x ** 2 - 24 * x + 1

print(o.combinedMethod(expr, 0.001))
