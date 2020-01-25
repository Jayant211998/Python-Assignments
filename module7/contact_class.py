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
c=contact("jayant","jayantgawali98@gmail.com",9340216311)
c.set()
name=input("enter name ")
phone=input("enter phone ")
email=input("enter email")
c.get(name,email,phone)
c.set()