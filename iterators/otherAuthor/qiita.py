import itertools
import time


def naive(N, repeat):
    # prepare code
    tab = "\t"
    func = '\n'.join(['def loop_func(N):', tab + 's = 0'])
    loop_txt = lambda n: (n + 1) * tab + "for item_{} in range(N):".format(n)
    calc = lambda n:  (n + 1) * tab + 's += ' + \
        ' + '.join(["item_{}".format(_) for _ in range(n)])
    code = "\n".join([func] +
                     [loop_txt(n) for n in range(repeat)] +
                     [calc(repeat)] +
                     [tab + 'return s'])

    # print(code)
    exec(code)
    start_time = time.time()
    s = eval("loop_func({})".format(N))
    end_time = time.time()
    elapsed = end_time - start_time
    return s, elapsed


def product(N, repeat):
    # prepare code
    tab = '\t'
    items = ' , '.join('item_{}'.format(_) for _ in range(repeat))
    sum_items = ' + '.join('item_{}'.format(_) for _ in range(repeat))
    forloop = ' '.join([tab + 'for',
                        items, 'in',
                        'itertools.product(range(N), repeat=repeat):'])
    code = '\n'.join(['def loop_func(N, repeat):', tab + 's = 0', forloop,
                      2 * tab + 's += ' + sum_items, tab + 'return s'])
    # print(code)
    exec(code)
    start_time = time.time()
    s = eval("loop_func({}, {})".format(N, repeat))
    end_time = time.time()
    return s, end_time - start_time


def main():
    N = 10
    n_trial = 50
    repeat = 6
    naive_times = []
    product_times = []
    for _ in range(n_trial):
        naive_s, naive_elapsed = naive(N, repeat)
        prodcut_s, prodcut_elapsed = product(N, repeat)
        assert naive_s == 27000000
        assert prodcut_s == 27000000
        naive_times.append(naive_elapsed)
        product_times.append(prodcut_elapsed)
    print(sum(naive_times) / n_trial)
    print(sum(product_times) / n_trial)

if __name__ == '__main__':
    main()
