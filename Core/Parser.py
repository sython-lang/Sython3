import re

from Core.Utils import split


class Parser:
    def __init__(self, program):
        self.program = program
        blocked_left_regex_symbols = ("!<>", "", "", "", "", "", "", "", "", "", "", "", "", "")
        blocked_right_regex_symbols = ("", "", "", "", "", "", "", "", "", "", "", "", "=", "=")
        regex_symbols = ("=", ")", '"', "'", "\n", "+", "-", "/", "*", "%", "(", ",", "<", ">")
        other_symbols = ("**", "//", "<=", ">=", "==", "!=")
        for k, v in enumerate(regex_symbols):
            regex = re.compile(r"([^{0}])([{1}])([^{2}]|$)".format(v+blocked_left_regex_symbols[k], v,
                                                                   v+blocked_right_regex_symbols[k]))
            self.program = regex.sub("\\1 \\2 \\3", self.program)
        for i in other_symbols:
            self.program = self.program.replace(i, " " + i + " ")

    def tokenize(self):
        tokens = self.program.split(" ")
        tlist = []
        while len(tokens):
            token = tokens.pop(0)
            if token == '"':
                text = '"'
                while tokens[0] != '"':
                    if text == '"':
                        text += tokens[0]
                    else:
                        text += " " + tokens[0]
                    tokens.pop(0)
                text += '"'
                tokens.pop(0)
                tlist.append(text)
            elif token == "'":
                text = "'"
                while tokens[0] != "'":
                    if text == "'":
                        text += tokens[0]
                    else:
                        text += " " + tokens[0]
                    tokens.pop(0)
                text += "'"
                tokens.pop(0)
                tlist.append(text)
            elif token != "":
                tlist.append(token)
        return tlist

    def parse(self):
        return self.read_from_tokens(self.tokenize(), 0)

    def read_from_tokens(self, tokens, nb):
        if len(tokens) == 0:
            return []
        liste = []
        while len(tokens):
            token = tokens.pop(0)
            if token == "(":
                liste.append(self.read_from_tokens(tokens, nb + 1))
            elif token == ")":
                return liste
            elif token == "=":
                liste.append(self.get_value(token))
                liste.append(self.read_from_tokens(tokens, nb + 1))
                liste.append(self.get_value("\n"))
            elif token == "\n" and nb != 0:
                return liste
            else:
                liste.append(self.get_value(token))

        liste = split(liste, "\n")

        return liste

    @staticmethod
    def get_value(token):
        try:

            return int(token)
        except ValueError:
            try:
                return float(token)
            except ValueError:
                return str(token)
