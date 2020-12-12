import functools
from dataclasses import dataclass
from typing import Any


@dataclass
class Ref:
    var: Any


def d_print_count(foo):
    counter = Ref(0)

    @functools.wraps(foo)
    def bar(*args, **kwargs):
        counter.var += 1
        print("Called", counter.var, "time(s)")
        return foo(*args, **kwargs)

    return bar


@d_print_count
def buzz():
    pass


@d_print_count
def foobar():
    pass


if __name__ == '__main__':
    for _ in range(10):
        buzz()
    foobar()
