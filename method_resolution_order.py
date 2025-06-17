class A:
    def __init__(self):
        print('A')
class B(A):
    def __init__(self):
        super().__init__()
        print('B')
class C(A):
    def __init__(self):
        super().__init__()
        print('C')
class D(B,C):
    def __init__(self):
        super().__init__()
        print('D')
d=D()

#D-->B-->C-->A(method resolution order)
# first it calls __init__() inside D class
#then it calls __init__() inside first parent of D(ie.B)
# from B class __init__() it calls super().__init__() that means C class __init__()
#from C class _init() it calls super().__init__() that means A class _init_()
#In A class it prints A,then it prints C,then it prints B,and then it prints D
#this order of execution is called method resolution order