# n = int(input('Enter a number:'))
# if n > 0:
#     if n % 2 == 0:
#         print(n, 'Positive even  number')
#     else:
#         print(n, 'positive odd number')
# elif n<0:
#     if n % 2 == 0:
#         print(n, 'negative even  number')
#     else:
#         print(n, 'negative odd  number')
# else:
#     print('number is 0')

#check the given number is
# divisible by 2 and not divisible by 3
#divisible by 2 and divisible by 3
# not divisible by 2 and  divisible by 3
#not divisible by 2 and not divisible by 3
n = int(input('Enter a number'))
if n %2 ==0:
    if n%3==0:
     print('divisible by 2 and 3')
    else:
        print('dvisible by 2 and not by 3 ')
else:
    if n%3 ==0:
      print('not divisible by 2 and divisible by 3')
    else:
        print('not divisible by 2 and 3')