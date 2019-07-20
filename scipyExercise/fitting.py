"""
reference
http://oppython.hatenablog.com/entry/2015/09/28/222920
"""

import numpy as np 
from matplotlib import pyplot as plt 
from scipy import optimize

def approximate_polynomial(coefficients,x,y=0):
    """calc polynomial f(x)=sum(a[i]*x**i) using Horner method"""
    fx=0
    for i in range(len(coefficients)):
        b=fx*x+coefficients[i]
        fx=b
    residual=fx-y
    return residual

def main():
    low,sup=-5,10
    num_scan=15
    degree=7
    score_list=np.array(np.random.randint(low,sup,num_scan))

    xs=np.array(range(num_scan))
    scores=np.array(score_list)
    
    init_coefficients=np.zeros(degree)
    optimized=optimize.leastsq(approximate_polynomial,init_coefficients,args=(xs,scores))
    print(optimized[0])
    approximated_value=approximate_polynomial(optimized[0],xs)

    fig,ax=plt.subplots()
    ax.plot(xs,scores,'o')
    ax.plot(xs,approximated,'-')
    plt.show()
if __name__ == '__main__':
    main()