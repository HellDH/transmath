from typing import Dict

from main import NumericalMethods

from sympy import symbols, Expr

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
                                "expr": x ** 3 + 4 * x - 3,
                                "epsilon": 0.001,
                                "cords": (0, 1),
                                "expected": 0.674
                            }
                         ])
def test_newton_method(data: Dict[str, Expr | float | tuple]):
    obj = o.newtonMethod(data["expr"], data["epsilon"], data["cords"])

    assert round(float(obj), 3) == data["expected"]

@pytest.mark.parametrize("data",
                         [
                            {
                                "expr": x ** 3 - 3 * x + 1,
                                "epsilon": 0.01,
                                "cords": (-2, -1),
                                "expected": -0.946
                            }
                         ])
def test_chord_method(data: Dict[str, Expr | float | tuple]):
    obj = o.chordMethod(data["expr"], data["epsilon"], data["cords"])

    assert round(float(obj), 3) == data["expected"]
