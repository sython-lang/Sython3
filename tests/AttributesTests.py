try:
    from BaseTest import BaseTest
except ImportError:
    from tests.BaseTest import BaseTest  # Import when use PyCharm


class AttributesTests(BaseTest):
    def test_str(self):
        self.codes_test(
            ("'OUI'.lower();", 'oui'),
            ("'oui'.upper();", 'OUI'),
            ("'ceci est'.capitalize();", 'Ceci est'),
            ("'ceci est'.title();", 'Ceci Est')
        )
