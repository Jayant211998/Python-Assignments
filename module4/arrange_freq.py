l=list(map(int,input().split(" ")))
d=dict()
for i in l:
    d[i]=l.count(i)
x=[]
for i in d.values():
   x.append(i)
y=[]
for i in d.keys():
   y.append(i)

for i in range(len(x)):
    m=x[i]
    for j in range(i,len(x)):
        if x[i]<x[j]:
            x[i],x[j]=x[j],x[i]
            y[i],y[j]=y[j],y[i]
print(y)
for i in range(len(x)):
    m=y[i]
    for j in range(i,len(x)):
        if y[i]>y[j] and d[y[i]]==d[y[j]]:
            y[i],y[j]=y[j],y[i]
for i in y:
    print((str(i)+" ")*d[i],end=" ")