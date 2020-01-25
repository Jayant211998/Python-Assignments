def read(file_read):
    r = file_read.read()
    print(r)
def write(file_write,c):
    file_write.write("name:" + c.name + "\n")
    file_write.write("phone:" + c.phone + "\n")
    file_write.write("email:" + c.email + "\n")
    c.set()
    file_write.close()
def update(file_write,c):
    file_write = open("update.txt", "w")
    print("Enter new Data")
    name = input("enter name ")
    phone = input("enter phone ")
    email = input("enter email ")
    c.get(name, email, phone)
    file_write.write("name"+c.name+"\n")
    file_write.write("phone"+c.phone+"\n")
    file_write.write("email"+c.email+"\n")
    c.set()
    file_write.close()
def Exit():
    exit(0)
file_write=open("update.txt","w")
file_read=open("update.txt","r")
class contact:
    def __init__(self,n,e,p):
        self.name=n
        self.phone=p
        self.email=e
    def get(self,n,e,p):
        self.name=n
        self.phone=p
        self.email=e
    def set(self):
        print("name: ",self.name)
        print("phone number: ", self.phone)
        print("email: ", self.email)
c=contact("jayant","jayantgawali98@gmail.com","9340216311")
while(True):
    print("1. Write File ")
    print("2. Read File ")
    print("3. Update File ")
    print("4. Exit")
    i=int(input("Enter Choice "))
    if i==1:
        write(file_write,c)
    elif i==2:
        read(file_read)
    elif i==3:
        update(file_write,c)
    elif i==4:
        Exit()
