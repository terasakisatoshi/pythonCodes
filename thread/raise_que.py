import queue

q=queue.Queue()

for i in range(5):
    q.put(i)

while True:
    try:
        val=q.get(False)
    except queue.Empty:
        break
    print(val)
    q.task_done()