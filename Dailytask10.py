# Daily_Task_10
# Write a Python program to find the second-largest number in a given list of integers.
# input numbers = [12, 45, 1, 78, 23, 90, 67]
# Second-largest number: 78
# Constraints:
# 1)The list will contain at least two distinct numbers.
# 2)The numbers can be positive or negative.
# 3)solve without using sorting
l=[12, 45, 1, 78, 23, 90, 67]
l1=set(l)
l1.remove(max(l1))
second_largest =max(l1)
print('second largest number:',second_largest)
#
#
# Aptitude Question:
# Two trains, Train A and Train B,
# start from two different stations Thiruvananthapuram and Kasaragod,
# which are 600 km apart,
# and move towards each other at 8:00 AM.
# Train A has a speed of 80 km/h, and Train B has a speed of 120 km/h.
# Find:
# At what time will the two trains meet?
# Options:
# (A) 10:00 AM
# (B) 10:30 AM
# (C) 11:00 AM
# (D) 11:30 AM
# Speed=80+120=200km
# Distance=600km
# Time=600/200=3+8=11AM
