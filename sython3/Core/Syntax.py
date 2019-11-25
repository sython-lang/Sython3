from sython3.Core.Constants import ERROR_STR
from sython3.Core.Parser import Parser
from sython3.Core.Environment import Environment
from sython3.Core.Utils import flattener


class Syntax:
    def __init__(self, program):
        self.check = True
        self.program = program
        self.program_parsed = Parser(program).parse()

        from sython3.Core.Interpreter import Interpreter

        self.env = Environment(Interpreter())
        while isinstance(self.program_parsed, list) and len(self.program_parsed) == 1 \
                and isinstance(self.program_parsed[0], list) and len(self.program_parsed[0]) == 1:
            self.program_parsed = self.program_parsed[0]
        if isinstance(self.program_parsed[0][0], list):
            self.program_parsed = self.program_parsed[0]
        for i in (self.check_parenthesis, self.check_double_quotes, self.check_simple_quotes,
                  self.check_semi_colon,):
            self.check = i()
            break

    def check_semi_colon(self):
        for k, v in enumerate(self.program_parsed):
            nb = 0
            for function in self.env.functions.keys():
                nb += v.count(function)
            if nb > 1:
                print(ERROR_STR.format("SyntaxError", k+1, "';' expected"))
                return False
        for i in range(len(self.program.split("\n"))-1, -1, -1):
            if self.program.split("\n")[i] != "":
                if self.program.split("\n")[i][-1].strip() != ";":
                    print(ERROR_STR.format("SyntaxError", i+1, "';' expected"))
                    return False
                break
        return True

    def check_double_quotes(self):
        for i in flattener(self.program_parsed):
            if i[0] == '"':
                if i[-1] != i[0]:
                    print(ERROR_STR.format("SyntaxError", i, '" expected.'))
                    return False
        return True

    def check_simple_quotes(self):
        for i in flattener(self.program_parsed):
            if i[0] == "'":
                if i[-1] != i[0]:
                    print(ERROR_STR.format("SyntaxError", i, "' expected."))
                    return False
        return True

    def check_parenthesis(self):
        passed = 0
        for line, exp in enumerate(self.program.split(";")):
            nb = 0
            if not passed:
                if exp.strip().startswith("for"):
                    passed = 2
                else:
                    for k, i in enumerate(exp):
                        if i == "(":
                            nb += 1
                        elif i == ")":
                            if nb == 0:
                                print(ERROR_STR.format("SyntaxError", line, "')' unexpected"))
                                return False
                            else:
                                nb -= 1
                    if nb != 0:
                        print(ERROR_STR.format("SyntaxError", line, "')' expected"))
                        return False
            else:
                passed -= 1
        return True
