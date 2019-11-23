try:
    from BaseTest import BaseTest
except ImportError:
    from tests.BaseTest import BaseTest  # Import when use PyCharm


class AttributesTests(BaseTest):
    attributes = {
        str: {
            "lower": str.lower, "upper": str.upper, "capitalize": str.capitalize, "title": str.title,
            "count": str.count, "endswith": str.endswith, "replace": str.replace, "strip": str.strip,
            "isalnum": str.isalnum, "isalpha": str.isalpha, "isascii": str.isascii, "isdecimal": str.isdecimal,
            "isdigit": str.isdigit, "isnumeric": str.isnumeric, "islower": str.islower, "isupper": str.isupper,
            "isprintable": str.isprintable, "istitle": str.istitle
        },
        float: {
            "isint": float.is_integer
        }
    }

    def test_str(self):
        self.codes_test(
            ("'OUI'.lower();", 'oui'),
            ("'oui'.upper();", 'OUI'),
            ("'ceci est'.capitalize();", 'Ceci est'),
            ("'ceci est'.title();", 'Ceci Est'),
            ("'Test oui'.count('e');", 1),
            ("'Test'.endswith('t');", True),
            ("'Test'.replace('e', 't');", "Ttst"),
            ("'    Test   '.strip();", 'Test'),
            ("'1'.isalnum();", True),
            ("'1'.isalpha();", False),
            ("'1'.isascii();", True),
            ("'1'.isdecimal();", True),
            ("'1'.isdigit();", True),
            ("'1'.isnumeric();", True),
            ("'a'.islower();", True),
            ("'a'.isupper();", False),
            ("'a'.isprintable();", True),
            ("'a'.istitle();", False)
        )
