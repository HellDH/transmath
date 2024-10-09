from typing import Dict

from main import NumericalMethods

from sympy import symbols, Expr, tan

import pytest

o = NumericalMethods()
x = symbols('x')

@pytest.mark.parametrize("data",
                         [
                            {
                                "expr": x ** 3 + 3 * x ** 2 - 24 * x + 1,
                                "epsilon": 0.001,
                                "cords": (-7, -6),
                                "expected": -6.639
                            }
                         ])
def test_combined_method(data: Dict[str, Expr | float | tuple]):
    obj = o.combinedMethod(data["expr"], data["epsilon"], data["cords"])
    
    assert round(float(obj), 3) == data["expected"]

@pytest.mark.parametrize("data",
                         [
                            {
                                "expr": tan(0.93 * x + 0.43) - x ** 2 ,
                                "epsilon": 0.0001,
                                "cords": (-0.4, -0.2),
                                "expected": -0.339
                            }
                         ])
def test_newton_method(data: Dict[str, Expr | float | tuple]):
    obj = o.newtonMethod(data["expr"], data["epsilon"], data["cords"])

    assert round(float(obj), 3) == data["expected"]
