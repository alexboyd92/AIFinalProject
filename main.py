from enviroment import Environment
from agent import SimpleReflexAgent

env = Environment()
env.print_shape()
vacuum = SimpleReflexAgent(env)