import os
import numpy
import random


class environment:
    def __init__(self, x=1, y=2, walls=0):
        self.enviro = []
        self.setSize(x,y)
        self.setShape(walls)
        self.setDirt()

        
    def setSize(self,x=1, y=2):
        # x is rows y is column  
        self.enviro = [ [0] * y for _ in range(x)]

    def setShape(self, walls=0):  
        pass 
    
    def setDirt(self):
        for rowIndex, row in enumerate(self.enviro):
            for colIndex, col in enumerate(row):
                rand = random.randint(0,1)
                # places dirt if rand = 1, clean if 0
                if rand == 1:
                    self.enviro[rowIndex][colIndex] = rand

    def print_shape(self):
        print(self.enviro)
        


env = environment()

env.print_shape()
