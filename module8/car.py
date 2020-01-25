from automobile import Automobile as A
class Car(A):
    def  __init__(self,make,model,milege,price,doors):
        A.__init__(self,make,model,milege,price)
        self.doors =doors
    def set_doors(self):
        print(self.doors)
    def get_doors(self,d):
        self.doors=d
class Truck(A):
    def  __init__(self,make,model,milege,price,dt):
        A.__init__(self,make,model,milege,price)
        self.drivetype =dt
    def set_drivetype(self):
        print(self.drivetype)
    def get_drvetype(self,d):
        self.drivetype=d

class suv(A):
    def  __init__(self,make,model,milege,price,pc):
        A.__init__(self,make,model,milege,price)
        self.pass_cap =pc
    def set_doors(self):
        print(self.pass_cap)
    def get_doors(self,pc):
        self.pass_cap=pc


C=Car("Tata",132,60,1000000,4)
C.get_make("abc")
C.get_doors(5)
C.get_milege(40)
C.get_model("ABC")
C.get_price(100000)
C.set_doors()
C.set_make()
C.set_milege()
C.set_model()
C.set_price()


