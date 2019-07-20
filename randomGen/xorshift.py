"""
implement xorshift with python
https://ja.wikipedia.org/wiki/Xorshift
https://qiita.com/yosgspec/items/e4287262f8dbea2aa815
https://ask.helplib.com/1591921
"""

from numba import jit


def xorshift(generator, seed=None):
    ret = seed
    def inner():
        nonlocal ret
        if ret is None:
            ret = generator()
        else:
            ret = generator(*ret)
        return ret[-1]
    return inner


@jit
def xor32(y=2463534242):
    y = y ^ (y << 13 & 0xFFFFFFFF)
    y = y ^ (y >> 17 & 0xFFFFFFFF)
    y = y ^ (y << 5 & 0xFFFFFFFF)
    return y & 0xFFFFFFFF,


#@jit
#def xor64(_x=88172645463325252, x=88172645463325252):
#    _x = _x ^ (_x << 13)
#    _x = _x ^ (_x >> 7)
#    _x = _x ^ (_x << 17)
#    return _x, _x & 0xFFFFFFFF


@jit
def xor96(x=123456789, y=362436069, z=521288629):
    t = (x ^ (x << 3 & 0xFFFFFFFF)) ^ (
        y ^ (y >> 19 & 0xFFFFFFFF)) ^ (
        z ^ (z << 6 & 0xFFFFFFFF))
    x = y
    y = z
    z = t
    return x, y, z


@jit
def xor128(x=123456789, y=362436069, z=521288629, w=88675123):
    t = x ^ (x << 11) & 0xFFFFFFFF
    x = y
    y = z
    z = w
    w = (w ^ (w >> 19)) ^ (t ^ (t >> 8)) & 0xFFFFFFFF
    return x, y, z, w


def uniform(rand, begin=0, end=1):
    def inner():
        return begin+(rand())/(int(0xFFFFFFFF)/(end-begin))
    return inner


def calc_pi(generator):
    u01 = uniform(generator)
    counter = 0
    N = 1000000
    for i in range(N):
        x = u01()
        y = u01()
        if x*x+y*y < 1.0:
            counter += 1
    print(4.0*counter/N)


def apply_example():
    random32 = xorshift(xor32)
    calc_pi(random32)
    #random64 = xorshift(xor64)
    #calc_pi(random64)
    #random96 = xorshift(xor96)
    #calc_pi(random96)
    #random128 = xorshift(xor128)
    #calc_pi(random128)

def main():
    #random32=xorshift(xor32)
    #for i in range(100):
    #    print(random32())

    apply_example()
if __name__ == '__main__':
    main()
