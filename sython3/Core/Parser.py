import re

from sython3.Core.Utils import split


class Parser:
    def __init__(self, program):
        self.program = program.replace("\n", "")
        self.symbols = ("=", ")", '"', "'", ";", "+", "-", "/", "*", "%", "(", ",", "<", ">", "**", "//", "<=", ">=",
                        "==", "!=")
        self.regex_symbols = (("!<>=", "=", "="), ("", ")", ""), ("", '"', ""), ("", "'", ""), ("", ";", ""),
                              ("", "+", ""), ("", "-", ""), ("/", "/", "/"), ("*", "*", "*"), ("", "%", ""),
                              ("", "(", ""), ("", ",", ""), ("", "<", "="), ("", ">", "="))
        for i in self.regex_symbols:
            if i[0] != "" and i[2] != "":
                regex = re.compile(r"([^{0}]|^)([{1}])([^{2}]|$)".format(*i))
                self.program = regex.sub("\\1 \\2 \\3", self.program)
            elif i[2] != "":
                regex = re.compile(r"([{0}])([^{1}]|$)".format(*i[1:]))
                self.program = regex.sub(" \\1 \\2", self.program)
            elif i[0] != "":
                regex = re.compile(r"([^{0}]|^)([{1}])".format(*i[:-1]))
                self.program = regex.sub("\\1 \\2 ", self.program)
            else:
                regex = re.compile(r"([{0}])".format(i[1]))
                self.program = regex.sub(" \\1 ", self.program)
        for i in (i for i in self.symbols if len(i) == 2):
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
        return self.read_from_tokens(self.tokenize(), False)

    def read_from_tokens(self, tokens, return_semi_colon):
        if len(tokens) == 0:
            return []
        liste = []
        while len(tokens):
            token = tokens.pop(0)
            if token == "(":
                liste.append(self.read_from_tokens(tokens, False))
            elif token == ")":
                return liste
            elif token == "=":
                liste.append(self.get_value(token))
                liste.append(self.read_from_tokens(tokens, True))
                liste.append(self.get_value(";"))
            elif token == ";" and return_semi_colon:
                return liste
            else:
                liste.append(self.get_value(token))

        liste = split(liste, ";")
        for i in self.symbols:
            while isinstance(liste, list) and len(liste) == 1:
                liste = liste[0]
            temp = split(liste, i, False)
            for k, v in enumerate(temp):
                if len(v) == 1:
                    temp[k] = v[0]
            liste = temp

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
