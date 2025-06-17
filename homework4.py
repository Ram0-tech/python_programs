# print fibonacci series
n = int(input('Enter a number:'))
# a = 0
# b = 1
# for i in range(n):
#     print(a, end=' ')
#     c = a + b
#     a = b
#     b = c

a,b = 0,1
for i in range(n):
    print(a,end=' ')
    a,b = b,a+b

# print the characters at even index position
# s = 'hello'
# for i in range(0, len(s), 2):
#     print(s[i])





# l=[]
# count = int(input('Enter the count:'))
# for i in c:
