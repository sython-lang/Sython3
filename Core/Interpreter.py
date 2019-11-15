from Core.Environment import Environment
from Core.Syntax import Syntax
from Core.Parser import Parser
from Core.Constants import ERROR_STR
from Core.Utils import split


class Interpreter:
    def __init__(self):
        self.env = Environment()

    def repl(self, prompt="> "):
        while True:
            code = input(prompt)
            if Syntax(code).check:
                parser = Parser(code)
                val = self.eval_exp(0, parser.parse())
                if val is not None:
                    print(str(val))

    def execute(self, prog):
        if Syntax(prog).check:
            parser = Parser(prog)
            self.eval(parser.parse())

    def eval(self, prog):
        for k, v in enumerate(prog):
            self.eval_exp(k, v)

    def eval_exp(self, nb, exp):
        if isinstance(exp, str):
            if exp[0] == '"' or exp[0] == "'":
                return exp.replace('"', "").replace("'", "")
            else:
                try:
                    return self.env.variables[exp]
                except KeyError:
                    print(ERROR_STR.format("NameError", nb, "{} doesn't exist".format(exp)))
        elif isinstance(exp, (int, float)):
            return exp
        elif len(exp) == 1:
            return self.eval_exp(nb, exp[0])
        else:
            if exp[0] in self.env.functions.keys():
                proc = self.env.functions[exp[0]]
                args = [self.eval_exp(nb, i) for i in split(exp[1], ",")]
                return proc(*args)
            elif exp[1] in self.env.operators.keys():
                proc = self.env.operators[exp[1]]
                if exp[1] == "=":
                    args = (exp[0], self.eval_exp(nb, exp[2]))
                else:
                    args = (self.eval_exp(nb, exp[0]), self.eval_exp(nb, exp[2]))
                return proc(*args)
