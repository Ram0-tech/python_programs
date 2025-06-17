# for i in range(1,6):
#     print('Python')

# for i in range(1,11):
#     print('Hello Ram')

#print the series 1..100
# for i in range(1,101):
#     print(i,end=' ')

# #print the series 1,3,5,7,9
# for i in range(1,11,2):
#     print(i)

# print the series 2,4,6,8,10
# for i in range(2,11,2):
#     print(i)

# print the series 10,20,30,40,60,70,80,90
# for i in range(10,91,10):
#     print(i,end=' ')

# print the series 1,4,9,16,25,36,49,81,100
# for i in range(1,11):
#     print(i**2)

# print the series 4,9,14,19,24,29,34,39
# for i in range(4,40,5):
#     print(i)

# print the series 5,4,3,2,1
# for i in range(5,0,-1):
#     print(i)

# print the series 8,6,4,2,0
# for i in range(8,-1,-2):
#     print(i)

# # sum of 1..5
# sum = 0
# for i in range(1,6):
#     sum +=i
# print('Sum=',sum)

# product  of 1..5
# p = 1
# for i in range(1,6):
#     p *=i
# print('Product=',p)

# sum of cubes of numbers from 1-10
# s = 0
# for i in range(1,11):
#     s+=i**3
# print('Sum=',s)

# factorial
# n = int(input('Enter a number:'))
# fact =1
#
# for i in range(1,n+1):
#     fact*=i
# print(fact)

#factors
# n = int(input('Enter a number'))
#
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

#
# for i in range(200,501):
#     if i%3==0 and i%5==0:
#         print(i)


#in string
# s = 'hello python'
# for i in s:
#     print(i)

# in list
# l = [10,'hi',3.14]
# for i in l:
#     print(i)

# print those numbers that are divisible by 3 in the range(1,100)
# for i in range(1,100):
#     if i%3==0:
#         print(i)
# print those numbers that are divisible by 5 in the given sequence l=[10,43,23,90,18,16,78,34]
#print the count and sum
# l=[10,43,23,90,18,16,78,34]
# s=0
# c = 0
# for i in l:
#     if i%5==0:
#         s+=i
#         c+=1
#         print(i,end=' ')
# print()
# print('Sum=',s)
# print('Count=',c)

# print all the vowels   in the given string 'hello world'
# print the count of vowels
# s = 'hello world'
# v = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
# c = 0
# for i in s:
#     if i in v:
#         print(i)
#         c += 1
# print()
# print('Count of vowels=', c)

#print multiples of 5 in the range 100-200
# for i in range(100,201):
#     if i%5==0:
#         print(i,end=' ')
# print each characters in the given string s='python'
# s='python'
# for i in s:
#     print(i)
#print the even values in the given list l=[2,7,3,6,1,9]
# l=[2,7,3,6,1,9]
# for i in l:
#     if i%2==0:
#         print(i)
# print the even values in the given dictionary d={'a':10,'b':15,'c':80,'d':45,'e':31}

# d={'a':10,'b':15,'c':80,'d':45,'e':31}
# for i in d.values():
#     if i%2==0:
#         print(i)

# d={'a':10,'b':15,'c':80,'d':45,'e':31}
# for i,j in d.items():
#     print(i,j)