#NNetwork
#Author S.Terasaki
#Data 20.7.2016 
import numpy as np

#const
h=0.000001
epsilon=0.001

def sigmoid(x):
    return 1.0/(1+np.exp(-x))
    
#usage for ndarray of numpy :print(np.vectorize(step_func)(np.array([-1,0,1])))
def step_func(x):
    if x>0:
        return 1
    else:
        return 0

def identity_func(x):
    return x

class Layer():
    """
    func is activating funciton
    weight is weight vector its type is supposed to be np.array
    bias is bias its type is supposed to benp.array
    """
    alpha=0.01
    def __init__(self,params):
        w,b,func=params
        self.f=func
        self.w=w
        self.b=b
    
    def set_unit(self,u):
        self.u=u      
    
    def set_unit_from_previous_layer(self,u):
        self.u=self.w.dot(u)+self.b  
    
    def pass_next_layer(self):
        #activate unit
        return self.f(self.u)    
    def __str__(self):
        return "w=\n%s\nb=\n%s\nu=\n%s\nf(u)=\n%s\n"%(self.w,self.b,self.u,self.f(self.u))

class InitializeParam():
    def prepare_input_param(self):
        #3 by 3 identity matrix
        w=np.identity(3,'float64')
        #3 by 1 zero vector  
        b=np.zeros([3,1]) 
        return w,b,identity_func 

    def prepare_mediant_param(self):
        w=np.array(([0,-1,1],
                    [1,0,1],
                    [0,0,1]),'float64')
        #set b and x as column vector
        b=np.array([1,
                    1,
                    1]).reshape((-1,1))
        return w,b,sigmoid
            
    def prepare_output_param(self):
        w=np.array(([0,-1,1],
                    [1,0,1],
                    [0,0,1]),dtype='float64')
        #set b and x as column vector
        b=np.array([1,
                    1,
                    1]).reshape((-1,1))
        return w,b,sigmoid

    def prepare_mediant_param_random(self):    
        #make 3 by 3 matrix
        w=np.random.rand(3,3)
        #make column vector
        b=np.random.rand(3,1)
        return w,b,sigmoid

    def prepare_random_param(self):
        #make 3 by 3 matrix
        w=np.random.rand(3,3)
        #make column vector
        b=np.random.rand(3,1)
        return w,b,sigmoid

class NNetwork():        
    def __init__(self,layers):
        self.layers=layers    
    def upd_layer(self,index,layer):
        self.layers[index]=layer
        
    def get_output(self,x):
        #we should modify data structure. e.g. DataFrame (pandas)
        #input_layer
        self.layers[0].set_unit(x)
        for i in range(len(self.layers)-1):
            self.layers[i+1].set_unit_from_previous_layer(self.layers[i].pass_next_layer())
        return self.layers[len(self.layers)-1].pass_next_layer()
                        
def delta_net(network,l,i,j):
    layers=network.layers
    layers[l].w[i][j]=+h
    return NNetwork(layers)

def square_error(ys,ts):
    return np.sum((ys-ts)**2)/2.0                    

def partial_derivative(network,l,i,j,xs,ts):
    ys=network.get_output(xs)
    delta_ys=delta_net(network,l,i,j).get_output(xs)
    network.layers[l].w[i][j]=-h #reset
    return (square_error(delta_ys,ts)-square_error(ys,ts))/h

                                    
def initialize_network(initial_param):
    input_layer=Layer(initial_param.prepare_input_param())
    mediant_layer=Layer(initial_param.prepare_random_param())
    output_layer=Layer(initial_param.prepare_random_param())
    layers=[input_layer,mediant_layer,output_layer]
    return NNetwork(layers)    

def testdata():
    input_value=(np.array([3.5,
                           -0.2,
                           -9]).reshape((-1,1)))
    teaching_set=(np.array([0,
                            0,
                            1]).reshape((-1,1)))
    return input_value,teaching_set
def randomdata():
    input_value=np.random.rand(3,1)
    teaching_set=np.random.rand(3,1)
    return input_value,teaching_set

def main():
    initial_param=InitializeParam()
    network=initialize_network(initial_param)
    #create 3 by 1 vector
    input_value,teaching_set=testdata()
    print("teaching_set=\n%s"%teaching_set)
    #training loop!
    for loop in range(1000):
        for l,layer in enumerate(network.layers):
            for i in range(layer.w.shape[0]):
                for j in range(layer.w.shape[1]):
                    delta=epsilon*partial_derivative(network,l,i,j,input_value,teaching_set)
                    network.layers[l].w[i][j]-=delta
                    if square_error(network.get_output(input_value),teaching_set)<0.01:
                        break
    print("sqerror=\n%s"%square_error(network.get_output(input_value),teaching_set))
    #print([l.w for l in network.layers ])
    print("optimized output\n%s"%network.get_output(input_value))
    hoge=network.get_output(input_value)-teaching_set
    print("diff opt-teach\n%s"%hoge)
                                                    
if __name__=='__main__':
    main()