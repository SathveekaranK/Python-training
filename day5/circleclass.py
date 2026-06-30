class Circle:
    def __init__(self, r):
        self.radius = r
    def area(self):
        return 3.14 * self.radius * self.radius

r = float(input("Enter radius: "))
c = Circle(r)
print("Area of circle:", c.area())