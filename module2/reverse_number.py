x=int(input())
l=[]
n=0
while(x>0):
    l.append(x%10)
    x=x//10
l.reverse()
for i in range(len(l)):
    n=n+(l[i]*(10**i))
print(n)
   