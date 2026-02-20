import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp


def compile_numeric_function(eqs, symbols, param_symbols, param_values):

    eq_list = [eqs[c] for c in symbols.keys()]
    vars_list = [symbols[c] for c in symbols.keys()]

    func = sp.lambdify(
        [vars_list, list(param_symbols.values())],
        eq_list,
        "numpy"
    )

    def ode_system(t, y):
        return func(y, list(param_values.values()))

    return ode_system


def simulate(ode_system, y0, t_span):
    sol = solve_ivp(ode_system, t_span, y0, method="RK45")
    return sol