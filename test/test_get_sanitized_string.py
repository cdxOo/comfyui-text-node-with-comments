import unittest
from textwrap import dedent
from remove_comments import remove_comments

class TestRemoveComments(unittest.TestCase):
    def test_ok(self):
        str = dedent("""\
                 foo,// bar,
                 /*
                 herp,
                 derp*/
                 quux""")

        print(str);
        print('---------------')
        actual = remove_comments(str)
        print(actual)
        expected = dedent("""\
                foo,

                quux""")
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
