l=[]
n=int(input())
for i in range(n):
        x=list(map(int,input().split(" ")))
        l.append(x)
a=sum(l[0])
count=0
for i in l:
    if sum(i)==a:
       count+=1
d=[0,0]
for i in range(n):
    for j in range(n):
        if i==j:
            d[0]+=l[i][j]
        elif i+j==2:
            d[1]+=l[i][j]
if d[0]==a:
    count+=1
if d[1]==a:
    count+=1
for i in range(n):
    s=0
    for j in range(n):
        s+=l[j][i]
    if s==a:
        count+=1
if count==(2*n+2):
    print("yes")


