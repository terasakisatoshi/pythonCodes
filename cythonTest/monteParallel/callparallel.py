import monte
import time

NUM = 1000000000

def main():
    start=time.time()
    pi=monte.monte(NUM)
    end=time.time()
    print("pi, {}, elapsed={}".format(pi, end-start))
    

if __name__ == '__main__':
    main()