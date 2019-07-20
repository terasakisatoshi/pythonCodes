import subprocess
import time 

def call_subprocess(cmd):
    proc=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)

    out,err=proc.communicate()
    print(out.decode('utf-8'))

def run_sleep(period):

    proc=subprocess.Popen(['sleep {}'.format(str(period))],shell=True)
    return proc

def main():
    call_subprocess(['echo','hello world'])
    start=time.time()
    procs=[]
    for _ in range(30):
        proc=run_sleep(5)
        procs.append(proc)
    end=time.time()

    print('end-start=',end-start)

    start=time.time()
    for proc in procs:
        proc.communicate()
    end=time.time()

    print('end-start= %.3f seconds'%(end-start))

if __name__ == '__main__':
    main()

