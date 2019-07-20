import numpy as np

a=[3,1,4,1]

def horner_method(a,x):
    """calc poly f(x)=sum(a[i]*x**i) using Horner method"""
    b_pre=0
    for i in range(len(a)):
        b=b_pre*x+a[i]
        b_pre=b
    return b
    
def simple_method(a,x):
    n=len(a)
    return sum([a[i]*(x**(n-(i+1))) for i in range(n)])
    

def main():
    a=[3,1,4,1]
    x=1
    fx=horner_method(a,x)
    print(fx)
    fx=simple_method(a,x)
    print(fx)
    
if __name__ == '__main__':
    main()