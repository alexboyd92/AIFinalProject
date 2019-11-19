from enviroment import Environment
from agent import SimpleReflexAgent
from itertools import islice, product, permutations
import numpy as np


def getUserSizeInput():
    print('Input x size: ')
    x = int(input())
    print('Input y size: ')
    y = int(input())
    return list([x,y])

# sets whether all permutation computation is on or off
def setRandomLocations():
    print('All Permutations (True or False):')
    return bool(input())

def get_combinations(n, m):
    for flat in product([1, 0], repeat=n*m):
        yield np.reshape(flat, (n, m))
print ("Select which agent to use \n1)Normal agent \n2)state agent 3\n)random agent")
try :
    agentSel=int(input())
except:
    print("Error")
if agentSel ==1:
    scores = []
    x,y = getUserSizeInput()
    randomLocations = setRandomLocations()
    if randomLocations == True:
          # Gets all permutations of matrix
        for m in islice(get_combinations(x, y), None):
            #print(m) 
            for i in range(x):
                for j in range(y):
                    #print(i,j)
                    env = Environment(x, y, enviro=m)
                    vacuum = SimpleReflexAgent(env)
                    vacuum.setStartingLocation(i, j)
                    scores.append(vacuum.runVacuum())
    
    else:
        env = Environment(x, y)
        print('Environment:')
        env.print_shape()
        print('Initial Location:', end=' ')
        vacuum = SimpleReflexAgent(env)
        print('Vacuum Start:\n')
        vacuum.runVacuum()


else:
    print ("Select map 1-3")
    mapChoice = int(input())
    if mapChoice==1:
        env = Environment()
        env.setEnviro(Environment.MAP1)
    if mapChoice==2:
        env = Environment()
        env.setEnviro(Environment.MAP2)
    if mapChoice==3:
        env = Environment()
        env.setEnviro(Environment.MAP3)

    if agentSel==2:
        agent = ReflexAgentWithState(env)
        score = agent.runVacuum()
    if agenSel==3:
        agent = RelfexAgentWithRand(env)
        score = agent.runVacuum()





#print(scores)
print('Iterations:', len(scores))
print('Average: {:.2f}'.format(sum(scores)/len(scores)))












