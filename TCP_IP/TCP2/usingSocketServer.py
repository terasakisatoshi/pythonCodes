#python 2.7.11
import SocketServer
import time
import sys
handle_counter=0
init_time=0
timer_info=[]

class TimerInfo():
    def __init__(self,start,send):
        self.start=start
        self.send=send

class TCPHandler(SocketServer.BaseRequestHandler):
    """It is instantiated once per connection to the server,
    and must override the handle() method 
    to imlement communication to the client."""
    def handle(self):
        global handle_counter
        global init_time
        if handle_counter==0:
            init_time=time.time()
        handle_counter+=1
        #self.request is the TCP socket connected to the client
        start_time=time.time()-init_time
        self.data=self.request.recv(1024).strip()
        print("%s client address :"% self.client_address[0])
        print ("data=",self.data)
        time.sleep(1)
        #just send back the same data, but upper-cased
        send_time=time.time()-init_time
        self.request.send(self.data.upper())
        timer_info.append(TimerInfo(start_time,send_time))

#HOST PORT
HOST,PORT="localhost",9999

def main():
    #Create the server,binding to HOST on port PORT
    server =SocketServer.TCPServer((HOST,PORT),TCPHandler)
    #Active the server : this will keep running until you
    #interrupt the program with Ctrl-C
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print ("cnt",handle_counter)

    f=open("ser_res.txt",'w')
    for el in timer_info:
        f.write("start"+" "+str(el.start)+"\n")
        f.write("send"+" "+str(el.send)+"\n")

    server.shutdown()
    sys.exit()

if __name__ == '__main__':
    main()


