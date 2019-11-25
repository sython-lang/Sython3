try:
    from BaseTest import BaseTest
except ImportError:
    from tests.BaseTest import BaseTest  # Import when use PyCharm

from sython3.Core.Syntax import Syntax


class LoopsTests(BaseTest):
    def test_semi_colon(self):
        syntax_expr_right = Syntax("print('oui');")
        syntax_expr_false = Syntax("print('oui')")
        syntax_right = Syntax("print('oui');input();")
        syntax_false = Syntax("print('oui') input();")

        for i in (syntax_false, syntax_expr_false):
            self.assertFalse(i.check_semi_colon(), msg="\nCode : "+i.program)
        for i in (syntax_right, syntax_expr_right):
            self.assertTrue(i.check_semi_colon(), msg="\nCode : "+i.program)

    def test_double_quotes(self):
        syntax_expr_right = Syntax('print("oui");')
        syntax_expr_false = Syntax('print("oui);')
        syntax_right = Syntax('print("oui");input();')
        syntax_false = Syntax('print("oui); input();')

        for i in (syntax_false, syntax_expr_false):
            self.assertFalse(i.check_double_quotes(), msg="\nCode : "+i.program)
        for i in (syntax_right, syntax_expr_right):
            self.assertTrue(i.check_double_quotes(), msg="\nCode : "+i.program)

    def test_simple_quotes(self):
        syntax_expr_right = Syntax("print('oui');")
        syntax_expr_false = Syntax("print('oui);")
        syntax_right = Syntax("print('oui');input();")
        syntax_false = Syntax("print('oui); input();")

        for i in (syntax_false, syntax_expr_false):
            self.assertFalse(i.check_simple_quotes(), msg="\nCode : "+i.program)
        for i in (syntax_right, syntax_expr_right):
            self.assertTrue(i.check_simple_quotes(), msg="\nCode : "+i.program)

    def test_parenthesis(self):
        syntax_expr_right = Syntax("print('oui');")
        syntax_expr_false = Syntax("print('oui';")
        syntax_right = Syntax("print('oui');input();")
        syntax_false = Syntax("print('oui'; input();")

        for i in (syntax_false, syntax_expr_false):
            self.assertFalse(i.check_parenthesis(), msg="\nCode : "+i.program)
        for i in (syntax_right, syntax_expr_right):
            self.assertTrue(i.check_parenthesis(), msg="\nCode : "+i.program)
