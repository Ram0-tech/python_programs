# phone_book = {
# 'John' : [ '8592970000', 'john@xyzmail.com' ],
# 'Bob': [ '7994880000', 'bob@xyzmail.com' ],
# 'Tom' : [ '9749552647' , 'tom@xyzmail.com' ]
# }
# Extract all email addresses using map() function.
# print(list(map(lambda x:x[1],phone_book.values())))


# Python program to display all integers within the range 100-200 whose sum of digits is an even number
# s=0
# for i in range(100,200):
#     for j in str(i):
#       s+=int(j)
#     if s%2==0:
#      print(i)


# Write a program that prints the numbers from 1 to 100. But for multiples of 3, print "Fizz" instead of the number, for multiples of 5, print "Buzz", and for multiples of both 3 and 5, print "FizzBuzz".For multiples of 7, print "Bang".
# for i in range(1,100):
#     n=''
#     if i%3==0:
#        n+='Fizz'
#     if i%5==0:
#         n+'Buzz'
#     if i%3==0 and i%5==0:
#         n+='FizzBuzz'
#     if i%7==0:
#         n+='Bang'
#     print(n or i)


# To create a new list where each position contains the sum of the other two numbers in the original list
 # Example:
# l=[10,5,4]
# print([l[1]+l[2],l[0]+l[2],l[0]+l[1]])

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# for i in range(1,5):
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print()
#

# Given a string
# s="malayalam is a language"
# # a).count the number of words in a string
# # b).find the maximum length word
# # c).print the word if the word is palindrome.
# s1=s.split()
# print('number of words:',len(s1))
# print('maximum length of the word:',max(s1))
# print('palindrome words:')
# for i in s1:
#     if i==i[::-1]:
#      print(i)

# Define a function to find the BMI

# bmi=weight/(height/100)**2.(if weight in kg and height in cm).
# Using arguments and return statement.
# def b_m_i(w,h,):
#     bmi=w/(h/100)**2
#     return bmi
# bodymassindex=b_m_i(80,180)
# print('Bmi:',bodymassindex)
#

# Given a list
# vehicles = ['Car','Cycle','Bus','Tempo','Bike']
# a).print all vehicles
# b).print vehicle names starting with letter 'B'
# c).print all vehicles except the vehicle name with 'B'
# d).Iterate through the list elements and print each element. Exit from the loop if vehicle name =Bus.
# print(vehicles)
# for i in vehicles:
#     if 'B' in i[0]:
#         print(i)
# for i in vehicles:
#     if 'B'not in i:
#         print(i)
#         continue
#
# for i in vehicles:
#     print(i)
#     if 'Bus'==i:
#         break


# You have an array containing n-1 integers, where the integers are in the range of 1 to n. One number is missing. Find the missing number.
# Example:
# Input: [3, 7, 1, 2, 8, 4, 5]
# Output: 6
# l=[3,7,1,2,8,4,5]
# for i in l:
#     n=len(l)+1
#     e_sum=n*(n+1)//2
#     a_sum=sum(l)
#     m=e_sum-a_sum
# print(m)

# Define a function to print all prime numbers in the
# given list
# l=[23,12,11,56,74,80,36,39]
# n=len(l)
# def prime(num):
#     if num<2:
#         return 0
#     for i in range(2,num):
#         if num%i==0:
#             return 0
#     return 1
# for i in range(n):
#     if prime(l[i])==1:
#         print(l[i],"is prime")

num1 = 6
num2 = 3
if num1+ num2 != 10:
    not_ten = True

else:
    not_ten = False

    # Uncomment the below lines to show the result
print("Is the sum of the numbers not equal to 10? " + str(not_ten))
