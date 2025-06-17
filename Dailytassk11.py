# Task 11
# ********
# coding
# -Write a Python program to find the first non-repeating character in a string
# Example Outputs:
# ✅ Input: "swiss" → Output: 'w'
# ✅  Input: "aabbcc" → Output: "No non-repeating character found."
s=input('enter a word:')
d={}
for i in s:
    if i!=' ':
     if i not in d:
        d[i]=1
     else:
        d[i]+=1
for i in s:
    if i!=' 'and d[i]==1:
        print('First non-repeating character:',i)
        break
else:
    print('Non-repeating character not found!!!')


# Aptitude Question
# *******************
# -A person walks a certain distance at 5 km/h and returns at 4 km/h.
# If the total time taken for the journey is 4.5 hours, find the distance one way.
# Options:
# A) 8 km
# B) 10 km
# C) 12 km
# D) 15 km
# Let`s take distance as x
# x/5+x/4=4.5
#      =9x=90
#      =x=10
# i.e,distance=10km