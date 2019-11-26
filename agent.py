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
        #print(self.score)

class ReflexAgentWithRand(Environment):
        def __init__(self, Evironment, cycles=1000):
            self.tilesClean=0
            self.cyclesLeft=cycles
            self.agentLocation = [0,0]
            self.score = 0
            self.env = Evironment

        def moveAgent(self, locSensor):
            self.agentLocation = self.pickLocation(locSensor)
            print('Moving to:', self.agentLocation)
        
        def locationSensor(self):
            sensorLocationSize = 1
            tempMap = self.env.enviro
            try:
                tempUp = tempMap[self.agentLocation[0]-1][self.agentLocation[1]]
                tempUploc = [self.agentLocation[0]-1, self.agentLocation[1]]
            except:
                tempUp = 2
                tempUploc = [-1,-1]
            try:
                tempRight = tempMap[self.agentLocation[0]][self.agentLocation[1]+1]
                tempRightLoc = [self.agentLocation[0], self.agentLocation[1]+1]
            except:
                tempRight = 2
                tempRightLoc = [-1,-1]
            try:
                tempDown = tempMap[self.agentLocation[0]+1][self.agentLocation[1]]
                tempDownLoc = [self.agentLocation[0]+1, self.agentLocation[1]]
            except:
                tempDown = 2
                tempDownLoc = [-1,-1]
            try:
                tempLeft = tempMap[self.agentLocation[0]][self.agentLocation[1]-1]
                tempLeftLoc = [self.agentLocation[0], self.agentLocation[1]-1]
            except:
                tempLeft = 2
                tempLeftLoc = [-1,-1]

            return [tempUp, tempUploc, tempRight, tempRightLoc, tempDown, tempDownLoc, tempLeft, tempLeftLoc]

        def pickLocation(self, locSensor):
            directions = []
            if ((locSensor[0] != 2) and (-1 not in locSensor[1])):
                directions.append(locSensor[1])
            if ((locSensor[2] != 2) and (-1 not in locSensor[3])):
                directions.append(locSensor[3])
            if ((locSensor[4] != 2) and (-1 not in locSensor[5])):
                directions.append(locSensor[5])
            if ((locSensor[6] != 2) and (-1 not in locSensor[7])):
                directions.append(locSensor[7])
            
            nDirections = len(directions)
            if nDirections == 0:
                return self.agentLocation
            rDir = r.randint(0,nDirections-1)

            return directions[rDir]


        def vacuumSuck(self):
            self.env.enviro[self.agentLocation[0]][self.agentLocation[1]] = 0
            self.tilesClean += 1
            self.score += self.tilesClean

        def agentAction(self):
            if self.env.enviro[self.agentLocation[0]][self.agentLocation[1]] == 1:
                print('Sucking tile:', self.agentLocation)
                self.vacuumSuck()
                self.tilesClean += 1
            else:
                locSensor = self.locationSensor()
                self.moveAgent(locSensor)
                self.score -= 1


        def runVacuum(self):
            while(self.cyclesLeft != 0):
                if 1 not in self.env.enviro:
                    break
                self.agentAction()
                self.cyclesLeft -= 1
                print(self.env.enviro)
            return self.score







