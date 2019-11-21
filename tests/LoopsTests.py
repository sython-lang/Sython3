try:
    from BaseTest import BaseTest
except ImportError:
    from tests.BaseTest import BaseTest  # Import when use PyCharm


class LoopsTests(BaseTest):
    def test_while(self):
        self.programs_test_print(
            ("while(2 != 2) { print('oui'); };", "")
        )

    def test_for(self):
        self.programs_test_print(
            ("for(i=0; i<4; i=i+1) { print(i) };", "0\n1\n2\n3\n")
        )
