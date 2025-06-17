from abc import ABC,  abstractmethod
class Shape(ABC):
    @abstractmethod
    def getarea(self):
       pass
    @abstractmethod
    def getperimeter(self):
        pass
class Circle(Shape):
    def __init__(self):
       self.radius=float(input('Enter the  radius:'))
    def getarea(self):
       area=3.14*self.radius**2
       print('Area:',area)
    def getperimeter(self):
       perimeter=2*3.14*self.radius
       print('Perimeter:',perimeter)
c=Circle()
c.getarea()
c.getperimeter()

class Rectangle(Shape):
    def __init__(self):
       self.length=float(input('Enter the  length:'))
       self.width=float(input('Enter the width:'))
    def getarea(self):
       area=self.length*self.width
       print('Area:',area)
    def getperimeter(self):
       perimeter=2*(self.length+self.width)
       print('Perimeter:',perimeter)
r=Rectangle()
r.getarea()
r.getperimeter()
      
