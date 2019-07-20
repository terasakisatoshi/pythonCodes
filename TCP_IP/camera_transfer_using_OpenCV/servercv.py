# -*- coding:utf-8 -*-
#!/usr/bin/python

import SocketServer  
import cv2
import numpy  
import socket  
import sys
import time

handle_counter=0
init_time=0
info=[]
class TimerInfo():
    def __init__(self,start,cap_end,proc_end):
        self.start=start
        self.cap_end=cap_end
        self.proc_end=proc_end

class TCPHandler(SocketServer.BaseRequestHandler):  

    #リクエストを受け取るたびに呼ばれる関数
    capture=''  
    def handle(self):
        global handle_counter
        global init_time
        if handle_counter==0:
            init_time=time.time()
        handle_counter+=1
        #HELLOを受け取ったらJPEG圧縮したカメラ画像を文字列にして送信
        self.data = self.request.recv(128).strip()
        cap_start=time.time()-init_time
        ret, frame=capture.read()
        cap_end=time.time()-init_time
        jpegstring=cv2.cv.EncodeImage('.jpeg',cv2.cv.fromarray(frame)).tostring()  
        #print jpegstring
        proc_end=time.time()-init_time
        self.request.send(jpegstring)
        info.append(TimerInfo(cap_start,cap_end,proc_end))

  
#環境に応じて変更
HOST = '127.0.0.1'
PORT = 9876

#カメラの設定
capture=cv2.VideoCapture(0)
capture.set(3,1000)
capture.set(4,1000)
if not capture:  
    print "Could not open camera"  
    sys.exit()

SocketServer.TCPServer.allow_reuse_address = True
server = SocketServer.TCPServer((HOST, PORT), TCPHandler)  
server.capture=capture  
#^Cを押したときにソケットを閉じる
try:
    server.serve_forever()  
except KeyboardInterrupt:
    print "cnt",handle_counter
f=open("ser_res.txt",'w')
for el in info:
    f.write("start "+str(el.start)+"\n")
    f.write("capend "+str(el.cap_end)+"\n")
    f.write("proend "+str(el.proc_end)+"\n")
f.close()

server.shutdown()
sys.exit()