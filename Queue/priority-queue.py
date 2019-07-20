import Queue

class Job(object):
    def __init__(self,priority,description):
        self.priority=priority
        self.description=description
        print("New Job",description)
        return None
    def __cmp__(self,other):
        return cmp(self.priority,other.priority)

def main():

    q=Queue.PriorityQueue()

    q.put(Job(3,"Mid-level-job"))
    q.put(Job(10,"Low-level-job"))
    q.put(Job(1,"High-level-job"))

    while not q.empty():
        next_job=q.get()
        print("processing job:",next_job.description)

if __name__ == '__main__':
    main()