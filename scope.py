# global scope
# x = 10
# print(x)
# def fun():
#     print(x)
# fun()
#
# print(x)

# local scope
# def f():
#     x = 10 #can only be used inside the fn
#     print(x)
# f()
# print(x)  #error
#
# def f():
#     global x  #can access a local variable globally
#     x = 10
#     print(x)
#
#
# f()
# print(x)


# def f1():
#     global y
#     y = 10
#     print('inside',y)
#
#
# def f2():
#     x =20
#     print('inside',x)
#     print(y)
# f1()
# f2()


# nonlocal
# def f():
#     x =10
#     print('inside outer',x)
#     def f1():
#          print('inside inner',x)
#     f1()
# f()

#
# def f():
#     x =10
#     print('inside outer',x)
#     def f1():
#         nonlocal  x #for updation
#         x=x+1
#         print('inside inner',x)
#     f1()
# f()