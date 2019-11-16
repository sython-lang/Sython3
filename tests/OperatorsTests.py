try:
    from BaseTest import BaseTest
except ImportError:
    from tests.BaseTest import BaseTest  # Import when use PyCharm


class LogicalTests(BaseTest):
    def test_equal(self):
        self.codes_test(
            ("2 == 2;", True),
            ("'2' == 2;", False)
        )

    def test_notequal(self):
        self.codes_test(
            ("2 != 2", False),
            ("'pi' != 'po'", True)
        )

    def test_greater(self):
        self.codes_test(
            ("2 > 4;", False),
            ("3.2 > 3;", True)
        )

    def test_greaterequals(self):
        self.codes_test(
            ("2 >= 4;", False),
            ("3.2 >= 3;", True),
            ("2 >= 2;", True)
        )

    def test_less(self):
        self.codes_test(
            ("2 < 4;", True),
            ("3.2 < 3;", False)
        )

    def test_lessequals(self):
        self.codes_test(
            ("2 <= 4;", True),
            ("3.2 <= 3;", False),
            ("2 <= 2;", True)
        )


class MathematicalTests(BaseTest):
    def test_add(self):
        self.codes_test(
            ("2 + 2;", 4),
            ("8.5 + 1542.2;", 1550.7),
            ("-2 + 2;", 0),
            ('"oui" + "non";', "ouinon")
        )

    def test_sub(self):
        self.codes_test(
            ("2 - 2;", 0),
            ("2 - 4;", -2),
            ("-2 - 2;", -4),
            ("round(5.3 - 2, 2);", 3.30),
            ("round(3.3 - 5, 1);", -1.7)
        )

    def test_mult(self):
        self.codes_test(
            ("2 * 3;", 6),
            ("2 * 0.5;", 1),
            ("-2 * 2;", -4),
            ('"oui" * 2;', "ouioui")
        )

    def test_truediv(self):
        self.codes_test(
            ("2 / 2;", 1),
            ("2.5 / 2;", 1.25),
            ("-2 / 2;", -1)
        )

    def test_div(self):
        self.codes_test(
            ("2 // 4;", 0),
            ("2.03 // 2;", 1),
            ("-2.04 // 2;", -2.0)
        )

    def test_pow(self):
        self.codes_test(
            ("2 ** 2;", 4),
            ("4 ** 16;", 4294967296),
            ("-2 ** 2;", 4),
            ("2 ** -2;", 0.25)
        )

    def test_mod(self):
        self.codes_test(
            ("2 % 2;", 0),
            ("3 % 4;", 3),
            ("5 % 4;", 1),
            ("-2 % 3;", 1)
        )

    def test_set(self):
        self.codes_execute("var=2;", 'var2="oui";', "var3 = 1.4;", "var4 = -2;")
        self.codes_test(
            ("var;", 2),
            ("var2;", "oui"),
            ("var3;", 1.4),
            ("var4;", -2)
        )

    def test_errors(self):
        self.codes_test_print(
            ("vari;", "NameError : \n  - Line : 0 \n  - vari doesn't exist\n"),
            ("2 / 0;", "ZeroDivisionError : \n  - Line : 0 \n  - Division by zero\n"),
            ("'oui' - 2;", "TypeError : \n  - Line : 0 \n  - Unsupported operand type(s) for -: 'str' and 'int'\n"),
            ("2 % 0;", "ZeroDivisionError : \n  - Line : 0 \n  - Integer division or modulo by zero\n")
        )
