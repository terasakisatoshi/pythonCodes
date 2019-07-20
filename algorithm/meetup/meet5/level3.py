import string
from itertools import tee, cycle


def prepare_method(step):
    alphabet = list(string.ascii_lowercase)
    crypto = cycle(alphabet)
    if step >= 0:
        for _ in range(step):
            crypto.__next__()
    else:
        # note that step is negative
        for _ in range(len(alphabet) + step):
            crypto.__next__()

    cryptographic_methods = {w: c for w, c in zip(alphabet, crypto)}
    # insert space method
    cryptographic_methods[" "] = " "
    return cryptographic_methods


def algorithm(input_words, step):
    method = prepare_method(step)
    ret = "".join([method[w] for w in input_words])
    return ret


def main():
    assert algorithm("dog", 4) == "hsk"
    assert algorithm("spaces here", -1) == "rozbdr gdqd"

if __name__ == '__main__':
    main()
