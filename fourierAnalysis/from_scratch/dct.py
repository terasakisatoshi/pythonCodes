import numpy as np 
from matplotlib import pyplot as plt

pi=np.pi
T=np.pi

def func(t):
	return pi-t

def main():
	N=8
	D=T/N
	ts=np.array([(2*n+1)/2*D for n in range(N)])
	xs=func(ts)
	components=[1/N]
	components+=[2/N for _ in range(1,N)]
	diag=np.diag(components)
	mat=np.array([[np.cos(n*pi*(2*i+1)/2.0/N) for i in range(N)]
					 						  for n in range(N)])
	dct_coefficients=diag @ mat @ xs

	new_xs=mat.T @ dct_coefficients

	fig=plt.figure()
	ax1=fig.add_subplot(121)
	ax1.bar(np.arange(N),dct_coefficients,align='center',width=0.4)
	ax1.set_xlim(0.5,N-0.5)
	
	ax2=fig.add_subplot(122)
	interval=np.linspace(0,T,100)
	ax2.plot(interval,func(interval))
	f=lambda t: sum([dct_coefficients[n] * np.cos(n*pi*t/T) for n in range(N)])
	ax2.plot(ts,f(ts),'x')
	plt.show()
if __name__ == '__main__':
	main() 