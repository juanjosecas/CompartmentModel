import sympy as sp


def compute_jacobian(eqs, symbols):
    eq_list = [eqs[c] for c in symbols.keys()]
    vars_list = [symbols[c] for c in symbols.keys()]
    J = sp.Matrix(eq_list).jacobian(vars_list)
    return J