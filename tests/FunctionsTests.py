try:
    from BaseTest import BaseTest
except ImportError:
    from tests.BaseTest import BaseTest  # Import when use PyCharm


class FunctionsTests(BaseTest):
    def test_conversions(self):
        self.codes_test(
            ("int('4');", 4),
            ("float('4.3');", 4.3),
            ("str(2);", '2'),
            ("bool(2);", True)
        )

    def test_math(self):
        self.codes_test(
            ("round(2.4);", 2),
            ("round(2.43, 1);", 2.4),
            ("max(2, 4);", 4),
            ("min(2, 4);", 2)
        )

    def test_others(self):
        self.codes_test(
            ("len('oui');", 3)
        )
