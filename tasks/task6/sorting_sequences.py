"""
Используя классы последовательностей и функцию из предыдущего задания,
написать функцию для сортировки последовательностей
по возрастанию количества замен относительно референса. Все последовательности одной длины.
"""
from functools import lru_cache

from tasks.task6.insert_sort import insert_sort


@lru_cache
def sequence_distance(seq1, seq2):
    assert len(seq1) == len(seq2)
    return sum(1 if e1 != e2 else 0 for e1, e2 in zip(seq1, seq2))


def sequences_sort(lst, ref):
    def key_function(seq):
        return sequence_distance(seq, ref)
    insert_sort(lst, key_function)


def sequences_sorted(lst, ref):
    cpy = lst.copy()
    sequences_sort(cpy, ref)
    return cpy
