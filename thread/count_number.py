import threading
 
class MyThread(threading.Thread):
    def run(self) :
        i = 0
        for n in range(1000000):
            i += n
            if 0 == (n % 10000):    #10000おきに表示
                print('[mid] %s : %d' % (self.getName(), n))
        print('[end] %s : %d' % (self.getName(), i))
 
def main():
    thd1 = MyThread()
 
    thd1.start()
 
    print('in join')
    thd1.join()     #スレッド完了まで待機
    print('[finish]')
 
if __name__ == '__main__':
    main()