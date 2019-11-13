import os
import numpy as np
import random


class Environment:
    def __init__(self, x=1, y=2, walls=False):
        self.enviro = []
        self.size = [x, y]
        self.setShape(walls)
        self.setDirt()

    def getSize(self):
        return self.size

    #TODO: Fix to add walls to outer parts of map
    def setShape(self, walls):
        pass
        if walls:
            # if area is or greater than 16 units (x=4,y=4) than walls can be set up
            # 2 = wall at location
            if self.size[0] * self.size[1] >= 16:
                self.enviro[:,0] = 2
                self.enviro[:,-1] = 2
                self.enviro[0] = 2
                self.enviro[-1] = 2
                
    
    def setDirt(self):
        # sets dirt placement (1 = dirt at that location), randomized
        # self.enviro = np.floor(2*np.random.random((self.size[0],self.size[1])))
        self.enviro = np.random.randint(0, 2, size=(self.size[0],self.size[1]))

    def print_shape(self):
        print(self.enviro)
