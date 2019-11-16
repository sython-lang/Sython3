from sython3.Core.Interpreter import Interpreter
from sython3.Core.Parser import Parser
import unittest


class MathematicalTests(unittest.TestCase):
    def setUp(self):
        self.interpreter = Interpreter()

    def test_add(self):
        tests = (("2 + 2;", 4), ("8.5 + 1542.2;", 1550.7), ('"oui" + "non";', "ouinon"))
        for i in tests:
            parser = Parser(i[0])
            self.assertEqual(self.interpreter.eval_exp(0, parser.parse()), i[1])
