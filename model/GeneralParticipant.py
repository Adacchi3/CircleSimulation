import numpy as np
import math

class GeneralParticipant:
    
    def __init__(self, id):
        self.id = id
        self.budget = 0
        while( self.budget <= 0):
            self.budget = math.floor(np.random.normal(3851.35,3641.7))
        self.start = np.random.randint(71)
        self.time = np.random.randint(71)
        self.alpha = np.random.rand()
        self.beta = 1 - self.alpha
        self.log = []
        self.circlelist = []
        self.like_category = np.random.randinit(47)
