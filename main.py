from typing import Tuple
from sympy import Derivative, Expr

class NumericalMethods:
    def combinedMethod(self, expr: Expr, eps: float, coincidences: Tuple[float]) -> float | bool:
        def lower(cords: Tuple[float], x0: float = None):
            fn1 = expr.subs('x', cords[0])
            fn2 = expr.subs('x', cords[1])

            if fn1 * fn2 < 0:
                pass
            else:
                return False

            der = None

            for i in range(len(expr.args)):
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
        
            x11 = x0 - (fn1 / ((Derivative(expr.as_ordered_terms()[0]).doit()).subs('x', x0) \
                                + expr.as_ordered_terms()[1].subs("x", 1)))

            x12 = cords[0] - (((cords[1] - cords[0]) * fn1) / (fn2 - fn1))

            etta = (x11 + x12) / 2

            error = abs(etta.evalf() - x11.evalf())
        
            if not error < eps:
                recursion = lower((x11.evalf(), x12.evalf()), x11.evalf())
                return recursion

            return etta
        
        lower_fun = lower(coincidences)

        return lower_fun
    
    def newtonMethod(self, expr: Expr, eps: float, cords: Tuple[float]) -> float | bool:
        fx = expr.subs
        fxx = Derivative(expr).doit().doit().evalf().subs

        def lower(x0: float = None):
            if x0 == None:
                for i in range(2):
                    if fx('x', cords[i]) * fxx('x', cords[i]) > 0:
                        x0 = cords[i]
                    else:
                        continue

            if x0 == None:
                return False
            
            error = fx('x', x0) / Derivative(expr).doit().evalf().subs('x', x0)

            xn = x0 - error

            if error > eps:
                recursion = lower(xn)
                return recursion

            return xn
        
        lower_fun = lower()

        return lower_fun
    
    def chordMethod(self, expr: Expr, eps: float, cords: Tuple[float]) -> float | bool:
        pass

    
