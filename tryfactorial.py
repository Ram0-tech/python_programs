# import math
# while True:
#     try:
#         n=int(input('Enter a number'))
#         f=math.factorial(n)
#     except ValueError :
#         print('please enter a valid integer!!')
#     else:
#         print(f)
#         exit()
# #
# OR
import math


def fact():
    try:
        n = int(input('Enter a number'))
        f = math.factorial(n)
    except ValueError:
        print('please enter a valid integer!!')

    else:
        print(f)


fact()
