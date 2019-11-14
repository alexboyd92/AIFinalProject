from enviroment import Environment
from agent import SimpleReflexAgent

env = Environment(3,3)
print('Environment:')
env.print_shape()
print('Initial Location:', end=' ')
vacuum = SimpleReflexAgent(env)
print('Vacuum Start:\n')
vacuum.runVacuum()