import unittest

from tasks.task1.digits_convertion import my_int, int_to_str


class TestMethods(unittest.TestCase):
    def test_my_int(self):
        data = (
            ("123", 10),
            ("123", 8),
            ("123", 16),
            ("123", 33),
            ("abcd", 30),
            ("0", 20)
        )
        for s, base in data:
            got = my_int(s, base)
            expected = int(s, base)
            self.assertEqual(got, expected, "Converting string {} in base {} to integer. Got {}, but expected {}"
                             .format(s, base, got, expected))

    def test_my_int_fails(self):
        data = (
            ("-1", 10),
            ("1a", 10),
            ("10", 12345),
        )
        for s, base in data:
            with self.assertRaises(ValueError):
                my_int(s, base)

    def test_int_to_str(self):
        data = (
            (123, 10, "123"),
            (0o123, 8, "123"),
            (0x123abc, 16, "123abc"),
            (0, 16, "0")
        )
        for val, base, expected in data:
            got = int_to_str(val, base)
            self.assertEqual(got, expected, "Converting int {} to string with base {}. Got {}, but expected {}"
                             .format(val, base, got, expected))

    def test_int_to_str_fails(self):
        data = (
            (-1, 10),
            (123, 1),
            (123, -10),
            (123, 1234),
        )
        for val, base in data:
            with self.assertRaises(ValueError):
                int_to_str(val, base)


if __name__ == "__main__":
    unittest.main()
