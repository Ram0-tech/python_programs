# class Person:
#     #constructor method
#     def __init__(self,n,a):  #__init__ is a constructor method to create and initialize attributes of objects
#         self.name=n          #here self is a keyword represents current object
#         self.age=a           #here name and age are instance attributes
#     def showdetails(self):
#         print(self.name,self.age)
#
# p1=Person('Ram',24)
# # print(p1.name,p1.age)  #objectname.attributename
# p1.showdetails()
# p2=Person('Brinet',20)
# # print(p2.name,p2.age)
# p2.showdetails()


# dynamic
class Person:
    #constructor method
    def __init__(self):
        self.name=input('Enter the Name:')
        self.age=int(input('Enter the Age:'))
    def showdetails(self):
        print(self.name,self.age)

p1=Person()
p1.showdetails()
p2=Person()
p2.showdetails()