def insert_sort(lst: list, key = lambda x: x):
    for i in range(1, len(lst)):
        buf = lst[i]
        buf_key = key(buf)
        for j in range(i - 1, -1, -1):
            if key(lst[j]) > buf_key:
                lst[j + 1] = lst[j]
            else:
                lst[j + 1] = buf
                break
        else:
            lst[0] = buf


def insert_sorted(lst: list, key = lambda x: x):
    cpy = lst.copy()
    insert_sort(cpy, key)
    return cpy
