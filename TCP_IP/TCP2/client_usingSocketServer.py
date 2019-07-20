#run usingSocketServer.py in advance

import socket
import sys
import time

HOST,PORT="localhost",9999
data="".join(sys.argv[1:])
data="hello"

class TimerInfo():
    def __init__(self,start,recv):
        self.start=start
        self.recv=recv

time_info=[]
init_time=0
counter=0
def send_messenger():
    global counter,init_time
    if counter==0:
        init_time=time.time()
    counter+=1
    #create a socket (SOCK_STREAM means a TCP socket)
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #connet to server and send data
    sock.connect((HOST,PORT))
    start_time=time.time()-init_time
    sock.send(data+str(counter)+"\n")
    #receive data from the server and shut down
    received=sock.recv(1024)
    recv_time=time.time()-init_time
    sock.close()
    print("sent:    %s"% data+str(counter))
    print("received     %s"% received)
    time_info.append(TimerInfo(start_time,recv_time))
    time.sleep(0.5)


def main():
    for i in range(10):
        send_messenger()

    f=open("res.txt",'w')
    for el in time_info:
        f.write("start"+" "+str(el.start)+"\n")
        f.write("recv"+" "+str(el.recv)+"\n")



if __name__ == '__main__':
    main()
