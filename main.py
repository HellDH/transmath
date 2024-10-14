from typing import Tuple, List
from inspect import signature
from sympy import Derivative, Expr, parse_expr, Matrix

class NumericalMethods:
    def combinedMethod(self, eq: str, eps: float, coincidences: Tuple[float]) -> float | bool:
        expr: Expr = parse_expr(eq, evaluate=False)

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
        
            if error > eps:
                recursion = lower((x11.evalf(), x12.evalf()), x11.evalf())
                return recursion

            return etta
        
        return lower(coincidences)
    
    def newtonMethod(self, eq: str, eps: float, cords: Tuple[float]) -> float | bool:
        expr: Expr = parse_expr(eq, evaluate=False)

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
        
        return lower()

    def zeidelMethod(self, expr: Tuple[str | float], iterations_count: int = 1) -> List[float] | bool:
        equation_system = []
        for ni, i in enumerate(expr):
            equation: Expr = parse_expr(i[0], evaluate=False)

            equation_system.append({
                "equation": list(equation.args),
                "diagonal_var": equation.args[ni],
                "eq_indexes": [i for i in range(1, len(equation.args) + 1)]
            })

        for num, j in enumerate(equation_system):
            var = j["diagonal_var"]
            j["equation"].remove(var)

            try:
                del j["eq_indexes"][num]
            except Exception as e:
                print(e)
                pass

            if abs(var.subs('x', 1)) >= abs(sum(j["equation"]).subs('x', 1)):
                continue
            else:
                return False

        hash_table = {}
        hash_table["iter_forms"] = {}

        for k in range(len(equation_system)):
            ldict = locals()

            arg_list = [str(arg.free_symbols.pop()) + str(equation_system[k]["eq_indexes"][num]) for num, arg in enumerate(equation_system[k]['equation'])]
            var_list = [str(eq * -1) + str(equation_system[k]["eq_indexes"][num]) for num, eq in enumerate(equation_system[k]['equation'])]

            s = f"xn = lambda {', '.join(arg_list)}: ({expr[k][1]} + {' + '.join(var_list)}) / {equation_system[k]['diagonal_var'].subs('x', 1)}"

            exec(s,
                 globals(),
                 ldict)
            
            hash_table["iter_forms"][k + 1] = ldict["xn"]

        for step in range(iterations_count + 1):
            hash_table[step] = {}
            for n in range(1, iterations_count + 1):
                hash_table[step]["x" + str(n)] = 0

        for iter in range(1, iterations_count + 1):
            increment = 1
            for f in hash_table['iter_forms'].values():
                sig = signature(f)
                
                params_list = [hash_table[iter - 1][str(el)] for el in sig.parameters.values()]

                hash_table[iter][f'x{increment}'] = f(*params_list)
                increment += 1

        return [round(result, 3) for result in hash_table[iterations_count].values()]

    def chordMethod(self, expr: Expr, eps: float, cords: List[float]) -> float | bool:
        pass # TODO : Сделать метод хорд, слишком долго откладывается
