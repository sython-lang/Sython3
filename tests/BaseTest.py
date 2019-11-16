from sython3.Core.Parser import Parser
from sython3.Core.Interpreter import Interpreter
import unittest
import io
import sys


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.interpreter = Interpreter()

    def codes_execute(self, *codes):
        for i in codes:
            parser = Parser(i)
            self.interpreter.eval_exp(0, parser.parse())

    def codes_test(self, *tests):
        for i in tests:
            parser = Parser(i[0])
            self.assertEqual(self.interpreter.eval_exp(0, parser.parse()), i[1], msg="\nCode : "+i[0])

    def codes_test_print(self, *tests):
        for i in tests:
            parser = Parser(i[0])
            captured = io.StringIO()
            sys.stdout = captured
            self.assertIsNone(self.interpreter.eval_exp(0, parser.parse()), msg="\nCode : "+i[0])
            sys.stdout = sys.__stdout__
            self.assertEqual(captured.getvalue(), i[1], msg="\nCode: " + i[0])

