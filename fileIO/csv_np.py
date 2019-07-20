import numpy as np 

arr=np.fromfunction(lambda m,n:m*10+n,(3,3),dtype=int)
print(arr)

np.savetxt('test_np.csv',arr,delimiter=',',header='x,y,z',comments='#Comment line\n')

dat=np.loadtxt('test_np.csv',delimiter=',',skiprows=2)
print("dat",dat,type(dat))

subdat=np.loadtxt('test_np.csv',delimiter=',',skiprows=2,usecols=(0,2))

print(subdat)

x,y,z=np.loadtxt('test_np.csv',delimiter=',',skiprows=2,unpack=True)

print("x=",x)
print('y=',y)
print('z=',z)

