import winsound
from tkinter import *
n=int(input("Enter Number"))
def number(n):
    if n==0:
        var="Zero"
    elif n==1:
        var="One"
    elif n==2:
        var="Two"
    elif n==3:
        var="Three"
    elif n==4:
        var="Four"
    elif n==5:
        var="Five"
    elif n==6:
        var="Six"
    elif n==7:
        var="Seven"
    elif n==8:
        var="Eight"
    elif n==9:
        var="Nine"
    elif n==10:
        var="Ten"
    elif n==11:
        var="Eleven"
    elif n==12:
        var="Twelve"
    elif n==13:
        var="Thirteen"
    elif n==14:
        var="Fourteen"
    elif n==15:
        var="Fifteen"
    elif n>=16 and n<=19:
        var=number(n-10)+"teen"
    elif n==20:
        var="Twenty"
    elif n==30:
        var="Thirty"
    elif n==50:
        var="Fifty"
    elif n>=40 and n<=90 and n%10==0:
        var=number(n//10)+"ty"
    elif n>20 and n<100:
        v=n%10
        var=number(n-v)+number(v)
    elif n%100==0 and n<1000 and n>=100:
        var=number(n//100)+"Hundred"
    elif n%100!=0 and n<1000 and n>=100:
        v=n-(n // 100)*100
        var = number(n // 100) + "Hundred and "+number(v)
    elif n%1000==0 and n<10000:
        var = number(n // 100) + "Thousand"
    elif n%1000!=0 and n<10000 and n>=1000:
        v=n-(n // 1000)*1000
        var = number(n // 1000) + "Thousand"+number(v)
    elif n==10000:
        var="TenThousand"
    else:
        var="error"
    return var
print(number(n))
l=[]
while(n>0):
    l.append(n%10)
    n=n//10
l.reverse()
for i in l:
    winsound.PlaySound(str(i) + '.wav', winsound.SND_FILENAME)
