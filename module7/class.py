import random
class coin:
    def  __init__(self):
        self.sideup='heads'
    def toss(self):
        if random.randint(0,1)==0:
            self.sideup = 'heads'
        else:
            self.sideup='Tails'
        print(self.sideup)
    def get_sideup(self):
        return self.sideup
def main():
    c=coin()
    c.toss()
    print('this side is up',c.get_sideup())
main()