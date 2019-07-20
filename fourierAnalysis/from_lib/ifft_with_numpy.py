import numpy as np 
from scipy import fftpack 
from matplotlib import pyplot as plt 

#constant variables
num_samples=1000
plot_interval=0.01
xs=np.arange(0,num_samples*plot_interval,plot_interval)
kill_frq=4.5

def plot_original(func):
    fig,ax=plt.subplots(figsize=(8,3))
    ax.plot(xs,func(xs))
    
def apply_fft(func,plotxmax=10,restricted_func=None,pass_filter='low'):
    ys=func(xs)
    fourier_value=np.fft.fft(ys)
    frq=np.fft.fftfreq(num_samples,d=plot_interval)
    amplitude_spectrum=np.abs(fourier_value)
    fig=plt.figure(figsize=(8,15))
    
    ax1=fig.add_subplot(511)
    ax1.set_title('original')
    ax1.plot(xs,func(xs))
    
    ax2=fig.add_subplot(512)
    ax2.set_title('amplitude_spectrum')
    ax2.set_xlim([0,plotxmax])
    ax2.plot(frq,amplitude_spectrum,'-')

    inv_fft=np.fft.ifft(fourier_value)
    ax3=fig.add_subplot(513)
    ax3.set_title('inverse fft')
    ax3.plot(xs,inv_fft.real)
    
    #restrict frequency
    kill_idx=np.argmin(np.abs(frq-kill_frq))
    if pass_filter=='low':
        fourier_value[kill_idx:-kill_idx]=0
    elif pass_filter=='high':
        fourier_value[:kill_idx]=0
        fourier_value[-kill_idx:]=0
    else:
        raise Exception("pass_filter must be 'low' or 'high'")
    amplitude_spectrum=np.abs(fourier_value)
    ax4=fig.add_subplot(514)
    ax4.set_title('restricted (< {} ) amplitude_spectrum'.format(kill_frq))
    ax4.set_xlim([0,plotxmax])
    ax4.plot(frq,amplitude_spectrum,'-')

    inv_fft=np.fft.ifft(fourier_value)
    ax5=fig.add_subplot(515)
    ax5.set_title('inverse fft of restricted freq')
    ax5.plot(xs,inv_fft.real,'g')
    
    if not restricted_func == None:
        ax5.plot(xs,restricted_func(xs),'r')
    plt.show()

def main():
    fs=[1,2,3,4,5,6,7,8,9]
    pass_filter='high'
    if pass_filter=='low':
        rest=list(filter(lambda f:f<kill_frq, fs))
    elif pass_filter=='high':
        rest=list(filter(lambda f:f>kill_frq, fs))
    func=      lambda x:sum([np.cos(2*np.pi*f*x) for f in fs])
    restricted=lambda x:sum([np.cos(2*np.pi*f*x) for f in rest])
    apply_fft(func,restricted_func=restricted,pass_filter=pass_filter)
if __name__ == '__main__':
    main()