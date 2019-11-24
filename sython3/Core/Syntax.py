from sython3.Core.Constants import ERROR_STR
from sython3.Core.Parser import Parser
from sython3.Core.Environment import Environment


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
        for i in (  # self.check_parenthesis, self.check_double_quotes, self.check_simple_quotes,
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

    def check_double_quotes(line, exp):
        nb = 0
        for i in exp:
            if i == '"':
                nb += 1
        if nb % 2:
            print(ERROR_STR.format("SyntaxError", line, 'Double quote not finished'))
            return False
        return True

    def check_simple_quotes(line, exp):
        nb = 0
        for i in exp:
            if i == "'":
                nb += 1
        if nb % 2:
            print(ERROR_STR.format("SyntaxError", line, 'Simple quote not finished'))
            return False
        return True

    def check_parenthesis(line, exp):
        nb = 0
        for i in exp:
            if i == "(":
                nb += 1
            if i == ")":
                if nb == 0:
                    print(ERROR_STR.format("SyntaxError", line, "')' unexpected"))
                    return False
                else:
                    nb -= 1
        if nb != 0:
            print(ERROR_STR.format("SyntaxError", line, "')' expected"))
            return False
        return True
