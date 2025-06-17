#print the series
# 3,6,9,12,15,....30
# for  i  in range(3,31,3):
#     print(i,end=' ')

# print the pattern
# 2
# 22
# 222
# 2222
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(2,end=' ')
#     print()


#print the pattern
# p
# py
# pyt
# pyth
# pytho
# python
# s='python'
# l = len(s)
# for i in range(l):
#     for j in range(i+1):
#         print(s[j],end=' ')
#     print()

#Given a list of fruits=['orange','banana','apple','pineapple','avocado']
# print the first fruitname starting with letter 'a'
# fruits=['orange','banana','apple','pineapple','avocado']
# for i in fruits:
#      if 'a' in i[0]:
#         print(i)
#         break
# #print
# 1  - 49
# 2  - 48
#
# -
# 49 - 1

# for i in range(1, 50):
#     print(i, '-', 50 - i)

# #Check whether a number is spy number.Spy number means sum of digits equal to product of digits
# for eg:1124

n =int(input('Enter a number:'))
# s =0
# p = 1
# while n >0:
#     n1 = n%10
#     s+=n1
#     p*=n1
#     n=n//10
# if s==p:
#      print('spynumber')
# else:
#     print('not a spy number')

      # OR
# n = int(input(('Enter a number:')))
# s =0
# p = 1
# for i in str(n):
#     s+=int(i)
#     p*=int(i)
# if s == p:
#     print('spynumber')
# else:
#     print('not a spy number')

