import pandas as pd 
import matplotlib as mpl 
from matplotlib import pyplot as plt 

alphabet='abcdefghijklmnopqrstuvwxyz'

def main():
    s=pd.Series([i for i in range(10)],index=[alphabet[i] for i in range(10)])
    print(s['a'],s.a)
    mpl.style.use('ggplot')
    font={'family':'IPAexMincho'}
    mpl.rc('font',**font)

    fig,ax=plt.subplots(1,2,figsize=(6,3))

    s.plot(ax=ax[0],kind='line',title='line')    
    s.plot(ax=ax[1],kind='box',title='box')
    fig.tight_layout()
    plt.show()
if __name__ == '__main__':
    main()