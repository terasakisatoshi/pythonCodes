from collections import defaultdict
import math


def main():
    e = 5
    N = int(math.ceil((10**e)**(1 / 3.))) + 1
    print("N=", N)
    d = defaultdict(list)
    for i in range(1, N):
        for j in range(1 + i, N):
            for k in range(1 + j, N):
                for l in range(1 + k, N):
                    d[i**(e - 1) + j**(e - 1) + k**(e - 1) + l**(e - 1)].append((i, j, k, l))

    kmin = min([k for k, v in d.items() if len(v) == e - 1 and k >= 10**e])
    print(kmin)
    print(d[kmin])
if __name__ == '__main__':
    main()
