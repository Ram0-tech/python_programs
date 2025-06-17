# N th value of a Fibonacci series..
# 1=0
# 2=1
# 3=1
# 4=2
# .
# .


n = int(input("enter the position to be displayed"))
a, b = 0, 1
for i in range(n - 1):
    a, b = b, a + b
print(a)

# Aptitude :
# A man plan to cover the distance of 6 km in 84 minutes. He decided to cover Two-third of tha distance in 4kmph and the remaining at some different speed.find the speed After the two- third distance is covered?
#
# Options
#
# A. 6.5 kmph
#
# B. 6 kmph
#
# C . 5.3 kmph
#
# D. 5 kmph
#
#
# Hint : convert minutes to hours
#
# 2/3 of 6 = 4
# time = 4/4 = 1hr
# remaining km = 2km
# remaining time = 24/60=.4
# speed = 2/.4=5kmph
