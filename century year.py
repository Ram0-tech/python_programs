y = int(input('Enter a year:'))
# if y % 100 == 0:
#     print("Century year")
# else:
#     print('Not a century year')
#
# result = 'Century year' if y % 100 == 0 else 'Non century year' # syntax: true expression if condition else false expression
# print(result)


#eg: positive or negative number
# n = int(input('enter a number:'))
# r = 'Positive number' if n>0 else 'Negative number'
# print(r)

# #f string example
# name = input('enter a name:')
# age = int(input('enter age:'))
# print(f'My name is {name} am {age} years old')

# account_number = 'XXXXXX2826'
# transaction_type = 'debited'
# payment_method = 'g-pay'
# amount = 190
# print(f'A/C {account_number} {transaction_type} by Rs {amount} towards {payment_method}')


#Leap year
year = int(input('Enter a year:'))
if year % 100 == 0 and year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    print(f'{year} is leap year')
else:
    print(f'{year} is not a leap year')
