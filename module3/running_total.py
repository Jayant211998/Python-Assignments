n=list(map(int,input("").split(" ")))
l=list(map(int,input("").split(" ")))
x=[]
for k in l:
    i=j=l.index(k)
    s1=s2=k
    a=n[1]-1
    while(a>0):
        i=(i+1)%(n[0])
        s1+=l[i]
        j=(j-1)%(n[0])
        s2+=l[j]
        a-=1
    x.append(s1)
    x.append(s2)
print(max(x))