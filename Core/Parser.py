import re
import itertools


class Parser:
    def __init__(self, program):
        self.program = program
        regex_symbols = ("(", ")", '"', "'", "\n", "+", "-", "/", "*", "%", "=")
        other_symbols = ("**", "//")
        for i in regex_symbols:
            regex = re.compile(r"([^{0}])([{0}])([^{0}]|$)".format(i))
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

        liste = list(filter(
            lambda n: not isinstance(n[0], str) or n[0].strip() != "",
            map
            (
                lambda n: list(n[1]),
                itertools.groupby(liste, lambda word: isinstance(word, str) and word == "\n")
            )
        ))

        if len(liste) == 1:
            liste = liste[0]

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
