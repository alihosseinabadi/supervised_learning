import numpy as np  


class linear : 
    def __init__(self, method : str , iter : int  = 100 , lr : float = 000.1, patch_size: int  = 32 , seeds : int = 100):
        self.method = method 
        self.iter = iter 
        self.lr = lr 
        self.w = None
        self.seeds = seeds
        self.patch_size = patch_size

    def linear(self,x,y):
        k = x.shape[0]
        xb= np.c_[np.ones(k,1),x]
        self.w = linalg.pinv(xb @ xb.T) @ y @ xb.T
    def gredient_Decent(self,x,y):
        self.w = np.zeros(np.shape[1])
        k = np.shape[0]
        xb = np.c_[np.zeros(k,1),x]

        for i in  range(iter):
            y_pred = self.w * xb
            # because its loss function of y - ypred power 2 ww rake for the gredient deent of it n the so y - wb 
            grad =  (2/n) * ((y_pred - y) @ xb.T)
            self.w -= grad * self.lr
    def gredient_decent_stch(self,x,y):
        self.w = np.zeros(shape[1])
        k = np.shape[0]
        wb = np.c_(np.ones(k,1),x)
        n = xb.shape[0]

        for epoch in self.batch_sizes:
            i = np.random.premetation(n)
            y_shuffle = y[i]
            x_shiffle = x[i]

        for i in  range(0,n,)

