# # list comprehension
# n = [1, 2, 3, 4]
# new = [i ** 2 for i in n]
# print(new)
#
# new = [5 for i in n]
# print(new)
#
# new = ['hello' for i in n]
# print(new)
#
# # with condition
# print([i ** 2 for i in n if i % 2 == 0])
#
# new = [i ** 2 for i in n if i % 3 == 0]
# print(new)
#
# fruits = ['banana', 'apple', 'orange', 'cherry', 'pineapple']
# # a.creating a new list sequence with elements which contains letter 'n'
# print([i for i in fruits if 'n' in i])
# # b,creating a new list sequence with reverse of each elements
# print([i[::-1] for i in fruits])
# # c.creating a new list sequence with elements whose length greater than 6
# print([i for i in fruits if len(i) >6])
#
# l = [56, 12.6, 45, 90, -6, 34.8, -5, -12, 'hello', 'python']
# # creating a new list sequence with only floating point values
# print([i for i in l if type(i) == float])
# # creating list with only positive values
# print([i for i in l if type(i) == float or type(i) == int and i > 0])
#      # or
# print([i for i in l if type(i) !=str  and i > 0])
# # creating a list with only string types
# print([i for i in l if type(i) == str])
# # creating a list with elements whose value is divisible by 3 in the range(1,100)
# print([i for i in range(1, 100) if i % 3 == 0])
#
# # with set comprehension
# n = [1,2,3,4]
# new={i**2 for i in n}
# print(new)
#
# n = [1,2,3,3,4,5,6,6,6]
# print({i**3 for i in n})
#
# # with dictionary comprehension
# n = [1,2,3,4]
# print({i:i**2 for i in n})
#
# s='hello'
# print({i:s.count(i) for i in s})

# import module
# import scope
# scope.f()




# create a list which contains the sqaure root of each element from the given sequence
# import math
# l=[81,9,25,16,64]
# l1=[]
# for i in l:
#     # math.sqrt(i)
#     l1.append(int(math.sqrt(i)))
# print(l1)
#   OR
# print(list(map(lambda x:int(math.sqrt(x)),l)))
#  OR
# print([math.isqrt(i) for i in l] )