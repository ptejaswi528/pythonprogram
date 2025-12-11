from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
if __name__ == "__main__":
    l = int(input("Enter length of rectangle: "))
    b = int(input("Enter breadth of rectangle: "))
    ob = Rectangle(l, b)
    print(f"Area of Rectangle: {ob.area()}")
    r = int(input("Enter radius of circle: "))
    c = Circle(r)
    print(f"Area of Circle: {c.area()}")
