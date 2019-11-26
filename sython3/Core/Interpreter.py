from sython3.Core.Environment import Environment
from sython3.Core.Syntax import Syntax
from sython3.Core.Parser import Parser
from sython3.Core.Constants import ERROR_STR
from sython3.Core.Utils import split


class Interpreter:
    def __init__(self):
        self.env = Environment(self)

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
        while isinstance(prog, list) and len(prog) == 1 and isinstance(prog[0], list) and len(prog[0]) == 1:
            prog = prog[0]
        if isinstance(prog[0][0], list):
            prog = prog[0]
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
            if isinstance(exp[0], str) and exp[0] in self.env.builtins.keys():
                proc = self.env.builtins[exp[0]]
                temp = split(exp[1], ",")
                for k, v in enumerate(temp):
                    if len(v) == 1:
                        temp[k] = v[0]
                args = temp
                for k, v in enumerate(args):
                    if isinstance(v, list):
                        for i in self.env.operators.keys():
                            if i in v:
                                temp = split(v, i, False)
                                for kt, vt in enumerate(temp):
                                    if len(vt) == 1:
                                        temp[kt] = vt[0]
                                if exp[0] not in self.env.not_eval_function:
                                    args[k] = self.eval_exp(nb, temp)
                                else:
                                    args[k] = temp
                    else:
                        if exp[0] not in self.env.not_eval_function:
                            args[k] = self.eval_exp(nb, v)
                        else:
                            args[k] = v
                if exp[0] in self.env.not_eval_function:
                    args.insert(0, nb)
                    args += [i for i in exp[2:] if i != "elif"]
                return proc(*args)
            elif isinstance(exp[1], str) and exp[1] in self.env.operators.keys():
                proc = self.env.operators[exp[1]]
                if exp[1] == "=":
                    args = (exp[0], self.eval_exp(nb, exp[2]))
                elif exp[1] == ".":
                    args = (nb, self.eval_exp(nb, exp[0]), exp[2])
                else:
                    args = (self.eval_exp(nb, exp[0]), self.eval_exp(nb, exp[2]))
                try:
                    return proc(*args)
                except Exception as e:
                    print(ERROR_STR.format(e.__class__.__name__, nb, " ".join(e.args).capitalize()))
