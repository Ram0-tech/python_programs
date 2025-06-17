# # Check whether a number is prime or not
# n = int(input('Enter a number:'))
# if n > 1:
#     for i in range(2, n):
#         if n % i == 0:
#             print('Not a prime number')
#             break
#     else:
#         print('Prime number')
# else:
#     print('Not a prime number')



# Check whether a number is Armstrong number or not
# n = int(input("Enter a number: "))
# a = str(n)
#
# sum = 0
# l = len(a)
#
# for i in a:
#
#     sum += int(i) ** l
#
# if sum == n:
#     print('Armstrong Number')
# else:
#     print('Not an  Armstrong Number')
# #
#
# Check whether a string is Palindrome or not (without slice)
# s = input('Enter a string:')
# rev = ''
# for i in s:
#     rev = i + rev
# if s == rev:
#     print('Palindrome')
# else:
#     print('Not palindrome')


# Count the occurrence of each character in a string
#
# For eg
# S=hello
#
# h 1
# e 1
# l 2
# # o 1
# #
s = input('Enter a string:')
d ={}
for i in s:
    if i!=' ':
     if i not in d:
        d[i]=1
     else:
        d[i]+=1
for i,j in d.items():
 print(i,j)


# find the occurrence of a specific character in a string
# s = input('Enter a string:')
# ch = input('Enter a character:')
# count = 0
# for i in s:
#     if i==ch:
#         count+=1
# print(count)

# i = 1
# while i<10:
#     print(i)
#     if i==4:
#         break
#     i+=1
# else:
#     print('hello')

# for i in range(1,10):
#     print(i)
#     if i==4:
#         break
# else:
#     print('hello')


# print all prime numbers in the given list
# l=[23,45,67,12,80,34]
# for i in l:
#      if i>1:
#       for j in range(2,i):
#          if i%j==0:
#              break
#       else:
#           print(i)

