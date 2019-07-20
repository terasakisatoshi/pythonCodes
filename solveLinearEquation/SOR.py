import numpy as np
import sympy as sy 

epsilon=0.0001
maxiteration=100
#SOR = Successive Over-Relaxation
def main():
    n=10
    # prepare matrix a
    a=np.diag([5.]*n)
    a+=np.diagflat([2.]*(n-1),1)
    a+=np.diagflat([2.]*(n-1),-1)
    print(a)

    b=np.array([3,1,4,0,5,-1,6,-2,7,-15],dtype='f').T
    #initial value x
    x=np.ones(10).T

    D=np.diag(np.diag(a))
    L=np.tril(a,-1)
    U=np.triu(a,+1)
    omega=1.22
    M= np.linalg.inv(D+omega * L) @ ((1-omega)*D-omega*U)
    N=omega * np.linalg.inv(D + omega * L)
    for k in range(maxiteration):
        x_new=M @ x + N @ b
        if(np.linalg.norm(x_new-x) <epsilon):
            break
        x=x_new
    else:
        print("fail SOR method ...")
        exit(1)

    print("the sol of ax = b using SOR method is \n{}".format(x))
    print("iteration {} times".format(k))
    print("indeed ax-b is \n{}".format(a @x -b))
    print("you can check sol x using sympy...")
    sy_a=sy.Matrix(a)
    sy_x=sy_a.solve(b)
    print(sy_x)

if __name__ == '__main__':
    main()



