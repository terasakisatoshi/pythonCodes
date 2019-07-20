from calcpoly import horner_method
epsilon=0.001
h=0.0001
def diff(f,x):
    return (f(x+h)-f(x))/h
def main():
    a=[1,-3,2]
    f=lambda x:horner_method(a,x)
    df=lambda x:diff(f,x)
    x_init=-45
    x=x_init
    x_new=-x
    while(abs(x_new-x)>epsilon):
        x=x_new
        x_new=x-f(x)/df(x)
        print("abs=%s"%abs(x_new-x))
        print(x)
        
    print('the solution x is %s'%x)
    print('infact f({})={}'.format(x,f(x)))
if __name__=='__main__':
    main()