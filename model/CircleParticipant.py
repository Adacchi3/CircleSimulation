import numpy as np
import math

class CircleParticipant:
    
    def __init__(self, 
    id, 
    bookfee=math.floor(np.random.normal(30757.57,29924.93)), 
    book_quality = np.random.normal(0.5,0.2),
    ad = np.random.rand(),
    dm = np.random.rand(),
    category = np.random.randint(47),
    price = math.floor(np.random.normal(596,382.15))):
        self.id = id
        self.bookfee = bookfee
        while( self.bookfee <= 0):
            self.bookfee = math.floor(np.random.normal(30757.57,29924.93))
        #self.book_quality = 0.5 + (self.bookfee-30757.57)/(3*29924.93)
        self.book_quality = book_quality
        self.ad = ad
        self.dm = dm
        self.category = category
        self.price = price

    def show_info(self):
        str =  "{{\'id\': {0.id}, \'bookfee\': {0.bookfee}, \'book_quality\': {0.book_quality}, \'ad\': {0.ad}, \'dm\': {0.dm}, \'category\': {0.category}, \'price\': {0.price}}}".format(self)
        return str

if __name__ == '__main__':
    agent = CircleParticipant(1,48400,0.7,0.5,0.5,1,800)
    print(agent.show_info())
