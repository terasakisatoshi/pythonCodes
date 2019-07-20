import decimal
from decimal import Decimal

import sympy


def reciprocal(p, raw=False):
    decimal.getcontext().prec = p - 1
    r = Decimal(1) / Decimal(p)
    if raw:
        return r
    else:
        # only show digit part include dot
        # e.g. 0.142857 -> .142857
        return str(r)[1:]


def do_interesting(p):
    if p <= 7:
        raise ValueError("p must be larger than 5")
    r = reciprocal(p)
    v = int(r[(p - 1) // 2 + 1])
    assert v in [0, 9], 'actual v={}'.format(v)
    if v == 0:
        assert p % 40 in [1, 3, 9, 13, 27, 31, 37, 39], 'actual {} {}'.format(p, p % 40)
    if v == 9:
        assert p % 40 in [7, 11, 17, 19, 21, 23, 29, 33], 'actual {} {}'.format(p, p % 40)
    return v
if __name__ == '__main__':
    sympy.sieve.extend_to_no(300)
    for i, p in enumerate(sympy.sieve._list):
        if p <= 7:
            continue
        assert sympy.isprime(p)
        print((p - 1) // 2 + 1)
        print('check {}-th prime number = {}'.format(i, p))
        v = do_interesting(p=p)
        print(v)
    print('OK')
