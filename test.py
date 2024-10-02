from main import NumericalMethods

from sympy import symbols

o = NumericalMethods()

x = symbols('x')
expr = x ** 3 - 0.2 * x ** 2 + 0.5 * x + 1.5

print(o.chordMethod(expr, 0.0001, [-1, 0]))
