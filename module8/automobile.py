class Automobile:
    def __init__(self,ma,mo,mi,p):
        self.make=ma
        self.model=mo
        self.milage=mi
        self.price=p
    def get_make(self,ma):
        self.__make=ma
    def get_model(self,mo):
        self.__model=mo
    def get_milege(self,mi):
        self.__milage=mi
    def get_price(self,p):
        self.__price=p
    def set_make(self):
        print(self.make)
    def set_model(self):
        print(self.model)
    def set_milege(self):
        print(self.milage)
    def set_price(self):
        print(self.price)
A=Automobile("tata",123,60,3000000)


