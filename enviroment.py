import os
import numpy as np
import random


class Environment:
    def __init__(self, x=1, y=2, walls=False, enviro=[]):
        self.enviro = enviro
        self.size = [x, y]
        self.setShape(walls)
        self.setDirt()

    def getSize(self):
        return self.size

    # No method needed for Walls: [walls - true] -> (2*x +2*y - 4) is the amount of walls / [wall - false] -> original perimeter 
    #TODO: Fix to add walls to outer parts of map
    def setShape(self, walls):
        if walls:
            for i in range(x):
                for j in range(y):
                    if i == 0 or i == x-1 or j == 0 or j == y-1:
                        self.enviro[i][j] = 2
                
    def setEnviro(m):
        self.enviro = m
    
    def setDirt(self):
        # sets dirt placement (1 = dirt at that location), randomized
        # self.enviro = np.floor(2*np.random.random((self.size[0],self.size[1])))
        self.enviro = np.random.randint(0, 2, size=(self.size[0],self.size[1]))

    def print_shape(self):
        print(self.enviro)
