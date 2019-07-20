from optxorshift import cycalc_pi,u01
from xorshift import calc_pi
from numba import jit


def pycalc_pi(N):
    counter=0
    for i in range(N):
        x = u01()
        y = u01()
        if x*x+y*y < 1.0:
            counter += 1
    print(4.0*counter/N)

def main():
    N=10000000
    pycalc_pi(N)

if __name__ == '__main__':
	main()