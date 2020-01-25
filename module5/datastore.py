def change_roomuse(n,u,o,m):
    global datastore
    for i in range(len(datastore["office0"]["medical0"])):
        if n==datastore["office0"]["medical0"][i]["room-number"]:
            datastore["office"+str(o)]["medical"+str(m)][i]["use"]=u
    
def change_roomnum(n1,n2,o,m):
    global datastore
    for i in range(len(datastore["office0"]["medical0"])):
        if n1==datastore["office0"]["medical0"][i]["room-number"]:
            datastore["office"+str(o)]["medical"+str(m)][i]["room-number"]=n2

def change_roomprice(n,p,o,m):
    global datastore
    for i in range(len(datastore["office0"]["medical0"])):
        if n==datastore["office0"]["medical0"][i]["room-number"]:
            datastore["office"+str(o)]["medical"+str(m)][i]["price"]=p


def create_office(n):
    global datastore
    if n==0:
        return 0
    for i in range(1,n+1):
        datastore["office"+str(i)]=datastore["office0"]
    
def create_parking(n):
    global datastore
    if n==0:
        return 0
    for i in range(1,n+1):
        datastore["office"]["parking"+str(i)]=datastore["office0"]["parking0"]
    
def create_medical(n):
    global datastore
    if n==0:
        return 0
    for i in range(1,n+1):
        datastore["office"]["medical"+str(i)]=datastore["office0"]["medical0"]

    
datastore={"office0":{"medical0":[{"room-number":100,"use":"reception","sq-ft":50,"price":75},{"room-number":101,"use":"waiting","sq-ft":50,"price":75},{"room-number":102,"use":"examination","sq-ft":50,"price":75},{"room-number":100,"use":"office","sq-ft":50,"price":75}],"parking0":{"location":"premium","style":"covered","price":750}}}

def ru():
    print("change use of room-number")
    num=int(input("enter room number whose use is to be changed "))
    use=input("enter new use of room  ")
    o=int(input("enter office number to be changed"))
    m=int(input("enter medical number to be changed"))
    change_roomuse(num,use,o,m)
    print()
def rn():
    print("change room number")
    n1=int(input("enter room number to be changed "))
    n2=int(input("enter new room number "))
    o=int(input("enter office number to be changed"))
    m=int(input("enter medical number to be changed"))
    change_roomnum(n1,n2,o,m)
    print()
def rp():
    print("change room price")
    n=int(input("enter room number whose price is to be changed "))
    p=int(input("enter new price of room "))
    o=int(input("enter office number to be changed"))
    m=int(input("enter medical room number to be changed"))
    change_roomprice(n,p,o,m)
    print()
def cno():
    print("Create new office")
    n=int(input("Enter number of offices to be created"))
    create_office(n)
    print()
def cnp():
    print("Create new parking")
    n=int(input("Enter number of parkings to be created"))
    create_parking(n)
    print()
def cnm():
    print("Create new medical rooms")
    n=int(input("Enter number of parkings to be created"))
    create_medical(n)
    print()
def sd():
    print("Show details")
    print(datastore)

print("1.Chage room Use")
print("2.Chage room Number")
print("3.Chage room price")
print("4.Create Office")
print("5.Create Parking")
print("6.Create Medical")
print("7.showdetails")
i=int(input("Enter Choice "))
d={1:ru(),2:rn(),3:rp(),4:cno(),5:cnp(),6:cnm(),7:sd()}
d[i]
