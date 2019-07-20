import numpy as np 
from sklearn.feature_extraction import image
import time
from concurrent import futures
import multiprocessing as mp 
def arg_wrapper(args):
    return args[0](*args[1:])

def extract_patches_single():
    row,col=500,500
    one_image=np.arange(row*col).reshape(row,col)
    image.extract_patches_2d(one_image,(50,50))

def extract_patches_multi_process():
    row,col=500,500
    one_image=np.arange(row*col).reshape(row,col)
    nproc=4
    p=mp.Pool(nproc)
    func_args=[(image.extract_patches_2d,one_image,(50,50)) for _ in range(nproc)]

def extract_patches_multi_thread():
    row,col=500,500
    one_image=np.arange(row*col).reshape(row,col)
    nproc=5
    executor = futures.ThreadPoolExecutor(max_workers=2)
    fs=[executor.submit(image.extract_patches_2d,one_image[:i+row//nproc],(50,50)) for i in range(nproc)]
    for f in futures.as_completed(fs):
        continue

def measure_time(func):
    start=time.time()
    func()
    end=time.time()
    print("elapsed=",end-start)

def main():
    measure_time(extract_patches_single)
    measure_time(extract_patches_multi_process)
    measure_time(extract_patches_multi_thread)
if __name__ == '__main__':
    main()