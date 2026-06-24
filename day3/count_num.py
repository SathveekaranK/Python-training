class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    
    def area(self):
        print(self.length * self.breadth)

r1=Rectangle(2,2)
r1.area()