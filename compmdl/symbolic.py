import sympy as sp


def generate_symbolic_system(model):
    compartments = model.compartments
    params = model.parameters

    symbols = {c: sp.Symbol(c) for c in compartments}
    param_symbols = {k: sp.Symbol(k) for k in params.keys()}

    eqs = {c: 0 for c in compartments}

    for flow in model.flows:
        rate_expr = sp.sympify(
            flow.rate,
            locals={**symbols, **param_symbols}
        )

        eqs[flow.from_] -= rate_expr
        eqs[flow.to] += rate_expr

    return symbols, param_symbols, eqs