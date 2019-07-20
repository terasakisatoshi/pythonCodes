import numpy as np
from matplotlib import pyplot as plt 

COEFF=0.05
EPSILON=0.1

def function(x):
    return np.sin(x) * np.exp(-COEFF*x)

def upper(x):
    return np.exp(-COEFF*x)

def lower(x):
    return -np.exp(-COEFF*x)

def main():
    xmax=100
    xs=np.linspace(0,xmax,1000)
    ys=function(xs)

    ns=[n for n in range(xmax)]
    seq=[function(n) for n in ns]

    fig,ax=plt.subplots(figsize=(12,8))
    ax.set_title(r"An Introduction to $\epsilon$-$N$ method")
    ax.set_xlabel(r"$n$", fontsize=20)
    ax.set_ylabel(r"$a_n$", fontsize=20)

    ax.plot(xs,function(xs),'--',markersize=2)
    ax.plot(ns,seq,'bo',label=r'$a_n=\sin(n) \exp(-{}n)$'.format(COEFF),markersize=3)

    ax.annotate(r'$\exp(-{}x)$'.format(COEFF),xy=(20,upper(20)),xycoords='data',
                    arrowprops=dict(arrowstyle="->"),
                    xytext=(+10,+30),textcoords='offset points')
    
    ax.plot(xs,upper(xs),'--')
    ax.annotate(r'$\exp(-{}x)$'.format(COEFF),xy=(20,upper(20)),xycoords='data',
                    arrowprops=dict(arrowstyle="->"),
                    xytext=(+10,+30),textcoords='offset points')

    ax.plot(xs,lower(xs),'--')
    ax.annotate(r'$-\exp(-{}x)$'.format(COEFF),xy=(20,lower(20)),xycoords='data',
                    arrowprops=dict(arrowstyle="->"),
                    xytext=(+10,-30),textcoords='offset points')

    N=np.log(EPSILON)/-COEFF
    #to show epsilon bound
    ax.plot([N,xmax],[EPSILON,EPSILON],linewidth=0.25,linestyle="--",color='r')
    ax.annotate(r'$\epsilon=$ %f'% EPSILON ,xy=((N+100)/2.0,EPSILON),xycoords='data',
                    arrowprops=dict(arrowstyle="->"),
                    xytext=(+10,+30),fontsize=12,textcoords='offset points')

    ax.plot([N,xmax],[-EPSILON,-EPSILON],linewidth=0.25,linestyle="--",color='r')
    ax.annotate(r'$\epsilon=$ %f'% -EPSILON ,xy=((N+100)/2.0,-EPSILON),xycoords='data',
                    arrowprops=dict(arrowstyle="->"),
                    xytext=(+10,-30),fontsize=12,textcoords='offset points')

    ax.plot([N,N],[ax.get_ylim()[0],EPSILON],linewidth=0.25,linestyle="--",color='r')
    ax.annotate(r'$N$=%d'%N, xy=(N,ax.get_ylim()[0]),xycoords='data',
                    arrowprops=dict(arrowstyle="->"),
                    xytext=(+10,+30),fontsize=24,textcoords='offset points')

    ax.legend(loc='upper right')

    plt.show()

if __name__ == '__main__':
    main()