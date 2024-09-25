from typing import List
from sympy import Derivative, Expr

class combinedMethod:
    def solve(self, expr: Expr, cords: List[float], eps: float, x0: float = None) -> float:
        fn1 = expr.subs('x', cords[0])
        fn2 = expr.subs('x', cords[1])

        der = None

        for i in range(len(expr.args)) :
            der = Derivative(expr).doit()

        try_expr = Derivative(der).doit()

        if len(try_expr.args) == 0:
            pass
        else:
            der = try_expr

        if x0 != None:
            pass
        else:
            if fn1 * der.subs('x', cords[0]) > 0:
                x0 = cords[0] 
            if fn2 * der.subs('x', cords[1]) > 0:
                x0 = cords[1]
    
        x11 = x0 - (fn1 / ((Derivative(expr.as_ordered_terms()[0]).doit()) \
                           .subs('x', x0) \
                              + expr.as_ordered_terms()[1].subs("x", 1)))

        x12 = x0 - (((cords[1] - x0) * fn1) / (abs(fn2) + abs(fn1)))
    
        detta = (x11 + x12) / 2

        ans = abs(detta.evalf() - x11)
    
        if not ans < eps:
            rec = self.solve(expr, [x11.evalf(), x12.evalf()], eps, x11.evalf())
            return rec

        return ans
