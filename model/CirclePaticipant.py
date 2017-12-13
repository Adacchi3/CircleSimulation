import numpy as np
import math

class CircleParticipant:
    
    def __init__(self, id):
        self.id = id
        self.bookfee = 0
        while( self.bookfee <= 0):
            self.bookfee = math.floor(np.random.normal(30757.57,29924.93))
        #self.book_quality = 0.5 + (self.bookfee-30757.57)/(3*29924.93)
        self.book_quality = np.random.normal(0.5,0.2)
        self.ad = np.random.rand()
        self.dm = np.random.rand()
        self.category = np.random.randint(47)
        self.price = math.floor(np.random.normal(596,382.15))

"""
if __name__ == '__main__':
    agent = CircleParticipant(1)
    print(agent.id)
    print(agent.price)
    print(agent.ad)
    print(agent.dm)
    print(agent.book_quality)
"""