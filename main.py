from typing import List
from sympy import Derivative, Expr

class NumericalMethods:
    def combinedMethod(self, expr: Expr, eps: float, cords: List[float], x0: float = None) -> float | bool:
        fn1 = expr.subs('x', cords[0])
        fn2 = expr.subs('x', cords[1])

        if fn1 * fn2 < 0:
            pass
        else:
            return False 

        der = None

        for i in range(len(expr.args)) :
            der = Derivative(expr).doit()

        try_expr = Derivative(der).doit()

        match len(try_expr.args):
            case 0:
                pass
            case _:
                der = try_expr

        if x0 != None:
            pass
        else:
            if fn1 * der.subs('x', cords[0]) > 0:
                x0 = cords[0] 
            if fn2 * der.subs('x', cords[1]) > 0:
                x0 = cords[1]
    
        x11 = x0 - (expr.subs('x', x0) / ((Derivative(expr.subs('x', x0)).doit()).subs('x', x0)))

        x12 = cords[0] - (((cords[1] - cords[0]) * fn1) / (fn2 - fn1))
    
        etta = (x11 + x12) / 2

        ans = abs(etta.evalf() - x11)
    
        if not ans < eps:
            rec = self.solve(expr, [x11.evalf(), x12.evalf()], eps, x11.evalf())
            return rec

        return ans
    
    def chordMethod(self, expr: Expr, eps: float, cords: List[float]) -> float | bool:
        fn1 = expr.subs('x', cords[0])
        fn2 = expr.subs('x', cords[1])

        if fn1 * fn2 < 0:
            pass
        else:
            return False 
        
        
