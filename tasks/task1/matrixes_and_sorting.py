from copy import deepcopy
import random


def generate_filled_matrix(n: int) -> list:
    """Generate matrix n*n filled with numbers from 1 to n*n"""
    return [[column + line * n + 1 for column in range(n)] for line in range(n)]


def generate_filled_matrix_random(n: int) -> list:
    """Generate matrix n*n filled with numbers from 1 to n*n in random order"""
    digits = list(range(1, n*n + 1))
    random.shuffle(digits)
    return [[digits[column + line * n] for column in range(n)] for line in range(n)]


def matrix_to_str(matrix: list) -> str:
    """Convert two-dimensional list to string"""
    return '\n'.join('\t'.join(str(e) for e in line) for line in matrix)


def matrix_sorted(matrix: list) -> list:
    """Sort given matrix by sum of it's lines and columns"""
    matrix = deepcopy(matrix)
    n = len(matrix)

    # Sort lines
    for i in range(n - 1):
        for j in range(i + 1, n):
            if sum(matrix[i]) > sum(matrix[j]):
                matrix[i], matrix[j] = matrix[j], matrix[i]

    def col_sum(col): return sum(matrix[line][col] for line in range(n))

    def swap_columns(col1, col2):
        for line in range(n):
            matrix[line][col1], matrix[line][col2] = matrix[line][col2], matrix[line][col1]

    # Sort columns
    for i in range(n - 1):
        for j in range(i + 1, n):
            if col_sum(i) > col_sum(j):
                swap_columns(i, j)

    return matrix


if __name__ == '__main__':
    # n = 3
    n = int(input("Enter matrix size: "))
    m = generate_filled_matrix_random(n)
    print(matrix_to_str(m))
    print()

    s = matrix_sorted(m)
    print(matrix_to_str(s))
    print()

    print("Line sums:", [sum(line) for line in s])
    print("Col. sums:", [sum(line[col_idx] for line in s) for col_idx in range(n)])
