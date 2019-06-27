import numpy as np
from scipy.optimize import minimize

class ann:
    '''This class is defined to create a neural network for interpolation'''
    pass

    def __init__(self, n, f, data = None):

        self.size = n
        self.func = f
        if not data == None:
            self.data = data
        else: 
            self.data = np.random.rand(n, 3)

    def result(self, x):
        y = []

        for ii in range(len(x)):
            y.append(self.feed_forward(x[ii]))
        return y

    def feed_forward(self, x):

        neuron_sum = 0
        for ii in range(self.size):
            neuron_sum += self.func((x-self.data[ii][0])/self.data[ii][1])*self.data[ii][2]
        
        return neuron_sum

    def ann_train(self, x, f_xl, yl):

        self.data = np.reshape(x, (int(len(x)/3), 3))
        min_sum = 0
        for ii in range(len(f_xl)):
            min_sum += (self.feed_forward(f_xl[ii]) - yl[ii])**2

        return min_sum

    def minimizer(self, xl, yl): 
        initial = [self.data[ii][jj] for ii in range(len(self.data)) for jj in range(3)]
        fun = lambda x: self.ann_train(x, xl, yl)
        min_sum = minimize(fun, initial)
        self.data = np.reshape(min_sum.x, (int(len(min_sum.x)/3), 3))


class ann_other:
    '''This class is defined to create a neural network for interpolation of a given function. Both the derivative and anti-derivative can be found using this network'''
    pass

    def __init__(self, n, f, df, F, data = None):

        self.size = n
        self.func = f
        self.df = df
        self.int = F
        if not data == None:
            self.data = data
        else: 
            self.data = np.random.rand(n, 7)

    def result(self, x):
        y = []
        dy = []
        inty = []

        for ii in range(len(x)):
            y.append(self.feed_forward_func(x[ii]))
            dy.append(self.feed_forward_deriv(x[ii]))
            inty.append(self.feed_forward_int(x[ii]))
        return y, dy, inty

    def feed_forward_func(self, x):

        neuron_sum = 0
        for ii in range(self.size):
            neuron_sum += self.func((x-self.data[ii][0])/self.data[ii][1])*self.data[ii][2] 
        
        return neuron_sum
    
    def feed_forward_deriv(self, x):

        neuron_sum = 0
        for ii in range(self.size):
            neuron_sum += self.df((x-self.data[ii][3])/self.data[ii][4])*self.data[ii][2] 
        
        return neuron_sum

    def feed_forward_int(self, x):
         neuron_sum = 0
         for ii in range(self.size):
             neuron_sum += self.int((x-self.data[ii][5])/self.data[ii][6])*self.data[ii][2]
             
         return neuron_sum
     
    def ann_train_func(self, x, f_xl, yl):

        self.data = np.reshape(x, (int(len(x)/7), 7))
        min_sum = 0
        for ii in range(len(f_xl)):
            min_sum += (self.feed_forward_func(f_xl[ii]) - yl[ii])**2
            
        return min_sum
    

    def ann_train_deriv(self, x, f_xl, yl):

        self.data = np.reshape(x, (int(len(x)/7), 7))
        min_sum = 0
        for ii in range(len(f_xl)):
            min_sum += (self.feed_forward_deriv(f_xl[ii]) - yl[ii])**2

        return min_sum


    def ann_train_int(self, x, f_xl, yl):
        self.data = np.reshape(x, (int(len(x)/7), 7))
        min_sum = 0
        for ii in range(len(f_xl)):
            min_sum += (self.feed_forward_int(f_xl[ii]) - yl[ii])**2
        return min_sum


    def minimizer_other(self, xl, yl, dyl, Fyl): 
    
        initial = [self.data[ii][jj] for ii in range(len(self.data)) for jj in range(7)]
        fun = lambda x: self.ann_train_func(x, xl, yl) + self.ann_train_deriv(x, xl, dyl) + self.ann_train_int(x, xl, Fyl)
        min_sum = minimize(fun, initial)
        self.data = np.reshape(min_sum.x, (int(len(min_sum.x)/7), 7))

