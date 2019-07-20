from measure import measure_time
from numba import jit
import numpy as np
from array import array


@measure_time
def py_max(array):
    max_value = max(array)
    return max_value


@measure_time
def np_max(array):
    max_value = np.max(array)
    return max_value


@measure_time
@jit('int64(int64[:])')
def scratch_max_with_annotate(array):
    ret = array[0]
    for value in array:
        ret = value if ret < value else ret
    return ret


@measure_time
@jit
def scratch_max_jit(array):
    ret = array[0]
    for value in array:
        ret = value if ret < value else ret
    return ret


@measure_time
def scratch_max(array):
    ret = array[0]
    for value in array:
        ret = value if ret < value else ret
    return ret


@measure_time
def get_shuffled_list(arr):
    return shuffle_list(arr)


def bench_mark(arr):
    print('before shuffle', type(arr))
    np.random.shuffle(arr)
    print('after shuffle', type(arr))
    print(scratch_max(arr))
    print(scratch_max_jit(arr))
    print(scratch_max_with_annotate(arr))
    print(py_max(arr))
    print(np_max(arr))


def main():
    N = 100000000
    #bench_mark(list(range(N)))
    #bench_mark(array('L', list(range(N))))
    bench_mark(np.arange(N))

if __name__ == '__main__':
    main()
