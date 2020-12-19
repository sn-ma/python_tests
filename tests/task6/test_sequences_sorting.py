import unittest

from tasks.task3.sequences import DNA
from tasks.task6.sorting_sequences import sequences_sorted


class TestSequencesSorting(unittest.TestCase):
    def test_sequences_sorting(self):
        ref = DNA("GATTACA", "Gattaca")
        lst = [
            DNA("CTCTACA"),
            DNA("GATTACA"),
            DNA("AGCCGAG"),
            DNA("GATCACA"),
        ]
        lst_sorted = [
            DNA("GATTACA"),
            DNA("GATCACA"),
            DNA("CTCTACA"),
            DNA("AGCCGAG"),
        ]
        self.assertEqual(lst_sorted, sequences_sorted(lst, ref))


if __name__ == '__main__':
    unittest.main()
