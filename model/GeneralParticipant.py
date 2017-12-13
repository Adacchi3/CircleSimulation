import numpy as np
import math

class GeneralParticipant:
    
    def __init__(self, id):
        self.id = id
        self.budget = 0
        while( self.budget <= 0):
            self.budget = math.floor(np.random.normal(3851.35,3641.7))
        self.money = self.budget
        self.start = np.random.randint(71)
        self.time = np.random.randint(71)
        self.alpha = np.random.rand()
        self.beta = 1 - self.alpha
        self.log = []
        self.circlelist = []
        self.like_category = np.random.randint(47)

    def show_info(self):
        str =  "{{\'id\': {0.id}, \'budget\': {0.budget}, \'money\': {0.money}, \'start\': {0.start}, \'time\': {0.time}, \'alpha\': {0.alpha}, \'beta\': {0.beta}, \'like_category\': {0.like_category}, \'log\': {0.log}, \'circlelist\': {0.circlelist}}}".format(self)
        return str

    def check_ad(self, circles):
        for i in range(0, len(circles)):
            if(np.random.rand()<0.1):
                self.circlelist.append(circles[i].id)
        return
"""
if __name__ == '__main__':
    agent = GeneralParticipant(1)

    circles = []
    i = 0
    for i in range(100):
        circles.append(CircleParticipant(i))
    print(circles)
    agent.check_ad(circles)
    print(agent.show_info())
"""