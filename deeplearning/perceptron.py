#coding utf-8

import numpy as np 
from numpy.random import *
def sigmoid(x):
    return 1.0/(1+np.exp(-x))

def step_func(x):
    if x>0:
        return 1
    else:
        return 0

class TrainningSet():
    def __init__(self,val_in,val_out):
        self.input=val_in
        self.out=val_out
    def __str__(self):
        return self.input,self.output


class SinglePerceptron():
    """
    func is activating funciton
    weight is weight vector its type is np.array
    bias is bias its type is flot
    """
    alpha=0.01
    def __init__(self,func,weight,bias):
        self.f=func
        self.w=weight
        self.b=bias
    def output(self,x):
        """x is supposed to be np.array"""
        return self.f(self.w.dot(x)+self.b)
    def sq_err(self,x,val):
        """val trainning output value"""
        return (self.output(x)-val)**2
    def _upd_w(self,xs,r):
        self.w=self.w+xs*self.alpha*(r-self.output(xs))
    def _upd_b(self,xs,r):
        self.b=self.b+self.alpha*(r-self.output(xs))
    def _update(self,val_in,val_out):
        self._upd_w(val_in,val_out)
        self._upd_b(val_in,val_out)
    def optimize(self,trainning_set):    
        for i in range(1000):
            err_sum=sum([self.sq_err(el.input,el.out) for el in trainning_set])
            print "err sum",err_sum
            for el in trainning_set:
                print "err each el",self.sq_err(el.input,el.out)
                while(self.sq_err(el.input,el.out)>0.01):
                    print "el_in",el.input
                    self._update(el.input,el.out)
                    print self.w,self.b,self.sq_err(el.input,el.out)
            if err_sum<0.01:
                return i


    def __str__(self):
        return "w=%s,b=%f"% self.w,self.b

def main():
    weight=np.array([randint(-10,10),randint(-10,10)])
    bias=randint(-10,10)
    xs=np.array([1,1])
    per=SinglePerceptron(step_func,weight,bias)
    trains=[]

    t1=TrainningSet(np.array([0,0]),0)
    t2=TrainningSet(np.array([1,0]),1)
    t3=TrainningSet(np.array([0,1]),0)
    t4=TrainningSet(np.array([1,1]),0)
    trains=[t1,t2,t3,t4]
    count=per.optimize(trains)
    print "finish"
    print count
    print "result w, b"
    print per.w,per.b
    print "check"
    print [per.output(t.input)-t.out for t in trains]

if __name__ == '__main__':
    main()