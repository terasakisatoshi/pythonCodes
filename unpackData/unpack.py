"""
reference:
Python3 in practice
"""


def print_args(*args, **kwargs):
    print(args.__class__.__name__, args,
          kwargs.__class__.__name__, kwargs)


def main():

    sequence = range(6)
    first, second, *rest = sequence
    print(first, second, rest, type(rest))

    print_args()
    print_args(1, 2, 3, a="A")
    print_args('p', 'q', 'r', u='U', v='V')


if __name__ == '__main__':
    main()
