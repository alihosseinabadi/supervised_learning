import numpy as np 
class linear:
    #linear regressio model start to predict the slope w and true bais 
    def __init__(self,method : str , lr :float , w : float ,b : float, learning_rate = 0.001,iteration= 100, seed= 21,batch_size = 32 ):
        self.lr = lr
        self.w = None
        self.b = b 
        self.iteration= iteration
        self.seed = seed
        self.method = method 
        self.batch_size = batch_size
    def findw(self,x,y):
        #we take the row shape fo the our x data 
        b = np.shape(x[0])
        # make intercept and our data for each line toghater 
        xb = np.c_[np.ones(b,1),x]
        # in here we need to impelment the (y - ypred)**2 = (y - xw+b)2   == deravetive of it based on w because we need to find the w  == 2x@t(y -xw) == (y@ x.T - x@ x.T )==
        ## w = (x @x.T)^-1 @ (y @ x.T)
        self.w = np.linalg.pinv(xb @ xb.T) @ xb @ y

    def regression(self,x,y,b):
        xb = np._c[np.ones(self.b,1),x]
        self.w = np.zeros(xb.shape[1],dtype=float)
        n = xb.shape[0]
        # so first we need to declrate the formula y = Xw + b
        y = (x*self.b) + w
    