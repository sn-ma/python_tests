import string

# list of symbols from 0 to z
_symbols = string.digits + string.ascii_lowercase

# mapping from symbol to it's number value
_numbers = {ch: i for i, ch in enumerate(_symbols)}


def my_int(s: str, base: int = 10) -> int:
    """Converts the string to int with given base, like built-in int() method"""
    if base > len(_symbols):
        raise ValueError("Too big base ({} at most is supported)".format(len(_symbols)))
    try:
        digits = [_numbers[ch.lower()] for ch in s]
    except KeyError:
        raise ValueError("Wrong characters in given string! Only numbers and digits supported")
    if any(d >= base for d in digits):
        raise ValueError("Wrong symbols for base {}".format(base))

    def gen_multipliers():
        m = 1
        while True:
            yield m
            m *= base

    return sum(d * m for d, m in zip(reversed(digits), gen_multipliers()))


def int_to_str(val: int, base: int = 10) -> str:
    """Converts int to string with given base"""
    if val < 0:
        raise ValueError("Negative numbers are not yet supported")
    if not 2 <= base <= len(_symbols):
        raise ValueError("Invalid base (supported values: from 2 to {})".format(len(_symbols)))

    if val == 0:
        return _symbols[0]

    def rev_digits():
        x = val
        while x > 0:
            yield x % base
            x //= base

    digits = reversed(list(rev_digits()))
    return ''.join(_symbols[d] for d in digits)


if __name__ == '__main__':
    base_in = my_int(input("Base for first two numbers: "))
    val1, val2 = (my_int(s, base_in) for s in (input("First number: "), input("Second number: ")))
    base_out = my_int(input("Base for sum: "))
    print("Sum in base {}: {}".format(base_out, int_to_str(val1 + val2, base_out)))
