import random
class card:
    def __init__(self,f,s,v):
        self.face=f
        self.suit=s
        self.value=v
    def __str__(self):
        return(f"face= ",self.face,"  suit= ",self.suit,"  value= ",self.value)
c=[]
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
    def next_card(self):
        a=self.l[0]
        self.l.remove(self.l[0])
        return([a.value,a.face,a.suit])

# print(d.next_card())
