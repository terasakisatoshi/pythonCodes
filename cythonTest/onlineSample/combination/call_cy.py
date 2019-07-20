from cy_combination import naive, opt1, opt2, opt_numpy, opt_cnumpy

import time


def test_naive():
    N = 10000
    start = time.time()
    total = naive(N)
    end = time.time()
    print(total)
    print('elapsed=', end-start)


def test_opt1():
    N = 10000
    start = time.time()
    total = opt1(N)
    end = time.time()
    print(total)
    print('elapsed=', end-start)

def test_opt2():
    N = 10000
    start = time.time()
    total = opt2(N)
    end = time.time()
    print(total)
    print('elapsed=', end-start)

def test_opt_numpy():
    N = 10000
    start = time.time()
    total = opt1(N)
    end = time.time()
    print(total)
    print('elapsed=', end-start)


def test_opt_cnumpy():
    N = 10000
    start = time.time()
    total = opt1(N)
    end = time.time()
    print(total)
    print('elapsed=', end-start)


def main():
    # test_naive()
    test_opt1()
    test_opt2()
    test_opt_numpy()
    test_opt_cnumpy()

if __name__ == '__main__':
    main()
