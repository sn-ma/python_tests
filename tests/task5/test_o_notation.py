import math
import unittest

from tasks.task5.o_notation import SingleRunResult, analyse_o_notation


class TestONotation(unittest.TestCase):
    def test_o_notation(self):
        self.assertEqual(["O(n)"], analyse_o_notation([
            SingleRunResult(10, 98),
            SingleRunResult(2, 21),
            SingleRunResult(100, 1009),
        ]))
        self.assertEqual(["O(n)"], analyse_o_notation([
            SingleRunResult(10, 1),
            SingleRunResult(2, 0.2),
            SingleRunResult(100, 10),
        ]))
        self.assertEqual(["O(n**2)"], analyse_o_notation([
            SingleRunResult(10, 3 * 10 ** 2),
            SingleRunResult(2, 3 * 2 ** 2 * 1.1),
            SingleRunResult(100, 3 * 100 ** 2 * 0.9),
        ]))
        self.assertEqual(["O(log(n))"], analyse_o_notation([
            SingleRunResult(10, math.log(10)),
            SingleRunResult(2, math.log(2) * 1.1),
            SingleRunResult(100, math.log(100) * 0.9),
        ]))


if __name__ == '__main__':
    unittest.main()
