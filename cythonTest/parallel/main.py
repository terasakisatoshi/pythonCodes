import multithreads as mt 
import time
print("Start")
start=time.time()
y=mt.test_serial()
end=time.time()
print(y)
print('elapsed=',end-start)

print("Start")
start=time.time()
y=mt.test_parallel()
end=time.time()
print(y)
print('elapsed=',end-start)