import operator as op


class Environment:
    def __init__(self):
        self.operators = {
            '+': op.add, '-': op.sub, "/": op.truediv, "*": op.mul, "//": op.floordiv, "%": op.mod,
            '**': op.pow, '=': self.set, "<=": op.le, "<": op.lt, ">": op.gt, ">=": op.ge, "==": op.eq, "!=": op.ne
        }
        self.functions = {
            'print': print, "int": int, 'float': float, 'str': str, 'round': round, 'if': self.condition_if
        }
        self.variables = {
            "true": True,
            "false": False
        }
        self.not_eval_function = ("if",)

    def condition_if(self, interpreter, nb, condition, *args):
        if interpreter.eval_exp(nb, condition):
            interpreter.eval_exp(nb, args[0])
        else:
            if "else" in args:
                interpreter.eval_exp(nb, args[2])

    def set(self, name, value):
        self.variables[name] = value
