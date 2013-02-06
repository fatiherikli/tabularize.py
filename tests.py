import unittest

import tabularize

class TabularizeTestCase(unittest.TestCase):

    def test_ignore_headers(self):
        self.assertEqual(tabularize.loads('| name | surname |'), [])

    def test_whitespace(self):
        self.assertEqual(tabularize.loads("""
        | name | surname |
        | edi  | budu    |
        """),  [{ "name": "edi", "surname": "budu"}])

    def test_dashes(self):
        self.assertEqual(tabularize.loads("""
        ------------------
        | name | surname |
        ------------------
        | edi  | budu    |
        ------------------
        """),  [{ "name": "edi", "surname": "budu"}])

        self.assertEqual(tabularize.loads("""
        __________________
        | name | surname |
        ..................
        | edi  | budu    |
        __________________
        """),  [{ "name": "edi", "surname": "budu"}])

    def test_multiple_lines(self):
        self.assertEqual(tabularize.loads("""
        __________________
        | name | surname |
        | edi  | budu    |
        | budu | edi     |
        __________________
        """),  [{ "name": "edi", "surname": "budu"},
                { "name": "budu", "surname": "edi"}])

    def test_comments(self):
        self.assertEqual(tabularize.loads("""

        Here is the our customer table:

        | name  | surname  |
        | edi   | budu     |
        | budu  | edi      |

        Thanks

        """),  [{ "name": "edi", "surname": "budu"},
                { "name": "budu", "surname": "edi"}])

    def test_different_types(self):
        self.assertEqual(tabularize.loads("""
        __________________
        | name | surname |
        | edi  | budu    |
        | budu | edi     |
        __________________
        """, return_type=list),  [["edi", "budu"], ["budu", "edi"]])

        self.assertEqual(tabularize.loads("""
        __________________
        | name | surname |
        | edi  | budu    |
        | budu | edi     |
        __________________
        """, return_type=tuple),  [("edi", "budu"), ("budu", "edi")])

    def test_docstrings(self):
        class _docstring:
            """
            This is a docstring

            Here is my test case:

            ------------------------------
            | name | surname | full_name |
            ------------------------------
            | edi  | budu    | edi budu  |
            | budu | edi     | budu edi  |
            ------------------------------

            """

        tabular = tabularize.from_docstring(_docstring, return_type=list)
        self.assertIsInstance(tabular, list)
        for name, surname, full_name in tabular: # testception
            self.assertEqual("%s %s" % (name, surname), full_name)


if __name__ == "__main__":
    unittest.main()
