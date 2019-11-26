from sython3.Core.Constants import ERROR_STR


class Enum:
    def __init__(self, name, *values):
        self.name = name
        self.values = values

    def get_value(self, nb, item):
        try:
            return self.values.index(item)
        except ValueError:
            print(ERROR_STR.format("AttributeError", nb, "'" + self.name + "' doesn't have '" + item + "' as value."))

    def __str__(self):
        return "<enum "+self.name+" {"+", ".join(self.values)+"}>"
