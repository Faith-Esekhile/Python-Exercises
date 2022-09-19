import random
class Coin:
    def __init__(self):
        self.sideup="heads"
    def toss(self):
        if random.randint(0,1)==0:
            self.sideup="heads"
        else:
            self.sideup="tails"
    def get_sideup(self):
        return self.sideup