import random as r
from enviroment import Environment

class SimpleReflexAgent(Environment):
    def __init__(self, Environment):

        # Gets the size of the environment
        size = Environment.getSize

        # Gets the dirt placement map
        dirtEnv = Environment.enviro
        
        # Performance Score
        score = 0
        
        # Randomized starting vacuum location based on size 
        vacuumLocation = [r.randint(0,size[0]), r.randint(0,size[1])]









