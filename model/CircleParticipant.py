import numpy as np
import math

class CircleParticipant:
    
    def __init__(self, 
    id, 
    bookfee= -1, 
    book_quality = -1,
    ad = -1,
    dm = -1,
    category = -1,
    price = -1 ):
        self.id = id
        self.bookfee = bookfee
        while( self.bookfee <= 0):
            self.bookfee = math.floor(np.random.normal(30757.57,29924.93))
        #self.book_quality = 0.5 + (self.bookfee-30757.57)/(3*29924.93)
        self.book_quality = book_quality
        while( self.book_quality <= 0 ):
            self.book_quality = np.random.normal(0.5,0.2)
        self.ad = ad
        while( self.ad <= 0 ):
            self.ad = np.random.rand()
        self.dm = dm
        while( self.dm <= 0 ):
            self.dm = np.random.rand()
        self.category = category
        while( self.category < 0):
            self.category = np.random.randint(47)
        self.price = price
        while( self.price <= 0):
            self.price = math.floor(np.random.normal(596,382.15))

    def show_info(self):
        str =  "{{\'id\': {0.id}, \'bookfee\': {0.bookfee}, \'book_quality\': {0.book_quality}, \'ad\': {0.ad}, \'dm\': {0.dm}, \'category\': {0.category}, \'price\': {0.price}}}".format(self)
        return str

if __name__ == '__main__':
    agent = CircleParticipant(1,48400,0.7,0.5,0.5,1,800)
    print(agent.show_info())
