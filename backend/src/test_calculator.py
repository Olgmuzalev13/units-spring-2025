import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        test_cases = [
            [1, -1, 0, "ok"],
            [0, 0, 0, "ok"],
            [7, 5, 12, "ok"],
            [-3, -11, -14, "ok"],
            [1.1, 2, 3.1, "ok"],
            [-1, 2, 1, "ok"],
            [10000000000000000000000000000000, 10000000000000000000000000000000, 20000000000000000000000000000000, "ok"],
            [-10000000000000000000000000000000, -10000000000000000000000000000000, -20000000000000000000000000000000, "ok"],
            [complex(1, 1), -1, complex(0, 1), "ok"],
            ["1", 2, TypeError, "err"],
            [None, 1, TypeError, "err"],
        ]
        func = self.calculator.addition
        test_all(self, test_cases, func)

    def test_multiplication(self):
        test_cases = [
            [0, 5, 0, "ok"],
            [7, 5, 35, "ok"],
            [-3, -11, 33, "ok"],
            [1.1, 2, 2.2, "ok"],
            [-1, 2, -2, "ok"],
            [10000000000000000000000000000000, 10000000000000000000000000000000, 100000000000000000000000000000000000000000000000000000000000000, "ok"],
            [complex(1, 1), complex(0, 1), complex(-1, 1), "ok"],
            ["1", "2", TypeError, "err"],
            [None, 1, TypeError, "err"],
        ]
        func = self.calculator.multiplication
        test_all(self, test_cases, func)

    def test_subtraction(self):
        test_cases = [
            [7, 7, 0, "ok"],
            [11, 5, 6, "ok"],
            [-11, -3, -8, "ok"],
            [4.1, 2, 2.1, "ok"],
            [-1, 2, -3, "ok"],
            [10000000000000000000000000000000, -10000000000000000000000000000000, 20000000000000000000000000000000, "ok"],
            [complex(1, 1), complex(10, 1), complex(-9, 0), "ok"],
            ["1", 2, TypeError, "err"],
            [None, 1, TypeError, "err"],
        ]
        func = self.calculator.subtraction
        test_all(self, test_cases, func)

    def test_division(self):
        test_cases = [
            [0, 11, 0, "ok"],
            [35, 5, 7, "ok"],
            [-33, -11, 3, "ok"],
            [2, 2, 1, "ok"],
            [-1, 2, -0.5, "ok"],
            [10000000000000000000000000000000, 0.00000000000000000000001, 1e+54, "ok"],
            [complex(2, 2), complex(3, 3), complex(0.66666, 0), "ok"],
            ["1", 2, TypeError, "err"],
            [1, 0, None, "ok"],
            [None, 1, TypeError, "err"],
        ]
        func = self.calculator.division
        test_all(self, test_cases, func)

    def test_absolute(self):
        test_cases = [
            [0, 0, "ok"],
            [7, 7, "ok"],
            [-33, 33, "ok"],
            [2.1, 2.1, "ok"],
            [-1, 1, "ok"],
            [10000000000000000000000000000000, 10000000000000000000000000000000, "ok"],
            [-10000000000000000000000000000000, 10000000000000000000000000000000, "ok"],
            [complex(2, 2), 2.828427, "ok"],
            ["1", TypeError, "err"],
            [None, 1, TypeError, "err"],
        ]
        func = self.calculator.absolute
        test_all(self, test_cases, func)

    def test_degree(self):
        test_cases = [
            [0, 5, 0, "ok"],
            [5, 0, 1, "ok"],
            [3, 5, 243, "ok"],
            [-5, -3, -0.008, "ok"],
            [2.1, 2, 4.41, "ok"],
            [-1, 2, 1, "ok"],
            [2, -1, 0.5, "ok"],
            [10000000000000000000000000000000, 2, 100000000000000000000000000000000000000000000000000000000000000, "ok"],
            [complex(1, 2), complex(3, 3), complex(0.34460, -0.21013), "ok"],
            ["1", 2, TypeError, "err"],
            [None, 1, TypeError, "err"],
        ]
        func = self.calculator.degree
        test_all(self, test_cases, func)

    def test_ln(self):
        test_cases = [
            [1, 0, "ok"],
            [1.5, 0.405465, "ok"],
            [10000000000000000000000000000000, 71.38013, "ok"],
            [0, ValueError, "err"],
            [-1, ValueError, "err"],
            [complex(1, 2), TypeError, "err"],
            ["1", TypeError, "err"],
            [None, 1, TypeError, "err"],
        ]
        func = self.calculator.ln
        test_all(self, test_cases, func)

    def test_log(self):
        test_cases = [
            [1, 2, 0, "ok"],
            [1, 7, 0, "ok"],
            [5.1, 2, 2.3505, "ok"],
            [10000000000000000000000000000000, 2, 71.38013, "ok"],
            [0, 1, ValueError, "err"],
            [1, 0, ValueError, "err"],
            [-2, 1, ValueError, "err"],
            [2, -1, ValueError, "err"],
            ["1", 2, TypeError, "err"],
            [None, 1, TypeError, "err"],
        ]
        func = self.calculator.log
        test_all(self, test_cases, func)

    def test_sqrt(self):
        test_cases = [
            [0, 0, "ok"],
            [4, 2, "ok"],
            [2.25, 1.5, "ok"],
            [100000000000000000000000000000000000000000000000000000000000000, 10000000000000000000000000000000, "ok"],
            [complex(3, 2), complex(1.81735, 0.55025), "ok"],
            [-1, complex(0, 1), "ok"],
            ["1", TypeError, "err"],
            [None, TypeError, "err"],
        ]
        func = self.calculator.sqrt
        test_all(self, test_cases, func)

    def test_nth_root(self):
        test_cases = [
            [0, 5, 0, "ok"],
            [27, 3, 3, "ok"],
            [2.25, 2, 1.5, "ok"],
            [2.25, 2.1, 1.47131, "ok"],
            [-1, 3, complex(0.5, 0.866025), "ok"],
            [2, -1, 0.5, "ok"],
            [100000000000000000000000000000000000000000000000000000000000000, 2, 10000000000000000000000000000000, "ok"],
            [complex(3, 2), complex(3, 2), complex(1.46890, -0.09061), "ok"],
            ["1", 2, TypeError, "err"],
            [2.25, 0, ZeroDivisionError, "err"],
            [None, 1, TypeError, "err"],
        ]
        func = self.calculator.nth_root
        test_all(self, test_cases, func)


def test_all(self, test_cases, func):
    for i in test_cases:
        if i[-1] == "ok":
            if len(i) == 4:
                self.assertAlmostEqual(func(i[0], i[1]), i[2], 4)
            else:
                self.assertAlmostEqual(func(i[0]), i[1], 4)
        elif i[-1] == "err":
            if len(i) == 4:
                self.assertRaises(i[2], func, i[0], i[1])
            else:
                self.assertRaises(i[1], func, i[0])


if __name__ == "main":
    unittest.main()
