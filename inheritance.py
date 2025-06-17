# single inheritance

# class A:
#     def m1(self):
#         print('Class A method of m1')
#     def m2(self):
#         print('Class A method of m2')
# a=A()
# a.m1()
# class B(A):
#   def m1(self):
#       super().m1()
#       print('Class B method of m1')
#
#   def m3(self):
#       print('Class A method of m3')
# b=B()
# b.m1()
# b.m3()


# class Person:
#     def __init__(self):
#         self.name=input('Enter the name:')
#         self.age=int(input('Enter age:'))
#     def show(self):
#         print(self.name,self.age)
# class Employee(Person):
#     def __init__(self):
#         super().__init__()
#         self.empid=int(input('Enter the employeeid:'))
#         self.salary=float(input('Enter salary:'))
#     def show(self):
#         super().show()
#         print(self.empid,self.salary)
# e=Employee()
# e.show()


# class Vehicle:
#     def __init__(self):
#         self.brand=input('Enter the brand:')
#         self.model=input('Enter the model:')
#         self.color = input('Enter the color:')
#         self.year=int(input('Enter the year:'))
#     def showdetails(self):
#         print(self.brand,self.model,self.color,self.year)
# class Car(Vehicle):
#     def __init__(self):
#         super().__init__()
#         self.fuel_type=input('Enter fuel type:')
#     def showdetails(self):
#         super().showdetails()
#         print(self.fuel_type)
#
# # v1=Vehicle()
# # v1.showdetails()
# # v2=Vehicle()
# # v2.showdetails()
# c1=Car()
# c1.showdetails()
# c2=Car()
# c2.showdetails()


# hierarchical inheritance
# class Vehicle:
#     def __init__(self):
#         self.brand=input('Enter the brand:')
#         self.model=input('Enter the model:')
#         self.color = input('Enter the color:')
#         self.year=int(input('Enter the year:'))
#     def showdetails(self):
#         print(self.brand,self.model,self.color,self.year)
# class Car(Vehicle):
#     def __init__(self):
#         super().__init__()
#         self.fuel_type=input('Enter fuel type:')
#     def showdetails(self):
#         super().showdetails()
#         print(self.fuel_type)
# class Bike(Vehicle):
#     def __init__(self):
#         super().__init__()
#         self.cc=int(input('Enter cc:'))
#     def showdetails(self):
#         super().showdetails()
#         print(self.cc)
# b=Bike()
# b.showdetails()


# multiple inheritance
class Hospital:
    def __init__(self):
        print('Hospital Details:')
        self.hos_name=input('Enter the hospital name:')
        self.phno=int(input('Enter the phn no:'))
        self.location=input('enter the place:')
    def display_details(self):
        print(self.hos_name,self.phno,self.location)
class Department:
    def __init__(self):
        print('Department Details:')
        self.department_name=input('Enter the department name:')
        self.hod=input('enter head of the department:')
        self.docname=input('Enter name of the doctor:')
    def display_details(self):
        print(self.department_name,self.hod,self.docname)

class Patient(Hospital,Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        print('Patient Details:')
        self.name=input('Enter patient name:')
        self.age=int(input('Enter  age:'))
        self.gender=input('Enter gender:')
        self.phn=int(input('Enter phone no:'))
    def display_details(self):
        Hospital.display_details(self)
        Department.display_details(self)
        print(self.name,self.age,self.gender,self.phn)

p=Patient()
p.display_details()