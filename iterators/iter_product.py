import time
import itertools


def naive(N):
    s = 0
    start_time = time.time()
    for i in range(N):
        for j in range(N):
            s += i + j
    end_time = time.time()
    return s, end_time - start_time


def product(N):
    s = 0
    start_time = time.time()
    for i, j in itertools.product(range(N), repeat=2):
        s += i + j
    end_time = time.time()
    return s, end_time - start_time


def main():
    N = 1000
    n_trial = 10
    naive_times = []
    product_times = []
    for _ in range(n_trial):
        naive_s, naive_elapsed = naive(N)
        prodcut_s, prodcut_elapsed = product(N)
        assert naive_s == prodcut_s
        naive_times.append(naive_elapsed)
        product_times.append(prodcut_elapsed)
    print(sum(naive_times) / n_trial)
    print(sum(product_times) / n_trial)

if __name__ == '__main__':
    main()
