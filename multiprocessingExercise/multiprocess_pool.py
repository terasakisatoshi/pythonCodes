from multiprocessing import Pool,cpu_count,current_process 
import time

def slow_func(x):
    print(current_process().name,":this started at%s" % time.ctime().split()[3])
    time.sleep(1)
    return x*x

def using_pool():
    print("num of cpus ",cpu_count())
    start=time.time()
    pool=Pool()
    print("answer : %d" % sum(pool.map(slow_func,range(12))))
    print("time : %f"% (time.time()-start))

def using_single():
    start=time.time()
    pool=Pool()
    print("answer : %d" % sum(map(slow_func,range(12))))
    print("time : %f"% (time.time()-start))

def main():
    print("Start using_pool()")
    using_pool()
    print("End using_pool()")
    print("Start using_pool()")
    using_single()
    print("End using_pool()")

if __name__ == '__main__':
    main()

