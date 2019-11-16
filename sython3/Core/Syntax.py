from sython3.Core.Constants import ERROR_STR


class Syntax:
    def __init__(self, program):
        self.check = True
        for k, v in enumerate(program.split("\n")):
            for i in (self.check_parenthesis, self.check_double_quotes, self.check_simple_quotes,
                      self.check_semi_colon):
                if not i(k+1, v):
                    self.check = False
                    break

    @staticmethod
    def check_semi_colon(line, exp):
        if len(exp.replace(" ", "")) and exp.replace(" ", "")[-1] != ";":
            print(ERROR_STR.format("SyntaxError", line, "Required ';'"))
            return False
        return True

    @staticmethod
    def check_double_quotes(line, exp):
        nb = 0
        for i in exp:
            if i == '"':
                nb += 1
        if nb % 2:
            print(ERROR_STR.format("SyntaxError", line, 'Double quote not finished'))
            return False
        return True

    @staticmethod
    def check_simple_quotes(line, exp):
        nb = 0
        for i in exp:
            if i == "'":
                nb += 1
        if nb % 2:
            print(ERROR_STR.format("SyntaxError", line, 'Simple quote not finished'))
            return False
        return True

    @staticmethod
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
