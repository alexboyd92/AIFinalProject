import random as r
from enviroment import Environment

class SimpleReflexAgent(Environment):

    def __init__(self, Environment, cycles=1000):

        # Gets the size of the environment
        self.size = Environment.getSize()
        #print(self.size)
        
        # Gets the dirt placement map
        self.dirtEnv = Environment.enviro
        #print(self.dirtEnv)
        
        # Performance Score
        self.score = 0

        # Number of cycles left on vacuum
        self.cyclesLeft = cycles
        
        # Randomized starting vacuum location based on size 
        self.vacuumLocation = [r.randint(0,self.size[0]-1), r.randint(0,self.size[1]-1)]
        print(self.vacuumLocation)

    def moveAgent(self, direction):
        
        # moves the agent up one position on the map
        if direction == 0:
            if self.vacuumLocation[0] > 0:
                self.vacuumLocation[0] -= 1
            else:
                self.moveAgent(r.randint(0,3))
        
        # moves the agent to the right one position
        elif direction == 1:
            if self.vacuumLocation[1] < self.size[1]-1:
                self.vacuumLocation[1] += 1
            else:
                self.moveAgent(r.randint(0,3))
        
        # moves the agent down one position
        elif direction == 2:
            if self.vacuumLocation[0] < self.size[0]-1:
                self.vacuumLocation[0] += 1
            else:
                self.moveAgent(r.randint(0,3))
        
        # moves the agent left one position
        elif direction == 3:
            if self.vacuumLocation[1] > 0:
                self.vacuumLocation[1] -= 1
            else:
                self.moveAgent(r.randint(0,3))
        

    def suck(self):
        self.dirtEnv[self.vacuumLocation[0]][self.vacuumLocation[1]] = 0
        self.score += 1

    def agentAction(self):
        if self.dirtEnv[self.vacuumLocation[0]][self.vacuumLocation[1]] == 1:
            self.suck()
        else:
            self.moveAgent(1)


    def runVacuum(self):
        while(self.cyclesLeft != 0):

            self.agentAction()
            print(self.dirtEnv)
            self.cyclesLeft -= 1
        
        print(self.score)









