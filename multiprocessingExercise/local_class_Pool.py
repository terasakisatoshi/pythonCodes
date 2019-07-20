from multiprocessing import Process,Pool,Pipe

class MyPool:
    proc_num=8
    def __init__(self,proc_num):
        self.proc_num=proc_num

    def my_map(self,func,args):
        def pipefunc(conn,arg):
            conn.send(func(args))
            conn.close()
        ret=[]
        k=0
        while(k<len(args)):
            plist=[]
            clist=[]
            end=min(k+self.proc_num,len(args))
            for arg in args[k:end]:
                pconn,conn=Pipe()
                plist.append(Process(target=pipefunc,args=(conn,arg,)))
                clist.append(pconn)
            for p in plist:
                p.start()
            for conn in clist:
                ret.append(conn.recv())
            for p in plist:
                p.join()
            k+=self.proc_num
        return ret

class Test():
    def func(self,x):
        return x*x

    def multi_process(self):
        p=MyPool(2)
        print(p.my_map(self.func,range(10)))

def main():
    test=Test()
    test.multi_process()

if __name__ == '__main__':
    main()
