import functools

from tasks.task3.sequences import AbstractSequence, SequenceTypeMetadata


def d_print_self(foo):
    @functools.wraps(foo)
    def bar(*args, **kwargs):
        try:
            self_ = args[0]
            if isinstance(self_, AbstractSequence):
                print("Called method", foo.__name__, "on", self_)
        except IndexError:
            pass
        return foo(*args, **kwargs)
    return bar


class SomeOtherSequence(AbstractSequence):
    _metadata = SequenceTypeMetadata("ABCD", "SomeOtherSequence")

    @d_print_self
    def mass(self):
        return len(self)


if __name__ == '__main__':
    s = SomeOtherSequence("AABB")
    print("Mass of", s, "is", s.mass())
