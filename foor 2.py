# l = [1,2,3,4,5,6]
# new=[]
# for i in l:
#     new.append(i**2)
# print(new)
#
# l = [1,2,3,4,5,6]
# new=set()
# for i in l:
#     new.add(i**2)
# print(new)

#reverse a string
# s = 'hello'
# rev=''
# for i in s:
#     rev=i+rev
# print(rev)

#given  a list l=[45,26,89,12,91,51]
#create  two lists from given list ,one list for even numbers and second list for odd numbers
# l=[45,26,89,12,91,51]
# even=[]
# odd=[]
# for i in l:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

#given a list l=['red',3.4,90,12,6.5,'abc']
#craete 3lists(for each type) from given list and count of each type
# l = ['red', 3.4, 90, 12, 6.5, 'abc']
# l1 = []
# l2 = []
# l3 = []
# for i in l:
#     if type(i) == int:
#         l1.append(i)
#     elif type(i) == str:

#         l2.append(i)
#     elif type(i) == float:
#         l3.append(i)
#     else:
#         pass
# print(l1)
# print(len(l1))
# print(l2)
# print(len(l2))
# print(l3)
# print(len(l3))

#multiplication table
# n = int(input('Enter a  number:'))
# for i in range(1,11):
#     print(i,'x',n,'=',i*n)


#remove duplicates
# l=[1,1,2,2,3,3,4,4,5,6,7]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)

# s='hello world'
# s1=' '
# for i in s:
#     if i not in s1 and i!=' ':
#        s1= s1+i
# print(s1)

#print the country  name end with land
# d={'country1':'India','country2':'Myanmar','country3':'Newsland','country4':'Iceland','country5':'England'}
# for i in d.values():
#     if 'land' in i:
#         print(i)
