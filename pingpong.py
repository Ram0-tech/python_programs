#Read a number num
# display PING if num is / by 3
# display PONG if num is / by 5
# display PINGPONG if num is / by 15
num = int(input('Enter a number'))
if num % 15 == 0:
    print('PINGPONG')
elif num % 5 == 0:
    print('PONG')
elif num % 3 == 0:
    print('PING')