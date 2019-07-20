import numpy as np 
from matplotlib import pyplot as plt 
#reference:https://matplotlib.org/1.2.1/examples/api/histogram_demo.html

def main():
    size=10000
    rate=0.5

    xs=np.random.normal(loc=0,scale=2.5,size=int(rate*size))
    xs=np.concatenate([xs,np.random.normal(loc=10,scale=5,size=int((1-rate)*size))])

    fig,ax=plt.subplots()
    density, bins, _=ax.hist(xs,bins=50,normed=True,edgecolor='black',facecolor='yellow',
            linewidth=0.5,alpha=0.75)

    #mode
    mode_idx=np.argmax(density)
    bincenters = 0.5*(bins[1:]+bins[:-1])
    mode=bincenters[mode_idx]
    plt.plot([mode,mode],[0,np.max(density)],'-.',color='black',label='mode')

    #median
    median=np.median(xs)
    plt.plot([median,median],[0,np.max(density)],'--',color='red',label='median')
    #q1 percentile
    q1=np.percentile(xs,25)
    plt.plot([q1,q1],[0,np.max(density)],':',color='blue',label='Q1')
    #q3 percentile
    q3=np.percentile(xs,75)
    plt.plot([q3,q3],[0,np.max(density)],':',color='blue',label='Q3')
    ax.set_xlim([-10,30])
    ax.legend()
    plt.show()

if __name__ == '__main__':
    main()
