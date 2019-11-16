try:
    from BaseTest import BaseTest
except ImportError:
    from tests.BaseTest import BaseTest  # Import when use PyCharm


class ConditionsTests(BaseTest):
    def test_if(self):
        self.codes_test_print(
            ("if(2 == 2) { print(2); };", "2\n"),
            ("if(4 != 2) { print('oui'); };", "oui\n"),
            ("if('oui' == 'non') { print('NOP'); };", "")
        )
