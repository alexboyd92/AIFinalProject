import os
import numpy as np
import random


MAP2 = np.array([
    [0,2,0,2,2,2,2,2,2,0],
    [0,0,0,0,0,0,0,0,2,0],
    [0,1,1,0,2,2,2,0,2,0],
    [2,2,2,2,0,1,0,1,0,0]
])
MAP1 = np.array([
    [0,0,0,2],
    [0,0,0,0],
    [0,1,1,0],
    [2,2,2,2]
])
MAP3 = np.array([
    [0,2,2,1],
    [0,2,0,1],
    [0,1,0,2],
    [2,1,1,2],
    [2,2,0,0]
])

class Environment:
    def __init__(self, x=1, y=2, enviro=[]):
        self.enviro = enviro
        self.size = [x, y]
        self.setDirt()

    def getSize(self):
        return self.size
                
    def setEnviro(self, m):
        self.enviro = m
        self.size[0] = len(m)
        self.size[1] = len(m[0])
    
    def setDirt(self):
        # sets dirt placement (1 = dirt at that location), randomized
        self.enviro = np.random.randint(0, 2, size=(self.size[0],self.size[1]))

    def print_shape(self):
        print(self.enviro)

    def pickStartingLocation(self, enviro):
        xStart = random.randint(0,self.size[0])
        yStart = random.randint(0,self.size[1])
    
