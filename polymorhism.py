#in class
#polymorphism allows different classes to have
#same function with different implementation
#eg
# class A:
#     def f1(self):
#         print('in class A')
# class B:
#     def f1(self):
#         print('in class B')
# class C:
#     def f1(self):
#         print('in class C')


# in inheritance class
# class A:
#     def f1(self):
#         print('in class A')
# class B(A):
#     def f1(self):
#         print('in class B')
# b=B()
# b.f1()



# in same class   #method overloading
class A:
    def f1(self):
        print('in fn 1')
    def f1(self,a):
        print('in fn 2')
    def f1(self,a,b):
        print('in fn 3')
a=A()
a.f1()
a.f1(10)
a.f1(20,30)      #python does not support this method#

