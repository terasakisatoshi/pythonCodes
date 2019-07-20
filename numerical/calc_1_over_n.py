import numba 
from numba import jit
import math
@jit
def main():
    max_count=100000
    total_sum=0
    for n in range(1,max_count):
        total_sum+=float(1)/n
    print(total_sum)


if __name__ == '__main__':
    main()