import numpy as np 

def omega(power,N):
    return np.exp(2.0*np.pi*power*1j/N)

def ope1(a,b):
    return a+b

def ope2(a,b,power,N):
    return (a-b)*omega(power,N)

def FFT_2(a,b):
    return [ope1(a,b),ope2(a,b,0,2)]

def FFT(xs,N):
    if N==2:
        return FFT_2(xs[0],xs[1])
    else:
        xs_former=[]
        half_len=len(xs)//2
        for i in range(half_len):
            a,b=xs[i],xs[i+half_len]
            xs_former.append(ope1(a,b))
        ys_former=FFT(xs_former,N//2)
        
        xs_latter=[]
        for i in range(half_len):
            a,b=xs[i],xs[i+half_len]
            xs_latter.append(ope2(a,b,i,N))
        ys_latter=FFT(xs_latter,N//2)

        return ys_former+ys_latter

def calc_FFT(xs):
    N=len(xs)
    if not N & (N-1) == 0:
        raise ValueError("you can not use iff len(xs)==2**k for some k")
    outs=FFT(xs,N)
    #resort output
    ys=[None for _ in range(len(outs))]
    for i in range(len(outs)):
        bit=format(i,'0{}b'.format(int(np.log2(N))))
        ys[int(bit[::-1],2)]=outs[i]
    return ys

def main():
    N=4
    xs=[1,1,0,0]
    print(calc_FFT(xs))
    xs=[0,np.pi/4,2*np.pi/4,3*np.pi/4,np.pi,3*np.pi/4,2*np.pi/4,np.pi/4]
    print(calc_FFT(xs))

if __name__ == '__main__':
    main()