def create_stats_calc(alphabet):
    def foo(sequence):
        stat = {letter: 0 for letter in alphabet}
        for ch in sequence:
            try:
                stat[ch] += 1
            except KeyError:
                raise Exception("Wrong letter (not in alphabet)")
        return stat
    return foo
