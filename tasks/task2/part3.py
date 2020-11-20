"""
Написать программу, которая запрашивает на ввод целые числа, до тех пор, пока не будет введена пустая строка.
После каждого введенного числа программа возвращает ответ, делиться ли это число на 2, 3, 5, 7, 11.
"""


__dividers = (2, 3, 5, 7, 11)


def part3():
    while True:
        line = input("Enter some number: ")
        if line == "":
            break
        num = int(line)
        divides, non_divides = [], []
        for d in __dividers:
            if num % d == 0:
                divides.append(d)
            else:
                non_divides.append(d)
        if len(divides) > 0:
            print("{} divides by {}".format(num, ", ".join(str(d) for d in divides)))
        if len(non_divides) > 0:
            print("{} doesn't divides by {}".format(num, ", ".join(str(d) for d in non_divides)))


if __name__ == '__main__':
    part3()
