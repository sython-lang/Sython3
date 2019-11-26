try:
    from BaseTest import BaseTest
except ImportError:
    from tests.BaseTest import BaseTest  # Import when use PyCharm


class ComplexTypesTests(BaseTest):
    def test_enum(self):
        self.programs_test_print(
            ("enum Michel { a, b }; print(Michel); print(Michel.a); print(Michel.b);", "<enum Michel {a, b}>\n0\n1\n")
        )
