import numpy as np

def step_func(x):
    if x>0:
        return 1
    else :
        return -1
        
def sigmoid_func(x):
    return 1/(1+np.exp(-x))
def main():
    print(np.vectorize(step_func)(np.array([-1,0,1])))
    print(sigmoid_func(np.array([-1,0,1])))
if __name__=='__main__':
    main()