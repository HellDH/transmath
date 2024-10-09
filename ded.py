from main import NumericalMethods

from sympy import symbols, Eq

x = symbols('x')

o = NumericalMethods()

expr = (
    Eq(10 * x + x + 2 * x, 1),
    Eq(3 * x + 5 * x, -2),
    Eq(x - x + 9 * x, -1)
)

print(o.ZeidelMethod(expr, 0.1))
