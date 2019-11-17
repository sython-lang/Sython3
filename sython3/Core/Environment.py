import operator as op


class Environment:
    def __init__(self):
        self.operators = {
            '+': op.add, '-': op.sub, "/": op.truediv, "*": op.mul, "//": op.floordiv, "%": op.mod,
            '**': op.pow, '=': self.set, "<=": op.le, "<": op.lt, ">": op.gt, ">=": op.ge, "==": op.eq, "!=": op.ne
        }
        self.functions = {
            'print': print, "int": int, 'float': float, 'str': str, 'round': round, 'if': self.condition_if,
            'input': input
        }
        self.variables = {
            "true": True,
            "false": False
        }
        self.not_eval_function = ("if",)

    @staticmethod
    def condition_if(interpreter, nb, *args):
        for i in range(0, len(args), 2):
            if args[i] == "else":
                interpreter.eval_exp(nb, args[i+1])
                return
            else:
                if interpreter.eval_exp(nb, args[i]):
                    interpreter.eval_exp(nb, args[i+1])
                    return

    def set(self, name, value):
        self.variables[name] = value
