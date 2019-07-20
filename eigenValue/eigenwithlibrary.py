import numpy as np 
import sympy as sy
from sympy import init_printing
from sympy import pprint
init_printing()

__author__='SatoshiTerasaki<terasakisatoshi.math@gmail.com>'
__version__='1.0.0'
__date__='2017/02/25'

def calc_with_sympy(A):
    print("calc with sympy")
    print("A="),pprint(A)
    for eigen_value,multi,eigen_vect in A.eigenvects():
        print("eigen_value",eigen_value,"its multiplocity is",multi)
        print("eigen_vect corresponds the eigen_value is")
        pprint(eigen_vect)

def calc_with_numpy(A):
    print("calc with numpy")
    eigen_vals,eigen_vects=np.linalg.eig(A)
    for idx,val in enumerate(eigen_vals):
        print("eigen vector corresponds {} is {}".format(val,eigen_vects[:,idx]))

def main():
    A=[[1,-1,2],
       [0,-1,3],
       [0,3,-1]]
    calc_with_sympy(sy.Matrix(A))
    calc_with_numpy(np.array(A))
    
if __name__=='__main__':
    main()