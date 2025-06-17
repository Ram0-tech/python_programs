# Write a Python program to check if a string is an anagram or not
#
# Example:
#
# Input:
# Enter first word: listen
# Enter second word: silent
#
# Output:
# True
#
# Input:
# Enter first word: hello
# Enter second word: world
#
# Output:
# False
s1=input("enter the first word: ")
s2=input("enter the second word: ")
l1=set(s1)
l2=set(s2)
if l1==l2:
    print("True")
else:
    print("False")
# Aptitude Question:
#
# A shopkeeper offers a 15% discount on an item marked at £2000. What is the selling price?
#
# Options:
# A) 1700
# B) 21800
# C) 21900
# D) 1950
ans= 1700