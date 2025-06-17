# s=lambda x:x**2
# print(s(5))
import functools

# print the first element of a given list
# l = [1,2,3,4]
# x = lambda  l:l[0]
# print(x(l))


# print the name  value of dictionary
# d = {'name':'arun','age':23,'place':'ekm'}
# x = lambda d:d['name']
# print(x(d))

# print the square root of a number
# import  math
# s = lambda  x : math.sqrt(x)
# print(s(81))

# print length of a string
# s = lambda x:len(x)
# print(s('hello'))

# n = [1,2,3,4]
# n1 = []
# for i in n:
#     n1.append(i**2)
# print(n1)

# using map()fn
# n = [1,2,3,4]
# print(list(map(lambda x:x**2,n)))

# create a list which contains the  square root of each number
# l = [81,64,25,16]
# import math
# print(list(map(lambda x:math.sqrt(x),l)))

# given a dictinary
# d = [{'name':'arun','age':23},{'name':'anu','age':25},{'name':'amal','age':22}]
 # create a list with name values
# print(list(map(lambda x:x['name'],d)))

# create a list with length of each color values
# colors = ['red','green','orange','yellow']
# print(list(map(lambda x:len(x),colors)))

# l = [['abc','john',300,'english'],['stu','mike',350,'english']]
# extract authors name and create a new list
# print(list(map(lambda x:x[1],l)))

# using filter() fn
# even numbers
# n = [12,45,23,89,30]
# print(list(filter(lambda x:x%2==0,n)))

# extract color whose length is less than 5 and create a new list
# colors  = ['red','green', 'purple','blue']
# print(list(filter(lambda x:len(x)<5,colors)))

# create a new list that contains multiples of 3 and 5 in the given range(1,101,)
# n = range(1,101,)
# print(list(filter(lambda x:x%3==0 and x%5==0,n)))


# extract -ve values and create new list
# n = [12,30,-2,-11,67,-34]
# print(list(filter(lambda x:x<0,n)))

# extract the numbers that contains digit 3 from the range (100,200) and create a new list
# print(list(filter(lambda x:'3' in str(x),range(100,200))))

# using reduce() fn
# print sum
# n = [1,2,3,4]
# print(functools.reduce(lambda x,y:x+y,n))
