class CompartmentModel:

    def __init__(self, schema):
        self.schema = schema

    @classmethod
    def from_yaml(cls, path):
        from .parser import load_yaml
        return cls(load_yaml(path))

    def compile(self):
        from .jacobian import compute_jacobian
        from .symbolic import generate_symbolic_system

        self.symbols, self.param_symbols, self.eqs = \
            generate_symbolic_system(self.schema)

        self.jacobian = compute_jacobian(self.eqs, self.symbols)

    def simulate(self):
        from .solver import compile_numeric_function, simulate

        ode = compile_numeric_function(
            self.eqs,
            self.symbols,
            self.param_symbols,
            self.schema.parameters
        )

        y0 = [self.schema.initial_conditions[c]
              for c in self.schema.compartments]

        return simulate(ode, y0, self.schema.t_span)