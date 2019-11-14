from enviroment import Environment
from agent import SimpleReflexAgent
from itertools import islice
import numpy as np
from itertools import product


def get_combinations(n, m):
    for flat in product([1, 0], repeat=n*m):
        yield np.reshape(flat, (n, m))

scoreTotal = 0

env = Environment(2, 2)
print('Environment:')
env.print_shape()
print('Initial Location:', end=' ')

# Gets all permutations of matrix
for m in islice(get_combinations(2, 2), None):
    print(m)




vacuum = SimpleReflexAgent(env)
print('Vacuum Start:\n')
vacuum.runVacuum()




