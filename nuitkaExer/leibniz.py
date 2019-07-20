import time 

def leibniz(n):
    s=0
    for i in range(n):
        a=(-1)**i * 1/(2*i+1)
        s+=a
    return 4*s

def main():
    start = time.time()
    print(leibniz(100000000))
    end= time.time()
    print("elapsed", end-start)

if __name__ == '__main__':
    main()