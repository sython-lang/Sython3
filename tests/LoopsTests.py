try:
    from BaseTest import BaseTest
except ImportError:
    from tests.BaseTest import BaseTest  # Import when use PyCharm


class LoopsTests(BaseTest):
    def test_while(self):
        self.programs_test_print(
            ("while(2 != 2) { print('oui'); };", "")
        )
