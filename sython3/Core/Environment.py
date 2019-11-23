import operator as op

from sython3.Core.Constants import ERROR_STR
from sython3.Core.Utils import split


class Environment:
    def __init__(self, interpreter):
        self.interpreter = interpreter

        self.operators = {
            '+': op.add, '-': op.sub, "/": op.truediv, "*": op.mul, "//": op.floordiv, "%": op.mod,
            '**': op.pow, '=': self.set, "<=": op.le, "<": op.lt, ">": op.gt, ">=": op.ge, "==": op.eq, "!=": op.ne,
            '.': self.attr
        }
        self.functions = {
            'print': print, "int": int, 'float': float, 'str': str, 'round': round, 'if': self.condition_if,
            'input': input, "while": self.loop_while, "for": self.loop_for, "max": max, "min": min,
            'len': len, 'bool': bool
        }
        self.variables = {
            "true": True,
            "false": False
        }
        self.not_eval_function = ("if", "while", "for")
        self.attributes = {
            str: {
                "lower": str.lower, "upper": str.upper, "capitalize": str.capitalize, "title": str.title,
                "count": str.count, "endswith": str.endswith, "replace": str.replace, "strip": str.strip,
                "isalnum": str.isalnum, "isalpha": str.isalpha, "isascii": str.isascii, "isdecimal": str.isdecimal,
                "isdigit": str.isdigit, "isnumeric": str.isnumeric, "islower": str.islower, "isupper": str.isupper,
                "isprintable": str.isprintable, "istitle": str.istitle
            },
            float: {
                "isint": float.is_integer
            }
        }

    def attr(self, nb, obj, attribut):
        if isinstance(attribut, list):
            attribut[1] = [self.interpreter.eval_exp(nb, i) for i in split(attribut[1], ",")]
            try:
                if len(attribut[1]):
                    return self.attributes[type(obj)][attribut[0]](obj, *attribut[1])
                else:
                    return self.attributes[type(obj)][attribut[0]](obj)
            except KeyError:
                print(ERROR_STR.format("AttributeError", nb,
                                       "'" + type(obj).__name__ + "' doesn't have '" + attribut[0] + "' as attribute."))
        else:
            print(ERROR_STR.format("AttributeError", nb, 'Attribute must be functions.'))

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
