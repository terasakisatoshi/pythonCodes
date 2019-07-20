import random
import copy
import time
from numba import jit
from array_creator import create_test_set
from measure import get_elapsed_data


@get_elapsed_data
def scratch_lin_search(test_set):
    hit = False
    for key, arr in test_set:
        for i in arr:
            if i == key:
                break


@get_elapsed_data
def std_search(test_set):
    for key, arr in test_set:
        if key in arr:
            continue


def main():
    size = 100000
    trial = 1
    test_set = create_test_set(size, trial)
    original = list(range(size))
    print(scratch_lin_search(test_set))
    print(std_search(test_set))

if __name__ == '__main__':
    main()
