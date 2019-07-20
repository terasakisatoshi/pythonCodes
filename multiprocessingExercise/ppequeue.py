from concurrent import futures
import queue
import threading
import time

class JobManager(object):
    def __init__(self,jobs):
        self.jobs=jobs
        self.result=queue.Queue()
        self.threads=[]
        self.process_task_done=False
        self.init_threads()

    def init_threads(self):
        t=threading.Thread(target=self.process_jobs)
        self.threads.append(t)
        for t in self.threads:
            t.start()

    def process_jobs(self):
        def pull_job():
            while not self.jobs.empty():
                job=self.jobs.get()
                yield job
        executor=futures.ProcessPoolExecutor()
        fs=[executor.submit(do_somethind,job) for job in pull_job()]
        for f in futures.as_completed(fs):
            self.result.put(f.result())
        self.process_task_done=True

    def pull(self):
        while True:
            if self.process_task_done and self.result.empty():
                break
            res=self.result.get()
            yield res

def do_somethind(i):
    print('do_somethind',i)
    time.sleep(2)
    return i

def main():
    que=queue.Queue()
    for i in range(30):
        que.put(i)
    job_manager=JobManager(que)
    get=[]
    for res in job_manager.pull():
        print('get',res)
        get.append(res)
    print(sorted(get))

if __name__ == '__main__':
    main()