"""
Написать программу, которая принимает на вход набор строк
(до пустой строки), состоящих из количества повторов (n) и
времени, затраченного на выполнение программы,
разделенные запятой, и оценивает соответствие роста затрат
времени функции n, n^2, ln(n). Считаем, что константа может
варьировать на 50%.
"""
import math
from collections import namedtuple


SingleRunResult = namedtuple("SingleRunResult", "n time")

__functions = {
    "O(n)": lambda n: n,
    "O(n**2)": lambda n: n ** 2,
    "O(log(n))": lambda n: math.log(n),
}


def analyse_o_notation(runs):
    """
    Returns list of appropriate O-notations for given run timings

    :param runs: iterable of SingleRunResult
    :return: list of strings (names of functions)
    """
    # Get rid of n=1 because log(1) is 0, and we don't want deal with zero division
    runs = list(filter(lambda r: r.n > 1, runs))
    result = []
    for fun_name, function in __functions.items():
        c_values = [r.time / function(r.n) for r in runs]
        c_min, c_max = min(c_values), max(c_values)
        if (c_max - c_min) / c_max < 0.5:
            result.append(fun_name)
    return result


if __name__ == '__main__':
    def read_run_results_from_input():
        while True:
            line = input()
            if not line:
                break
            n, time = (float(s.strip()) for s in line.split(","))
            yield SingleRunResult(n, time)
    print("Enter some function run results (in format 'n, time'), followed by an empty line:")
    analyse_result = analyse_o_notation(read_run_results_from_input())
    print("Acceptable O-notation(s):")
    print("\n".join("\t" + name for name in analyse_result))
