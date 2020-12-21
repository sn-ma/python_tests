def take_n(gen, n = 100):
    """Limit generator to first n values"""
    return (val for idx, val in zip(range(n), gen))