class ReflexAgentWithState(Environment):

    def __init__(self, Environ, cycles=1000):
        
        self.lastAction = 0
        self.agentLocation = [0,0]
        self.tilesClean = 0
        self.score = 0
        self.cyclesLeft = cycles
        self.env = Environ
        self.bump = False
        self.state = [[0,0]]
        print(self.env.enviro)


    def locationSensor(self):
        sensorLocationSize = 1
        tempMap = self.env.enviro
        try:
            tempUp = tempMap[self.agentLocation[0]-1][self.agentLocation[1]]
            tempUploc = [self.agentLocation[0]-1, self.agentLocation[1]]
        except:
            tempUp = 2
            tempUploc = [-1,-1]
        try:
            tempRight = tempMap[self.agentLocation[0]][self.agentLocation[1]+1]
            tempRightLoc = [self.agentLocation[0], self.agentLocation[1]+1]
        except:
            tempRight = 2
            tempRightLoc = [-1,-1]
        try:
            tempDown = tempMap[self.agentLocation[0]+1][self.agentLocation[1]]
            tempDownLoc = [self.agentLocation[0]+1, self.agentLocation[1]]
        except:
            tempDown = 2
            tempDownLoc = [-1,-1]
        try:
            tempLeft = tempMap[self.agentLocation[0]][self.agentLocation[1]-1]
            tempLeftLoc = [self.agentLocation[0], self.agentLocation[1]-1]
        except:
            tempLeft = 2
            tempLeftLoc = [-1,-1]

        return [tempUp, tempUploc, tempRight, tempRightLoc, tempDown, tempDownLoc, tempLeft, tempLeftLoc]



    def agentAction(self):
        # 0 = no movement, 1 = suck, 2 = move up, 3 = move right, 4 = move down, 5 = move left
        
        if self.env.enviro[self.agentLocation[0]][self.agentLocation[1]] == 1:
            self.vacuumSuck()
            self.lastAction = 1
        else:
            #move vacuum
            if self.bump == True:
                pass
            else:
                locSensor = self.locationSensor()
                self.moveAgent(locSensor)
       

    def moveAgent(self, locSensor):
        #print(locSensor) #Print locSensor radius
        if locSensor[0] == 1:
            self.agentLocation[0] = self.agentLocation[0]-1
            self.lastAction = 2
            #print('move up1')
        elif locSensor[2] == 1:
            self.agentLocation[1] = self.agentLocation[1]+1
            self.lastAction = 4
            #print('move right1')
        elif locSensor[4] == 1:
            self.agentLocation[0] = self.agentLocation[0]+1
            self.lastAction = 3
            #print('move down1')
        elif locSensor[6] == 1:
            self.agentLocation[1] = self.agentLocation[1]-1
            self.lastAction = 5
            #print('move left1')
        else:
            move = False
            tempLocation = locSensor[1]
            # move up
            if (locSensor[0] != 2) and (-1 not in locSensor[1]) and (tempLocation not in self.state) and (move == False):
                self.agentLocation[0] = self.agentLocation[0]-1
                self.lastAction = 2
                move = True
                #print('move up2')

            tempLocation = locSensor[5]
            # move down
            if (locSensor[4] != 2) and (-1 not in locSensor[5]) and (tempLocation not in self.state) and (move == False):
                self.agentLocation[0] = self.agentLocation[0]+1
                self.lastAction = 4
                move = True
                #print('move down2')

            tempLocation = locSensor[3]
            #move right
            if (locSensor[2] != 2) and (-1 not in locSensor[3]) and (tempLocation not in self.state) and (move == False):
                self.agentLocation[1] = self.agentLocation[1]+1
                self.lastAction = 3
                move = True
                #print('move right2')
            
            tempLocation = locSensor[7]
            # move left
            if (locSensor[6] != 2) and (-1 not in locSensor[7]) and (tempLocation not in self.state) and (move == False):
                self.agentLocation[1] = self.agentLocation[1]-1
                self.lastAction = 5
                move = True
                #print('move left2')

            if move == False:
                if self.lastAction == 2:
                    self.agentLocation[0] = self.agentLocation[0]+1
                    self.lastAction = 4
                    #print('move backwards2')

                elif self.lastAction == 3:
                    self.agentLocation[1] = self.agentLocation[1]-1
                    self.lastAction = 5
                    #print('move backwards3')

                elif self.lastAction == 4:
                    self.agentLocation[0] = self.agentLocation[0]-1
                    self.lastAction = 2
                    #print('move backwards4')

                elif self.lastAction == 5:
                    self.agentLocation[1] = self.agentLocation[1]+1
                    self.lastAction = 3
                    #print('move backwards5')
            
                
        self.score -= 1
        if self.agentLocation not in self.state:
            self.state.append(self.agentLocation[:])

    def vacuumSuck(self):
        self.env.enviro[self.agentLocation[0]][self.agentLocation[1]] = 0
        self.tilesClean += 1
        self.score += self.tilesClean

    def runVacuum(self):
         while(self.cyclesLeft != 0):
            if 1 not in self.env.enviro:
                break
            self.agentAction()
            self.cyclesLeft -= 1
            print(self.env.enviro)
            #print(self.state)
            
            print('Current Location:', self.agentLocation)
         return self.score



# start (0,0) -> go down, if down is wall or node coordinates are (-1,-1) --- go diff direction AND check the same condition
# def functionFUNCTIONfunction(self):
#   pos = [0,0]
#   existsList[0]= (x=0,y=0)
#   ####since 0,0 you can only go positive so you either go down or right
#   # go right
#   if not wall
#       pos[] = [0,1] && exist[1]=true
