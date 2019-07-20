# -*- coding:utf-8 -*-
#!/usr/bin/python
#this python is written 2.7.11
import numpy
import socket
import cv2
import time
#define IP port for each env
HOST='127.0.0.1'
PORT=9876
timer_info=[]
init_time=0.0

def get_image():
    global timer_info
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((HOST,PORT))
    sock.send('HELLO\n')
    buf=''
    recvlen=100
    recv_start=time.time()-init_time
    while recvlen>0:
        receivedstr=sock.recv(1024*8)
        recvlen=len(receivedstr)
        buf+=receivedstr
    sock.close()
    recv_end=time.time()-init_time
    narray=numpy.fromstring(buf,dtype='uint8')
    decode_end=time.time()-init_time
    timer_info.append(['recv_start',recv_start])
    timer_info.append(['recv_end',recv_end])
    #timer_info.append(['decode_end',decode_end])
    return cv2.imdecode(narray,1)

def collect_image_info():
    global timer_info
    global init_time
    counter=0
    if counter==0:
        init_time=time.time()
    while counter<20:
        counter+=1
        start=time.time()-init_time
        timer_info.append(['getstart',start])
        img=get_image()
        get_end=time.time()-init_time
        timer_info.append(['getend',get_end])
        cv2.imshow('Capture',img)
        show_end=time.time()-init_time
        timer_info.append(['shw_end',show_end])
        if cv2.waitKey(100) &0xFF==ord('q'):
            break
    return timer_info

def main():
    info=collect_image_info()
    f=open("res.txt",'w')
    for i in info:
        f.write(str(i[0])+" "+str(i[1])+"\n")
    f.close()

if __name__ == '__main__':
    main()