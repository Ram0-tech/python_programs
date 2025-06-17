# 41)
# phone_book = {
# 'John' : [ '8592970000', 'john@xyzmail.com' ],
# 'Bob': [ '7994880000', 'bob@xyzmail.com' ],
# 'Tom' : [ '9749552647' , 'tom@xyzmail.com' ]
# }
# Extract all email addresses using map() function.
# print(list(map(lambda x:x[1],phone_book.values())))

# 42).Python program to display all integers within the range 100-200 whose sum of digits is an even number
#
# for i in range(100,201):
#     s=0
#     for j in str(i):
#         s+=int(j)
#     if s%2==0:
#         print(i)

# 43). Write a program that prints the numbers from 1 to 100. But for multiples of 3, print "Fizz" instead of the number, for multiples of 5, print "Buzz", and for multiples of both 3 and 5, print "FizzBuzz".For multiples of 7, print "Bang".
# 44).
# for i in range(1,100):
#     if i%3==0 and i%5==0:
#         print('FizzBuzz')
#     elif i%3==0:
#         print('fizz')
#     elif i%5==0:
#         print('Buzz')
#     elif i%7==0:
#         print('Bang')
#     else:
#         print(i)


# To create a new list where each position contains the sum of the other two numbers in the original list
# Example:
# l=[1,2,3]
# new=[5,4,3]
# s=sum(l)
# l1=[]
# for i in l:
#     l1.append(s-i)
# print(l1)


# 45).You have an array containing n-1 integers, where the integers are in the range of 1 to n. One number is missing. Find the missing number.
# Example:
# Input: [3, 7, 1, 2, 8, 4, 5]
# Output: 6
# l=[3, 7, 1, 2, 8, 4, 5]
# for i in range(1,9):
#     if i not in l:
#         print(i)


# 46).    1
#         2 1
#         3  2  1
#         4  3  2  1
# print the above pattern.
# for i in range(1,5):
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print()
# 47).Define a function to print all prime numbers in the
# given list
# l=[23,12,11,56,74,80,36,39]
# for i in l:
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)



# 48).Given a list
# vehicles = ['Car','Cycle','Bus','Tempo','Bike']
# a).print all vehicles
# b).print vehicle names starting with letter 'B'
# c).print all vehicles except the vehicle name with 'B'
# d).Iterate through the list elements and print each element. Exit from the loop if vehicle name =Bus.
# vehicles = ['Car','Cycle','Bus','Tempo','Bike']
# for i in vehicles:
#     print(i)
# for i in vehicles:
#     if 'B' in i[0]:
#         print(i)
#
# for i in vehicles:
#     if 'B'not in i:
#         print(i)
#         continue
# for i in vehicles:
#     # print(i)
#     if i=='Bus':
#        break
#        print(i)



# 49).Given a string
# s="malayalam is a language"
# a).count the number of words in a string
# b).find the maximum length word
# c).print the word if the word is palindrome.
# s="malayalam is a language"
# s1=s.split()
# print('no of words:',len(s1))
# print('maximum length word:',max(s1))
# print('palindrome words:')
# for i in s1:
#     if i==i[::-1]:
#         print(i)

# 50).Define a function to find the BMI
# bmi=weight/(height/100)**2.(if weight in kg and height in cm).
#
# Using arguments and return statement.
# def b_m_i(w,h):
#     bmi=w/(h/100)**2
#     return bmi
# weight=int(input('enter the weight:'))
# height=int(input('enter the height:'))
# b_m_i(weight,height)
# print(round(b_m_i(weight,height)))