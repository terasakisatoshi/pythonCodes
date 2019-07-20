import numpy as np

def lu_decomp(a,swap):
    (row,col)=a.shape
    for j in range(row):
        #search pivot
        maxind=j+np.argmax(abs(a[j:,j]))
        swap[j]=maxind
        #swap!
        a[[j,maxind],j:]=a[[maxind,j],j:]
        pivot=a[j,j]
        for i in range(j+1,row):
            p= -a[i,j]/pivot
            a[i,j:]+=p*a[j,j:]
            #memorize value p at [i,j] of a
            a[i,j]=p

def push_forward(a,swap,b):
    (row,col)=a.shape
    for j in range(row):
        #swap!
        b[[swap[j],j]]=b[[j,swap[j]]]
        for i in range(j+1,row):
            b[i]+= a[i,j] * b[j]

def back_forward(a,b,x):
    row=len(x)
    for i in range(row)[::-1]:
        x[i]=(b[i]-np.dot(a[i,i+1:row],x[i+1:row]))/a[i,i]

def main():
    a=np.matrix([[2,4,6],
                 [1,-1,5],
                 [4,1,-2]],dtype='float64')
    b=np.matrix([28,7,21],dtype='float64').T
    x=np.array([[None]*len(b)],dtype='float64').T
    swap=np.zeros(len(b),dtype='i').T

    lu_decomp(a,swap)
    push_forward(a,swap,b)
    back_forward(a,b,x)
    print("sol of ax=b with respect to x is =\n{}".format(x))

if __name__ == '__main__':
    main()