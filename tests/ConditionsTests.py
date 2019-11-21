try:
    from BaseTest import BaseTest
except ImportError:
    from tests.BaseTest import BaseTest  # Import when use PyCharm


class ConditionsTests(BaseTest):
    def test_if(self):
        self.programs_test_print(
            ("if(2 == 2) { print(2); };", "2\n"),
            ("if(4 != 2) { print('oui'); };", "oui\n"),
            ("if('oui' == 'non') { print('NOP'); };", "")
        )

    def test_else(self):
        self.programs_test_print(
            ("if(2 != 2) { print(1); } else { print(2); };", "2\n"),
            ("if(4 == 5) { print('Egal à 5'); } else { print('Pas Egal'); };", 'Pas Egal\n'),
            ("if(2 == 3) { print(1); } elif(2 == 4) { print(2); } else { print(3); };",  '3\n')
        )

    def test_elif(self):
        self.programs_test_print(
            ("if(2 != 2) { print(1); } elif(3 != 2) { print(2); };", "2\n"),
            ("if(4 == 5) { print('Egal à 5'); } elif(5==5) { print('Egal a 4'); };", 'Egal a 4\n'),
            ("if(2 == 3) { print(1); } elif(2 == 2) { print(2); } else { print(3); };", '2\n')
        )
