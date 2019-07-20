from concurrent import futures
#template 
def func(arg):
    #do something
    return arg**arg

def main():
    executor=futures.ProcessPoolExecutor(max_workers=4)
    args=range(10)
    fs=[executor.submit(func,arg) for arg in args]
    for f in futures.as_completed(fs):
        print(f.result())

if __name__ == '__main__':
    main()