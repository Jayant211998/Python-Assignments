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
class game:
    def __init__(self):
        self.P=person()
        self.d=deck()
    def play(self):
        global i
        if self.P.play(self.d)>=17:
            print("Player win after"+str(i)+"moves")
        else:
            i+=1
            self.play()

g=game()
g.play()