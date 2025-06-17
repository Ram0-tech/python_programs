# # 41).Write a Python Program to Sort Words in Alphabetic Order.
# s="python is a programming language"
# s1=s.split()
# s1.sort()
# print(s1)
#
# # 42).Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# # The numbers obtained should be printed in a comma-separated sequence on a single line.
# #
# # output
# # 2000, 2002, 2004, 2006, 2008, 2020, 2022, 2024, 2026, 2028, 2040, ...
# for i in range(1000,3001):
#     if i%2==0:
#         print(i,end=",")


# 47).Define a function to print all prime numbers in the
# given list
# l=[23,12,11,56,74,80,36,39]
# for i in l:
#     n=i
#     if(n>1):
#         for i in range(2,n):
#             if(n%i==0):
#                 print(n,"not a prime number")
#                 break
#         else:
#              print(n,"is a prime number")
#     else:
#         print(n,"is not a prime number")


# 43). Write a Python program that finds and prints all "special numbers" between 100 and 500. A number is considered "special" if:
#
# It is divisible by 7 or ends in 7.
# It does not contain the digit 3 anywhere in the number
# for i in range(100,501):
#     if i%7==0 or "3" not in str(i) or str(i)[-1]==7:
#         print(i)
#

#5).Write a Python Program to Find Armstrong Number in an Interval
a=int(input("enter the starting of the range"))
b=int(input("enter the end of the range"))
for i in range(a,b):
    n=i
    s=str(n)
    a=len(s)

    sum=0
    for i in s:
        sum=sum+int(i)**a
    if(n==sum):
        print(n,"is a armstrong number")

