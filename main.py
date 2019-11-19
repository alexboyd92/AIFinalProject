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

scores = []

x,y = getUserSizeInput()
randomLocations = setRandomLocations()


if randomLocations == True:
    # Gets all permutations of matrix
    for m in islice(get_combinations(x, y), None):
        print(m) 
        for i in range(x):
            for j in range(y):
                print(i,j)
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

print(scores)
print('Iterations:', len(scores))
print('Average: {:.2f}'.format(sum(scores)/len(scores)))












