import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w

class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return math.pi*self.r*self.r

r=Rectangle(4,5)
c=Circle(3)
print(f"Rectangle area: {r.area()}")
print(f"Circle area: {c.area()}")
