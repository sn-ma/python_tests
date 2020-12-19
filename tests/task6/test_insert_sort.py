import unittest

from tasks.task6.insert_sort import insert_sort, insert_sorted


class TestInsertSorting(unittest.TestCase):
    def test_insert_sorting(self):
        arr = [3, 1, 6, 1, 9, 0, 1, 45, 6]
        self.assertEqual(sorted(arr), insert_sorted(arr))


if __name__ == '__main__':
    unittest.main()
