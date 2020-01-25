n=int(input("enter number of fruits "))
fruit_list=[]
i=1
d0=dict()
while(n>0):
    d=dict()
    d0[i]=d
    name = input("name ")
    fruit_list.append(name)
    d1=dict()
    d[name] = d1
    d1['binomial name'] = input('binomial name ')
    print("name of 3 major producers ", end=" ")
    l = []
    l.append(input().split(" "))
    d1['major producer'] = l
    d2=dict()
    d1['nutrients'] = d2
    d2['carbs'] = int(input("carbs"))
    d2['protien'] = int(input("protiens"))
    d2['fat'] = int(input("fat"))
    i+=1
    n-=1
print(d0)
m=[]
for x in range(i):
    try:
        m.append(d0[x+1][fruit_list[x]]['nutrients']['protien'])
    except KeyError:
        print("",end="")
for x in range(i):
    try:
        if max(m)==d0[x+1][fruit_list[x]]['nutrients']['protien']:
            print(fruit_list[x])
    except KeyError:
        print("",end="")
