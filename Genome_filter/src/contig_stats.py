import numpy as np


def total_len(xs):
    return sum(xs)


def count(xs):
    return len(xs)


def quality(xs, level=50):
    sorted_len = sorted(xs, reverse=True)
    threshold = total_len(xs) * level / 100
    acc = 0
    for l in sorted_len:
        acc += l
        if acc > threshold:
            return l


def seq_quality(xs):
    n25 = quality(xs, level=25)
    n50 = quality(xs, level=50)
    n75 = quality(xs, level=75)
    return n25, n50, n75


def stats(recs):
    xs = list(map(lambda x: len(x.seq), recs))
    m = total_len(xs)
    c = count(xs)
    n25, n50, n75 = seq_quality(xs)
    return n25, n50, n75, m, c
