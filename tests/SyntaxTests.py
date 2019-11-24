try:
    from BaseTest import BaseTest
except ImportError:
    from tests.BaseTest import BaseTest  # Import when use PyCharm

from sython3.Core.Syntax import Syntax
import io
import sys


class LoopsTests(BaseTest):
    def setUp(self):
        super(LoopsTests, self).setUp()
        self.syntax_expr_right = Syntax("print('oui');")
        self.syntax_expr_not_semi_colon = Syntax("print('oui')")
        self.syntax_right = Syntax("print('oui');input();")
        self.syntax_not_semi_colon = Syntax("print('oui') input();")

    def test_semi_colon(self):
        for i in (self.syntax_not_semi_colon, self.syntax_expr_not_semi_colon):
            self.assertFalse(i.check_semi_colon(), msg="\nCode : "+i.program)
        for i in (self.syntax_right, self.syntax_expr_right):
            self.assertTrue(i.check_semi_colon(), msg="\nCode : "+i.program)
