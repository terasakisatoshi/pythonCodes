import numpy as np

def main():
    a=np.matrix([[2,-1,0,0],
                 [-1,3,-1,0],
                 [0,-1,3,-1],
                 [0,0,-1,2]],dtype='float64')
    b=np.matrix([4,-10,15,-11],dtype='float64').T

    ori_a,ori_b=a.copy(),b.copy()
    (row,col)=a.shape
    for i in range(1,row):
        for j in range(i):
            a[i,j]=(a[i,j]-np.sum((a[i,k]*a[k,k]*a[j,k] for k in range(j))))/a[j,j]
        a[i,i]-=np.sum(a[i,k]*a[i,k]*a[k,k] for k in range(i))

    for i in range(col):
        b[i]=(b[i]-np.sum((a[j,j]*a[i,j]*b[j] for j in range(i))))/a[i,i]
    for i in range(col-1)[::-1]:
        b[i]-=np.sum((a[j,i]*b[j] for j in range(i+1,col)))
        sol=b
    print("sol of ax=b is \n{}".format(sol))
    #to check ...
    print(ori_a @ sol - ori_b)

if __name__ == '__main__':
    main()