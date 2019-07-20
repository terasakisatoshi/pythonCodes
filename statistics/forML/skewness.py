from matplotlib import pyplot as plt 
import numpy as np
from scipy import stats

def prob_function(sample):
    values=[]
    for i in [0,1,2,3,4,5]:
        value=np.where(np.array(sample)==i)
        values.append(len(value[0])/len(sample))
    return lambda i : values[i]

def expectation(func,var=lambda x:x):
    return sum([var(x)*func(x) for x in [0,1,2,3,4,5]])

def variance(func,var=lambda x:x):
    return expectation(func,lambda x:(x-expectation(func))**2)

def std_deviation(func,var=lambda x:x):
    return (variance(func,var))**0.5




def main():
    sample1=2*[0]+4*[1]+12*[2]+24*[3]+24*[4]+10*[5]
    sample2=6*[0]+14*[1]+18*[2]+18*[3]+14*[4]+6*[5]
    sample3=2*[5]+4*[4]+12*[3]+24*[2]+24*[1]+10*[0]

    fig=plt.figure(figsize=(12,6))

    ax1=fig.add_subplot(131)
    ax2=fig.add_subplot(132)
    ax3=fig.add_subplot(133)
    
    for i in [1,2,3]:
        eval("ax{0}.set_title(\
                'skew=%f'%stats.skew(sample{0}))".format(i))
        #eval("ax{0}.hist(sample{0})".format(i))
        sample=eval("sample{}".format(i))
        func=prob_function(sample)
        func=np.vectorize(func)
        print(expectation(func))
        print(variance(func))
        print(np.var(sample))
        print(std_deviation(func))
        print(np.std(sample))
        xs=np.array([0,1,2,3,4,5])
        ys=func(xs)
        print(ys)
        eval("ax{0}.plot(xs,ys)".format(i))

    plt.show()

if __name__ == '__main__':
    main()