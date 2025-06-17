# Daily Task 6:
# Print the pattern
n=65
h=2*5
for i in range(1,6):
    for q in range(1,h+1):
        print(end=" ")
    h-=2
    for j in range(1,i+1):
        print(chr(n),end="   ")
        n+=1
    print()
k=3
a=80
for i in range(4,0,-1):
    for p in range(1, k+1):
        print(end=" ")        
    k=k+2
    for j in range(1,i+1):
        print(chr(a),end='    ')
        a+=1
    print()

# Aptitude
# A train 240 meters long is running at a speed of 72 km/h. How much time will it take to cross a platform 160 meters long?
# A) 20 seconds
# B) 25 seconds
# C) 30 seconds
# D)35seconds
# speed=72*(1000/3600)=20m/s
# Distance=240+160=400m
# Time=400/20=20s