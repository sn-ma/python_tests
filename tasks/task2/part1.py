"""
Написать программу, которая запрашивает на ввод целые числа, до тех пор, пока не будет введена пустая строка.
Затем она выводит: а) введенную последовательность чисел; б) сумму введенных чисел; в) самое большое число из введенных.
(а), (б) и (в) – это разные варианты одной программы.
"""


def part1(modes: str = "abc"):
    """
    :param mode: 'a' to print entered number sequence, 'b' to print the sum, 'c' to print the max value
    """
    numbers = []
    while True:
        line = input("Введите число: ")
        if line == "":
            break
        numbers.append(int(line))
    if "a" in modes:
        print("Вы ввели: ", ', '.join(str(n) for n in numbers))
    if "b" in modes:
        print("Сумма", sum(numbers))
    if "c" in modes:
        print("Максимум", max(numbers))


if __name__ == '__main__':
    part1()
