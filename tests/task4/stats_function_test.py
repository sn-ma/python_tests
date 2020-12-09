import unittest

from tasks.task4.stats_function import create_stats_calc
from tasks.task3.sequences import DNA, RNA


class MyTestCase(unittest.TestCase):
    def test_something(self):
        dna = DNA("GATTACAGGGAAATTACAAAA")
        self.assertEqual(dna.get_stat(), create_stats_calc(DNA.metadata().alphabet)(dna))

        with self.assertRaises(Exception):
            create_stats_calc(RNA.metadata().alphabet)(dna)


if __name__ == '__main__':
    unittest.main()
