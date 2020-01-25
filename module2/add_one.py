x=int(input())
n=0
l=[]
while(x>0):
    l.append(x%10)
    x=x//10
for i in range(len(l)):
    n=n+(((l[i]+1)%10)*(10**i))    
print(n)