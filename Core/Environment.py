import operator as op


class Environment:
    def __init__(self):
        self.operators = {
            '+': op.add, '-': op.sub, "/": op.truediv, "*": op.mul, "//": op.floordiv, "%": op.mod,
            '**': pow, '=': self.set
        }
        self.functions = {
            'print': print
        }
        self.variables = {

        }

    def set(self, name, value):
        self.variables[name] = value
