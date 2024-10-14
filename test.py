from typing import Dict, Tuple

from main import NumericalMethods

from sympy import symbols, init_printing, Expr, tan, Matrix, Eq

import pytest

init_printing(use_unicode=True)

o = NumericalMethods()
x = symbols('x')

@pytest.mark.parametrize("data",
                         [
                            {
                                "expr": "x ** 3 + 3 * x ** 2 - 24 * x + 1",
                                "epsilon": 0.001,
                                "cords": (-7, -6),
                                "expected": -6.639
                            }
                         ])
def test_combined_method(data: Dict[str, Expr | float | Tuple[float]]):
    obj = o.combinedMethod(data["expr"], data["epsilon"], data["cords"])
    
    assert round(float(obj), 3) == data["expected"]

@pytest.mark.parametrize("data",
                         [
                            {
                                "expr": "tan(0.93 * x + 0.43) - x ** 2" ,
                                "epsilon": 0.0001,
                                "cords": (-0.4, -0.2),
                                "expected": -0.339
                            }
                         ])
def test_newton_method(data: Dict[str, Expr | float | Tuple[float]]):
    obj = o.newtonMethod(data["expr"], data["epsilon"], data["cords"])

    assert round(float(obj), 3) == data["expected"]

@pytest.mark.parametrize("data",
                         [
                            {
                                "expr": [("10 * x + x + 2 * x", 1.),
                                         ("3 * x + 5 * x", -2.),
                                         ("x - x + 9 * x", -1.)],
                                "iteration_count": 3,
                                "expected": [0.179, -0.497, -0.18]
                            }
                         ])
def test_zeidel_method(data: Dict[str, Expr | float | Tuple[float]]):
    obj = o.zeidelMethod(data["expr"], data["iteration_count"])

    assert obj == data["expected"]
