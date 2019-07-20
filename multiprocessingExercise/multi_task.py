import multiprocessing as mp 
import os
from os.path import join,basename,dirname
from functools import partial

def say_hello_and_mkfolder(args):
    job=args[1]
    for i in job:
        print("Hello I'm ",str(i))
        target=join(args[0],"folder-"+str(i))
        if not os.path.exists(target):
            os.mkdir(target)

def create_folders(jobs,nproc):
    test_folder="TestFolder"
    if not os.path.exists(test_folder):
        os.mkdir(test_folder)

    pool=mp.Pool(nproc)    
    args=[(test_folder,job) for job in jobs]
    callback=pool.map(say_hello_and_mkfolder,args)

def task_distributer(task,nproc):
    """task:list or tuple"""
    task_size=len(task)
    div_size=task_size//nproc
    divided=[]
    for i in range(0,task_size,div_size):
        divided.append(task[i:min(i+div_size ,task_size)])
    return divided

def main():
    task=tuple(i for i in range(50))
    nproc=8
    task_divided=task_distributer(task,8)
    create_folders(task_divided,nproc)
    
if __name__ == '__main__':
    main()