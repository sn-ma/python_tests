import unittest

from tasks.snma_tools import take_n


class TestSnmaTools(unittest.TestCase):
    def test_take_n(self):
        def inf_gen():
            val = 0
            while True:
                yield val
                val += 1

        self.assertEqual(list(range(10)), list(take_n(inf_gen(), 10)))
        self.assertEqual(list(range(100)), list(take_n(inf_gen())))


if __name__ == '__main__':
    unittest.main()
