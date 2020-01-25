class car:
    def __init__(self,color,milage):
        self.color=color
        self.milage=milage
    def __str__(self):
        return f'a {self.color} car'
c1=car("red",63)
print(c1)