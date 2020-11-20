from collections import Counter


"""
Написать программу, которая запрашивает на ввод произвольную строку текста (написанную с  использованием латинского
алфавита).
Программа выводит:
    а) эту же строку, но без гласных;
    б) список использованных гласных;
    в) количество использованных гласных;
    г) статистику по встречаемости (буква – количество ее вхождений в строку).
(а), (б), (в) и (г) – это разные варианты одной программы.
"""


vowels = "aeioquy"


def part2(modes = "abcd"):
    """
    :param modes: iterable with or without letters a, b, c or d
    """
    line = input("Enter some line: ")
    if "a" in modes:
        print("Without vowels:", ''.join(letter for letter in line if letter not in vowels))
    if "b" in modes:
        print("Vowels used:", ", ".join(v for v in vowels if v in line))
    if "c" in modes:
        print("Total vowels count:", sum(1 for letter in line if letter in vowels))
    if "d" in modes:
        print("Letters counts:")
        for letter, count in Counter(line).items():
            print("\t{}: {} time(s)".format(letter, count))


if __name__ == '__main__':
    part2()