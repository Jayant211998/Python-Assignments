import random
class card:
    def __init__(self,f,s,v):
        self.face=f
        self.suit=s
        self.value=v
    def __str__(self):
        return(f"face= ",self.face,"  suit= ",self.suit,"  value= ",self.value)
class deck:
    def __init__(self):
        self.l=[]
        lf=['A','K','Q','J']
        lv=[1,13,12,11]
        ls=["hearts","dimond","spad","club"]
        for i in ls:
            count=0
            for j in lf:
                c=card(j,i,lv[count])
                self.l.append(c)
                count+=1
        for p in range(2,11):
            c=card(str(p),i,p)
            self.l.append(c)
    def shuffle(self):
        random.shuffle(self.l)
    def first_move(self):
        a = self.l[0]
        b=self.l[1]
        self.l.pop(0)
        self.l.pop(0)
        return ([[a.value, a.face, a.suit],[b.value, b.face, b.suit]])                      #extend value
    def next_card(self):
        try:                                                                                #card finished
            a=self.l[0]
            self.l.pop(0)
            return([a.value,a.face,a.suit])
        except:
            print("Cards are finish ")
    def return_cards(self):
        return self.l

class hand:
    def __init__(self):
        self.list_of_cards=[]
    def draw_two(self,d):
         d.shuffle()
         self.list_of_cards.extend(d.first_move())
    def draw_one(self,d):
        d.shuffle()
        self.list_of_cards.append(d.next_card())
    def return_to(self):
        pass
turn=0
class player:
    def __init__(self,n):
        self.h = hand()
        self.name=n
        self.value=0
        self.credit=0
    def show_hand(self):
        print(self.h.list_of_cards)
    def play(self,d,num):
        global turn
        self.credit+=1
        if turn<num:
            self.h.draw_two(d)
        else:
            self.h.draw_one(d)
        self.value = 0
        for i in range(len(self.h.list_of_cards)):
            self.value+=self.h.list_of_cards[i][0]
        turn+=1
class game:
    def __init__(self):
        self.d=deck()
        self.list_of_players=[]
    def create_player(self):
        self.list_of_players=create()
    def play(self):
        num=len(self.list_of_players)
        while(True):
            for i in self.list_of_players:
                print("Turn of ",i.name)
                i.play(self.d,num)
                i.show_hand()
                print("Value till now is",i.value)
                if i.value>=20:
                    print("player",i.name,"wins in",i.credit,"turns")
                    exit(0)
def create():
    n=int(input("enter number of players"))
    l=[]
    for i in range(n):
        name=input("enter name of player: ")
        p=player(name)
        l.append(p)
    return l
g=game()
g.create_player()
g.play()
