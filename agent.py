import random as r
from enviroment import Environment
import numpy as np
import nodes



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
        self.vacuumStartLocation = [r.randint(0,self.size[0]-1), r.randint(0,self.size[1]-1)]
        self.vacuumLocation = self.vacuumStartLocation
        #print(self.vacuumLocation)

    def setStartingLocation(self, x, y):
        self.vacuumStartLocation = [x, y]
        self.vacuumLocation = self.vacuumStartLocation

    def moveAgent(self, direction):
        # 0=up, 1=right, 2=down, 3=left

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

    def agentAction(self):
        if self.dirtEnv[self.vacuumLocation[0]][self.vacuumLocation[1]] == 1:
            self.suck()
            self.score += 1
        else:
            self.moveAgent(1)
            self.score -= 1

        cleanTiles = len(np.where(self.dirtEnv == 0))
        # Adds the number of clean tiles at that point in time to the score
        self.score += cleanTiles


    def runVacuum(self):
        while(self.cyclesLeft != 0):

            self.agentAction()
            #print(self.dirtEnv)
            self.cyclesLeft -= 1
            return self.score
        #print(self.score
class RelfexAgentWithRand(Environment):
        def __init__(self, Evironment, cycles=1000):
            self.tilesClean=0
            self.cyclesLeft=cycles
            self.agentLocation = Environment.locationSensor()
            self.score = 0
        def moveAgent(self):
            direction=  random.randrange(1, 4,1)
            if direction==1:
                pass
            if direction ==2:
                pass
            if direction ==3:
                pass
            if direction ==4:
                pass

        def agentAction(self):
            if self.dirtEnv[self.vacuumLocation[0]][self.vacuumLocation[1]] == 1:
                                self.suck()
                                self.tilesClean += 1
            else:
                self.moveAgent(1)
                self.score -= 1


        def runVacum(self):
            while(self.cyclesLeft != 0):
                self.agentAction()
                self.cyclesLeft -= 1
                self.score+=tilesClean







class ReflexAgentWithState(Environment):

    def __init__(self, Evironment, cycles=1000):
        self.state = []
        self.state = []
        self.model = []
        self.rules = []
        self.lastAction = None
        self.lastAction = None
        self.lastAction = None
        self.agentLocation = [0,0]
        self.score = 0

    def locationSensor(self):
        sensorLocationSize = 1
        tempMap = Environment.enviro
        tempCurrent = tempMap[self.agentLocation[0]][self.agentLocation[1]]

        try:
            tempUp = tempMap[self.agentLocation[0]-1][self.agentLocation[1]]
        except:
            tempUp = None
        try:
            tempRight = tempMap[self.agentLocation[0]][self.agentLocation[1]+1]
        except:
            tempRight = None
        try:
            tempDown = tempMap[self.agentLocation[0]+1][self.agentLocation[1]]
        except:
            tempDown = None
        try:
            tempLeft = tempMap[self.agentLocation[0]][self.agentLocation[1]-1]
        except:
            tempLeft = None


    #checks if dirt is present at current location
    def dirtSensor(self, location):
        dirtPresent = False
        # checks enviroment map if dirt is equal to 1
        if Enviroment.enviro[location[0]][location[1]] == 1:
            dirtPresent = True
        return dirtPresent

    def agentAction(self):
        if dirtSensor(self.agentLocation) == True:
            vacuumSuck()


    def vacuumSuck(self):
        Environment.enviro[self.agentLocation[0]][self.agentLocation[1]] = 0
        self.score += 1

    def runVacuum(self):
        return 0



# start (0,0) -> go down, if down is wall or node coordinates are (-1,-1) --- go diff direction AND check the same condition
# def functionFUNCTIONfunction(self):
#   pos = [0,0]
#   existsList[0]= (x=0,y=0)
#   ####since 0,0 you can only go positive so you either go down or right
#   # go right
#   if not wall
#       pos[] = [0,1] && exist[1]=true
