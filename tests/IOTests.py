try:
    from BaseTest import BaseTest
except ImportError:
    from tests.BaseTest import BaseTest  # Import when use PyCharm

from unittest.mock import patch


class PrintTests(BaseTest):
    def test_print(self):
        self.codes_test_print(
            ("print(2);", "2\n"),
            ("print(-2);", "-2\n"),
            ("print(2 + 2);", "4\n"),
            ("print('oui');", "oui\n"),
            ("print(2 + 2, 'oui'+'non');", "4 ouinon\n")
        )


class InputTests(BaseTest):
    def test_input(self):
        self.codes_execute("var=input();")
        self.codes_test(
            ("input();", "Test"),
            ("input('Oui ? ');", "Test"),
            ("var;", "Test")
        )
