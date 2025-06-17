import idlelib.multicall


class Vehicle:
    def __init__(self):
        self.brand=input('Enter the brand:')
        self.model=input('Enter the model:')
        self.color = input('Enter the color:')
        self.year=int(input('Enter the year:'))
    def showdetails(self):
        print(self.brand,self.model,self.color,self.year)
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.fuel_type=input('Enter fuel type:')
    def showdetails(self):
        super().showdetails()
        print(self.fuel_type)
class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self.cc=int(input('Enter cc:'))
    def showdetails(self):
        super().showdetails()
        print(self.cc)

l=[]
while True:
    print(' 1.Car details\n','2.Bike details\n','3.Show all details\n','4.Exit')
    ch=int(input('Enter the choice:'))
    if ch==1:
        c=Car()
        l.append(c)
    elif ch==2:
        b=Bike()
        l.append(b)
    elif ch==3:
        for i in l:
            i.showdetails()
    else:
        print('Invalid choice!!!')
        exit()