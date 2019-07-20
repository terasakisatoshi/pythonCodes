import threading
import queue
import time
from collections import defaultdict

class JobManager(object):
    """docstring for ThreadQueue"""
    def __init__(self,nthreads,jobs):
        self.nthreads=nthreads
        self.request=queue.Queue(nthreads)
        self.result=queue.Queue(2*nthreads)
        self.jobs=jobs
        self.threads=[]
        self.insert_done=False
        self.init_threads()

    def init_threads(self):
        for i in range(self.nthreads):
            t=threading.Thread(target=self.process_job,name=str(i))
            t.setDaemon(True)
            self.threads.append(t)
        self.threads.append(threading.Thread(target=self.insert_que_to_threads))
        for t in self.threads:
            t.start()
        print('init_threads done')

    def pull(self):
        while True:
            if self.insert_done and self.result.empty():
                for i in range(self.nthreads):
                    self.threads[i].join()
                break
            que=self.result.get()
            yield(que)
        return None

    def process_job(self):
        while True:
            try:
                i=self.request.get(timeout=1)
            except queue.Empty:
                break
            self.result.put(i)

    def insert_que_to_threads(self):
        while not self.jobs.empty():
            job=self.jobs.get()
            self.request.put(job)
        self.insert_done=True
        

def main():
    
    jobs=queue.Queue()
    for i in range(30):
        jobs.put(i)
    jm=JobManager(2,jobs)
    print('start')
    get=[]
    for i in jm.pull():
        print('pull',i)
        get.append(i)
    print(sorted(get))



if __name__ == '__main__':
    main()