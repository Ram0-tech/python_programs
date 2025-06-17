# Addition of two  numbers
# def add():
#     n1 = int(input('Enter a number:'))
#     n2 = int(input('Enter a number:'))
#     s = n1 + n2
#     print('Sum =', s)
#
#
# add()

# Factorial of a number
# def factorial():
#     n = int(input('Enter a number:'))
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     print('Factorial =', fact)
#
#
# factorial()

# def add(a,b):
#      "Addition of two numbers"  #docstring
#      sum = a + b
#      print(sum)
#
#
# n1 = int(input('Enter a number:'))
# n2 = int(input('Enter a number:'))
# add(n1, n2)

# using return stmnt
# def add():
#     n1 = int(input('Enter a number:'))
#     n2 = int(input('Enter a number:'))
#     sum = n1 + n2
#     return sum
#
#
# s = add()
# print(s)

# define a fn to calculate simple interest value
# p = int(input('Enter pricipal amount:'))
# n = float(input('Enter time period:'))
# r = int(input('Enter the rate of interest:'))
#
#
# def simple_intesest(p, n, r):
#     si = p * n * r / 100
#     return si
#
#
# print(simple_intesest(p, n, r))

# using multiple return value
# def arithmetic_op():
#     n1 = int(input('Enter the number:'))
#     n2 = int(input('Enter the number:'))
#     s=n1+n2
#     d=n1-n2
#     p=n1*n2
#     q=n1/n2
#     return s,d,p,q
# # result=arithmetic_op()
# # print(result)
# sum,diff,prod,quo=arithmetic_op()
# print(sum ,'\n',diff,'\n',prod,'\n',quo)

while True:
 print('Arithmetic operations', '\n', '1.Addition', '\n', '2.Subtraction', '\n', '3.Multiplication', '\n', '4.Division',
     '\n', '5.Exit')
# ch = int(input('Enter your choice:'))
# n1 = int(input('Enter the number:'))
# n2 = int(input('Enter the number:'))


def add(a, b):
  s = a + b
  print(s)


def diff(a, b):
  d = a - b
  print(d)


def mul(a, b):
  p = a * b
  print(p)


def div(a, b):
  q = a / b
  print(q)


ch = int(input('Enter your choice:'))
if ch in [1,2,3,4]:
 n1 = int(input('Enter the number:'))
 n2 = int(input('Enter the number:'))
if ch == 1:
   add(n1, n2)
elif ch == 2:
   diff(n1, n2)
elif ch == 4:
    div(n1, n2)
else:
    exit()

# Arbitary non keyword arguments
# def fun(*args):
#     # print(args)
#     #    OR
#     # for i in args:
#     #     print(i,end=" ")
#     # print()
#     # OR
#     print(args[0])
#
#
# fun('Arun')
# fun('Amal', 'Anu')
# fun('Vinu', 'Manu', 'Rinu')
# fun(1, 2, 3, 4, 5, 6)


# Arbitary  keyword arguments
def fun(**kwargs):
      print(kwargs)

fun(Alice=20,Manu=30)
fun(a=1,b=2,c=3)
fun(a=10,b=20,c=30,d=40)

# def fun(*a):
#     sum=0
#     for i in a:
#         sum+=i
#     print(sum)
# fun(10,20)
# fun(10,20,30,40,50)


