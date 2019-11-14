from enviroment import Environment
from agent import SimpleReflexAgent

scoreTotal = 0

env = Environment(2, 2)
print('Environment:')
env.print_shape()
print('Initial Location:', end=' ')
vacuum = SimpleReflexAgent(env)
print('Vacuum Start:\n')
vacuum.runVacuum()


