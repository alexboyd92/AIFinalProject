import os
import numpy as np
import random


class environment:
    def __init__(self, x=1, y=2, walls=0):
        self.enviro = []
        self.x = 0
        self.y = 0
        self._setSize(x,y)
        self._setShape(walls)
        self._setDirt()

        
    def _setSize(self,x=1, y=2):
        self.x = x
        self.y = y

    def _setShape(self, walls=0):  
        pass 
    
    def _setDirt(self):
        # sets dirt placement (1 = dirt at that location), randomized
        self.enviro = np.floor(2*np.random.random((self.x,self.y)))

    def print_shape(self):
        print(self.enviro)
        


env = environment()

env.print_shape()
