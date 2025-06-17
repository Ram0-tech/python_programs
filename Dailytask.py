
# Daily Task 5:
# Problem: Given an unsorted list of integers, find the length of the longest consecutive sequence.
# Example:
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4  # (Sequence: [1, 2, 3, 4])
def longest_consecutive(l):
    l1=set(l) #{1,2,3,4,100,200}
    lc=0
    for i in l1:
        if i-1 not in l1:
            first=i
            while first+1 in l1:
                first+=1
            lc=max(lc,first-i+1)
    return lc
n=[100,4,200,1,3,2]
print(longest_consecutive(n))


# Aptitude:
# A train, 130 metres long travels at a speed of 45 km/hr crosses a bridge in 30 seconds. The length of the bridge is
#
# A) 235 metres
#
# B) 245 metres
#
# C) 270 metres
#
# D)  220 metres
# Hint: Convert the speed of the train from km/hr to m/s
# speed=45x(1000/3600)=25/2 m/s
# Time=30seconds
# Distance=130m
# Length of the bridge be l
# 130+l/30=25/2
# l=375-130
#  =245m