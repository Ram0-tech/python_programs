#given a string
# s = 'python is a programming language'

# find the occurence of a specific character in the given string
# s = 'python is a programming language'
# ch = input('enter the character')
# print(s.count(ch))
# given a string
# s = 'python is a programming language'
# print words whose length is less than 5
# s = 'python is a programming language'
# a=s.split()
# for i in a:
#     if len(i)<5:
#         print(i)
# #


# given a string
# s = 'hello world'
# # find the position of particular character in the given string
# ch = input('enter the character')
# print(s.index(ch))
# find the common element
# l1 = [12,34,45,67,90]
# l2 = [56,23,34,78,12,55]
# s = set(l1)
# s1  =set(l2)
# print(list(s.intersection(s1)))

#     #or
# for i in l1:
#     if i  in l2:
#         print(i)

# given a dictionary
# d = {1: ['arun', 20000], 2: ['amal', 30000], 3: ['anu', 15000]}
# find maximum salary
# l = []
# for i in d.values():
#     l.append(i[1])
# print(max(l))

# given a list ,find maximum,minimum without using max, min fn
# l = [12, 34, 56, 67, 22]
# max = 0
# for i in l:
#     if i > max:
#         max = i
# print(max)
# min = l[0]
# for i in l:
#     if i < min:
#         min = i
# print(min)

# # given a string
# s = 'pyhton is a programming language'
# l = s.split()
# max = 0
# w = ' '
# for i in l:
#     if len(i) > max:
#         max = len(i)
#         w = i
# print(w)

# l =[1,1,1,2,3,3,5,5,5,6]
# find the occurence of each elemnt print o/p as dictionary
# d={}
#
# for i in l:
#     d[i]=l.count(i)
# print(d)