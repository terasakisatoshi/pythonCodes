import string
from itertools import tee, cycle


def prepare_method():
    alphabet = list(string.ascii_lowercase)
    crypto = cycle(alphabet)
    crypto.__next__()
    cryptographic_methods = {w: c for w, c in zip(alphabet, crypto)}
    # insert space method
    cryptographic_methods[" "] = " "
    return cryptographic_methods


def algorithm(input_words):
    method = prepare_method()
    ret = "".join([method[w] for w in input_words])
    return ret


def main():
    print(algorithm("dog"))
    print(algorithm("spaces here"))

if __name__ == '__main__':
    main()
