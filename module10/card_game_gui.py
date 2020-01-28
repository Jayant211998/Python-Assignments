from tkinter import *
import tkinter
import PIL
from PIL import Image,ImageTk
import random
import tkinter as tk
window = Tk()
frame=Frame(window)
frame.pack()
window.title("Card Game")
window.geometry("500x400")

class card:
    def __init__(self,f,s,v):
        self.face=f
        self.suit=s
        self.value=v
    def __str__(self):
        return(f"face= ",self.face,"  suit= ",self.suit,"  value= ",self.value)
def abc():
    return 1

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
        for i in self.h.list_of_cards:
            string=""
            for j in i:
                if i.index(j)==0:
                    string=string+str(j)
                else:
                    string = string + j
        load = Image.open(string+".png")
        render = ImageTk.PhotoImage(load)
        img = Label(image=render)
        img.image = render
        img.place(x=0, y=0)
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
        global all_player
        global chance
        if chance==0 and all_player==0:

                btn = Button(frame, text="Card ", bg="yellow", fg="red", width=4, height=2, font=("Times New Roman", "20"),
                command=next_player)
                btn.pack(side=LEFT)
                chance+=1
        btn1.after(0,btn1.destroy)
        print("Turn of ",self.list_of_players[all_player].name)
        self.list_of_players[all_player].play(self.d,len(self.list_of_players))
        self.list_of_players[all_player].show_hand()                                                        #show image
        print("Value till now is",self.list_of_players[all_player].value)
        if self.list_of_players[all_player].value>=50:
            print("player",self.list_of_players[all_player].name,"wins in",self.list_of_players[all_player].credit,"turns")
            exit(0)
        if all_player>=len(self.list_of_players)-1:
            all_player=-1
all_player=0
chance=0
def next_player():
    global all_player
    global g
    all_player+=1
    g.play()
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
btn1 = Button(frame, text="Play ", bg="white", fg="black", font=("Times New Roman", "20"),command=g.play)
btn1.pack(side=RIGHT)
window.mainloop()