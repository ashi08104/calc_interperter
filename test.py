import unittest
from parser import get_paired_parenthes_pos, str2tk, str2ast

class TestPairedParenthes(unittest.TestCase):
    def setUp(self):
        pass

    def test_rightp(self):
        self.assertEqual(
            get_paired_parenthes_pos("()", 0),
            1)

    def test_withcontent1(self):
        self.assertEqual(
            get_paired_parenthes_pos("(a)", 0),
            2)

    def test_withcontent2(self):
        self.assertEqual(
            get_paired_parenthes_pos("(ab)", 0),
            3)

    def test_withmoreparen1(self):
        self.assertEqual(
            get_paired_parenthes_pos("(())", 0),
            3)

    def test_withmoreparen2(self):
        self.assertEqual(
            get_paired_parenthes_pos("(())", 1),
            2)

    def test_withmoreparen3(self):
        self.assertEqual(
            get_paired_parenthes_pos("(0a(3)(dk(dd)((dd))))ab(", 0),
            20)

    def test_witherror1(self):
        with self.assertRaises(Exception):
            get_paired_parenthes_pos("(a", 0)

    def test_witherror2(self):
        with self.assertRaises(Exception):
            get_paired_parenthes_pos("(a(ab)", 0)

    def test_with_noerror3(self):
        self.assertEqual(
            get_paired_parenthes_pos("(a(ab))(", 0),
            6)

class TestStr2tk(unittest.TestCase):
    def setUp(self):
        pass

    def test_none(self):
        self.assertEqual(
            str2tk(""),
            [])

    def test_singledigit(self):
        self.assertEqual(
            str2tk("1"),
            ["1"])

    def test_whitepace(self):
        self.assertEqual(
            str2tk("(  1+3) "),
            ['(', '1', '+', '3', ')'])

    def test_multdigit(self):
        self.assertEqual(
            str2tk("11"),
            ["11"])

    def test_others(self):
        self.assertEqual(
            str2tk("(11+2)"),
            ["(", "11", "+", "2", ")"])

class TestParser(unittest.TestCase):
    def setUp(self):
        pass

    def test_n(self):
        self.assertEqual(str(str2ast("3")),
                         "[3:N N]")

    def test_e1(self):
        self.assertEqual(str(str2ast("(33+2)")),
                         "[+:[33:N N] [2:N N]]")

    def test_e2(self):
        self.assertEqual(str(str2ast("(33+(2+1))")),
                         "[+:[33:N N] [+:[2:N N] [1:N N]]]")

    def test_e3(self):
        self.assertEqual(str(str2ast("((3+3)+2)")),
                         "[+:[+:[3:N N] [3:N N]] [2:N N]]")

    def test_e3(self):
        self.assertEqual(str(str2ast("((1+((2+3)+3))+((((4+5)+(6+7))+8)+9))")),
                         "[+:[+:[1:N N] [+:[+:[2:N N] [3:N N]] [3:N N]]] [+:[+:[+:[+:[4:N N] [5:N N]] [+:[6:N N] [7:N N]]] [8:N N]] [9:N N]]]")


if __name__ == "__main__":
    unittest.main()
