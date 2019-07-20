import numpy as np
import matplotlib.pyplot as plt
import time

def analyze_server():
    start=[]
    send=[]
    f=open('ser_res.txt','r')
    lines=f.readlines()
    for lin in lines:
        word=lin.split()
        if "start" in lin:
            start.append(float(word[1]))
        if "send" in lin:
            send.append(float(word[1]))

    return start,send


def analyze_client():
    start=[]
    recv=[]
    f=open('res.txt','r')
    lines=f.readlines()
    for lin in lines:
        word=lin.split()
        if "start" in lin:
            start.append(float(word[1]))
        if "recv" in lin:
            recv.append(float(word[1]))
    return start,recv

def main():
    send,recv=analyze_client()
    get,ret=analyze_server()
    plt.plot(send,np.zeros(len(send)),"o")
    plt.plot(recv,np.zeros(len(recv)),"o")
    plt.plot(get,np.ones(len(get)),"o")
    plt.plot(ret,np.ones(len(ret)),"o")

    print np.average([((recv[i]-send[i])-(ret[i]-get[i]))/2 for i in range(len(send))])
    plt.show()
if __name__ == '__main__':
    main()
