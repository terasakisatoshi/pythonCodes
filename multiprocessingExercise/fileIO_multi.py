import sys
import time
from multiprocessing import Process

def read_file_via_heavy_task(idx,num_process,lines):
    for line in lines[idx::num_process]:
        print("process num= ",idx,"do some...",line.strip())
        time.sleep(1.0)

def main():
    num_process=4
    with open("test.txt",'r') as f:
        lines=f.readlines()

    process_list=[]
    for idx in range(num_process):
        p=Process(target=read_file_via_heavy_task,args=(idx,num_process,lines))
        process_list.append(p)

    for p in process_list:
        p.start()
    for p in process_list:
        p.join()

if __name__ == '__main__':
    main()