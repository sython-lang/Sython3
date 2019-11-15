import operator as op


class Environment:
    def __init__(self):
        self.operators = {
            '+': op.add, '-': op.sub, "/": op.truediv, "*": op.mul, "//": op.floordiv, "%": op.mod,
            '**': pow, '=': self.set, "<=": op.le, "<": op.lt, ">": op.gt, ">=": op.ge, "==": op.eq, "!=": op.ne
        }
        self.functions = {
            'print': print
        }
        self.variables = {
            "true": True,
            "false": False
        }

    def set(self, name, value):
        self.variables[name] = value
