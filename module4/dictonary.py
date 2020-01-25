Ques1:
d=dict()
n=int(input("enter number of records"))
for i in range(1,n+1):
    d1=dict()
    d1['name']=input("Name ")
    d1['age']=input("age ")
    d1['gender']=input("Gender ")
    d[i]=d1
del d[2]['gender']
print(d)

Ques2:
d=dict()
n=int(input("enter number of records"))
for i in range(1,n+1):
    d1=dict()
    d1['name']=input("Name ")
    d1['age']=input("age ")
    d1['gender']=input("Gender ")
    d[i]=d1
for i in d.items():
    print(" personID",i)
for key in d:
    print(d[key])

