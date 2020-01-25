from card_game import deck
class hand:
    def __init__(self):
        self.h=[]
        self.value=0
        #self.d=deck()
    def draw_from(self,d):
        d.shuffle()
        self.h.append(d.next_card())
        self.value+=self.h[0][0]
        a=self.h[0]
        self.h.pop(0)
        self.h.append(a)
        print(self.value)
        return self.value
    def return_to(self):
        a=self.h[0]
        self.d.l.append(a)
        self.h.remove(a)
#print(H1.h,H1.value)
class person:
    def __init__(self):
        self.H=hand()
        self.name="Jayant"
    def play(self,d):
        return self.H.draw_from(d)
    def show_hand(self):
        print(self.H.h)
        print(self.H.value)
i=1
n=int(input("enter number of players"))
player=[]
values=[]
for j in range(n):
    p=person()
    player.append(p)
    values.append(0)

class game:
    def __init__(self):
        self.P=player
        self.d=deck()
    def play(self):
        for i in range(len(self.P)):
            values[i]=self.P[i].play(self.d)
        while(True):
            for i in values:
                if values[i]>=20:
                    print("Player "+str(i+1)+" wins")
                    break

g=game()
g.play()