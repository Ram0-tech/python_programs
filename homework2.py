#1. l=['kelly','jenny','emi']
#Output:
#kelly kelly kelly
#jenny jenny jenny
#emi    emi   emi
# l=['kelly','jenny','emi']
# for i in l:
#     for j in l:
#         print(i,end=' ')
#     print()


#2
# serial_no=[1,2,3]
# qns=['what','why','when']
# #Output:
# 1.
# what
# when
# why
# 2.
# what
# why
# when
# 3.
# what
# why
# when

# serial_no=[1,2,3]
# qns=['what','why','when']
# for i in serial_no:
#     print(i, '.')
#     for j in qns:
#         print(j)


# 3.d={1:['lion','tiger','horse'],2:['cat','dog','cow']}
# Output
# lion
# tiger
# horse
# cat
# dog
# cow

# d={1:['lion','tiger','horse'],2:['cat','dog','cow']}
# for i in d:
#     for j in d[i]:
#         print(j)


# 4.print Pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# num=1
# for i in range(1,5):
#    for j in range(i):
#     print(num,end=" ")
#     num +=1
#    print()

# 5.
# 1
# 4 4
# 9 9 9
# 16 16 16 16
# for i in range(1,5):
#     for j in  range(1,i+1):
#         print(i**2,end=' ')
#     print()


# print all prime numbers in the given list
# l=[23,45,67,12,80,34]
# for i in l:
#      if i>1:
#       for j in range(2,i):
#          if i%j==0:
#              break
#       else:
#           print(i)

# print all prime numbers in the range(1,100)
# for i in range(1,100):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i,end=' ')

# A
# B B
# C C C
# D D D D
# n =65
# for i in range(1,5):
#     for j in  range(1,i+1):
#         print(chr(n),end=' ')
#     n+=1
#     print()

# A
# B C
# D E F
# G H I J
# n =65
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(n),end=' ')
#         n+=1
#     print()

# A
# A B
# A B C
# A B C D
# for i in range(1,5):
#     n = 65
#     for j in range(1,i+1):
#         print(chr(n),end=' ')
#         n+=1
#     print()

#         *
#       *   *
#     *   *   *
#   *   *   *   *
# *   *   *   *   *
n = 5
k = 4*2
for i in range(1,n+1):
    for p in range(1,k+1):
        print(end=' ')
    k-=2
    for j in range(1,i+1):
        print('*',end='   ')
    print()

# inverted pyramid
# k = 4*2
# for i in range(4,0,-1):
#     for p in range(1,k+1):
#         print(end=' ')
#     k+=2
#     for j in range(1,i+1):
#         print('*',end='   ')
#     print()


# n= 5
# k = 4*2
# for i in range(1,n+1):
#     for p in range(1,k+1):
#         print(end=' ')
#     k-=2
#     for j in range(1,i+1):
#         print('*',end='   ')
#     print()
# k=2
# for i in range(4,0,-1):
#     for p in range(1,k+1):
#         print(end=' ')
#     k+=2
#     for j in range(1,i+1):
#         print('*',end='   ')
#     print()
k =5*2
for i in range(1,6,2):
     for p in range(1,k+1):
         print(end=' ')
     k-=2
     for j in range(1,i+1):
         if j%2!=0:
             print(1,end=' ')
         else:
             print('A',end=' ')
     print()