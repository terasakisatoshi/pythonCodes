import numpy as np 
from matplotlib import pyplot as plt 
from scipy import integrate

Pi=np.pi
T=2*Pi
N= 50

target_func=None
fourier_series=None

def getVarName( var, symboltable, error=None ) :
    """
    Return a var's name as a string.\nThis funciton require a symboltable(returned value of globals() or locals()) in the name space where you search the var's name.\nIf you set error='exception', this raise a ValueError when the searching failed.
    """
    for k,v in symboltable.items() :
        if id(v) == id(var) :
            return k
    else :
        if error == "exception" :
            raise ValueError("Undefined function is mixed in subspace?")
        else:
            return error

def step_func(xs):
	return np.where(xs<0,0,1)

def linear(xs,a=1):
	return a*xs

def plot_func(funcs,func_name="function"):
	fig,ax=plt.subplots()
	for func in funcs:
		xs=np.linspace(-T/2,T/2,5000)
		ys=func[0](xs)
		ax.plot(xs,ys,label=func[1])
	ax.legend()
	ax.set_title("target_func (= "+func_name+" ) and its fourier series")
	plt.savefig(func_name+".png")
	plt.show()

def get_fourier(func,func_name):
	ts=np.linspace(-T/2,T/2,5000)
	A0=integrate.simps((lambda t:func(t)/T)(ts),ts) 
	As=np.array([integrate.simps((lambda t:2*func(t)*np.cos(2*n*Pi*t/T)/T)(ts),ts) for n in range(1,N)],dtype=np.float64)
	Bs=np.array([integrate.simps((lambda t:2*func(t)*np.sin(2*n*Pi*t/T)/T)(ts),ts) for n in range(1,N)],dtype=np.float64)
	Explicit_Bs=np.array([(1-(-1)**n)/(n*Pi) for n in range(1,N)])
	print(Explicit_Bs)
	cos_part=lambda t : np.array([np.cos(2*n*Pi*t/T) for n in range(1,N)],dtype=np.float64)
	sin_part=lambda t : np.array([np.sin(2*n*Pi*t/T) for n in range(1,N)],dtype=np.float64)

	global target_func,fourier_series
	target_func=func
	fourier_series=lambda t: A0+As.dot(cos_part(t))+Bs.dot(sin_part(t))
	plot_func([(func,getVarName(func,globals())) for func in [func,fourier_series]],func_name)

def main():
	get_fourier(step_func,getVarName(step_func,globals()))
	get_fourier(linear,getVarName(linear,globals()))
if __name__ == '__main__':
	main()