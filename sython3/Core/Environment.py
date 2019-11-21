import operator as op


class Environment:
    def __init__(self, interpreter):
        self.interpreter = interpreter

        self.operators = {
            '+': op.add, '-': op.sub, "/": op.truediv, "*": op.mul, "//": op.floordiv, "%": op.mod,
            '**': op.pow, '=': self.set, "<=": op.le, "<": op.lt, ">": op.gt, ">=": op.ge, "==": op.eq, "!=": op.ne
        }
        self.functions = {
            'print': print, "int": int, 'float': float, 'str': str, 'round': round, 'if': self.condition_if,
            'input': input, "while": self.loop_while, "for": self.loop_for
        }
        self.variables = {
            "true": True,
            "false": False
        }
        self.not_eval_function = ("if", "while", "for")

    def loop_for(self, nb, *args):
        init, cond, statement, exp = args[0]
        self.interpreter.eval_exp(nb, init)
        while self.interpreter.eval_exp(nb, cond):
            self.interpreter.eval_exp(nb, exp)
            self.interpreter.eval_exp(nb, statement)

    def condition_if(self, nb, *args):
        for i in range(0, len(args), 2):
            if args[i] == "else":
                self.interpreter.eval_exp(nb, args[i+1])
                return
            else:
                if self.interpreter.eval_exp(nb, args[i]):
                    self.interpreter.eval_exp(nb, args[i+1])
                    return

    def loop_while(self, nb, condition, exp):
        while self.interpreter.eval_exp(nb, condition):
            self.interpreter.eval_exp(nb, exp)

    def set(self, name, value):
        self.variables[name] = value
