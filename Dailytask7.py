# 1).wap to find a number is perfect number
# Perfect number is a positive integer that is equal to the sum of its positive divisors
n=int(input('Enter a number:'))
def divisor(n1):
  sum = 0
  for i in range(1,n1):
     if n1>0 and n1%i==0:
         sum=sum+i
  return sum
def perfect_number(n):
    if divisor(n)==n:
       print('perfect Number')
    else:
        print('Not a perfect number')
perfect_number(n)

# Aptitude
# The H.C.F. of two numbers is 23 and the other two factors of their L.C.M. are 13 and 14. The larger of the two numbers is:
# 276
# 299
# 322
# 345

# HCF=23
# Two factors of their LCM are 13 and 14
# so, 23*13=299 and 23*14=322
# Largest number is 322