import decimal
from decimal import Decimal

import sympy
from sympy import ntheory
from sympy import sieve


def reciprocal(p, raw=False):
    decimal.getcontext().prec = p - 1
    r = Decimal(1) / Decimal(p)
    if raw:
        return r
    else:
        # exclude `0.`
        # e.g. 0.142857 -> 142857
        return str(r)[2:]


def calc_recurrence_seq(p):
    decimal.getcontext().prec = p - 1
    r = reciprocal(p)
    for d in ntheory.divisors(p - 1):
        if d == 1 or d == p - 1:
            continue
        if r[:d] == r[d:2 * d]:
            return r[:d]
    return r[:p - 1]


def calc_some(p):
    if p <= 5:
        raise ValueError("p must be larger than 5")
    if not sympy.isprime(p):
        raise ValueError("specify prime. actual p = {}, ntheory.divisors = {}".format(p, ntheory.divisors(p)))
    r = reciprocal(p)
    seq = calc_recurrence_seq(p)
    d = len(seq)
    former = r[:d // 2]
    latter = r[d // 2:d]
    if d % 2 == 0:
        print('length of recurrence is even')
        print('1/{} = '.format(p), r)
        print('former = ', former)
        print('latter = ', latter)
        print('former + latter =\n', Decimal(former) + Decimal(latter))
    else:
        print('length of recurrence is not even. In fact')
        print('1/{}'.format(p), r)
        print('seq = ', seq)
        print('len(seq) = ', len(seq))
        print('But you may find something')
        if latter[0] == 9:
            print("you're lucky")
            print('former = ', former)
            print('latter = ', latter)
            print('former + latter =\n', Decimal(former) + Decimal(latter))

if __name__ == '__main__':
    calc_some(p=7)
    calc_some(p=11)
    calc_some(p=13)
    calc_some(p=19)
    calc_some(p=37)
    calc_some(p=193)
    calc_some(p=2011)
    calc_some(p=2017)
