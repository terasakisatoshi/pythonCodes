def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def lemma():
    print('HI')


def test_lemma():
    print("test_lemma is called")


def test_fails():
    assert (1, 2, 3) == (3, 2, 1)

import numpy as np


def test_npfalls():
    a = [[i for i in range(10)] for j in range(10)]
    b = [[i for i in range(10, 0, -1)] for j in range(10)]
    assert a == b
