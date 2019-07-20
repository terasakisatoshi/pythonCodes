from functools import wraps
import time 

def get_elappsed_time(function):
    @wraps(function)
    def measure_target(*args,**kwargs):
        start=time.time()
        ret=function(*args,**kwargs)
        end=time.time()
        return function.__name__,ret,end-start
    return measure_target

@get_elappsed_time
def zigzag_counter():
    counter=0
    for i in range(1000):
        for j in range(1000):
            counter=i*j*(-1)**j
    return counter

def main():
    print(zigzag_counter())


    
if __name__ == '__main__':
    main()