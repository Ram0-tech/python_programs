class Circle:
    def __init__(self):
        self.radius=float(input('Enter the radius: '))
    def getarea(self):
        area=3.14*self.radius**2
        print('Area of the circle:',area)
    def getperimeter(self):
        perimeter=2*3.14*self.radius
        print('Perimeter of the circle:',perimeter)
c=Circle()
# c.getarea()
p=Circle()
# p.getperimeter()
l=[c,p]
# print(l[0].radius,l[1].radius)
# l[0].getarea()
# l[0].getperimeter()

for i in l:
    print(i.radius)
    i.getarea()
    i.getperimeter()