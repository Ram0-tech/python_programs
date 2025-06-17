# Generate  Pascal’s Triangle
# Hint: Use Binomial Expansion
import math
n = int(input('Enter the no of rows:'))
k=n*2
for i in range(n+1):
    for p in range(1, k + 1):
        print(end=' ')
    k -= 1
    for j in range(i+1):
        a = math.factorial(i)/(math.factorial(i-j)*math.factorial(j))
        print(int(a), end=' ')
    print()
# Aptitude Question
# A vessel is filled with liquid, 3 parts of which are water and 5 parts syrup.How much of the mixture must be drawn off and replaced with water so that the mixture may be half water and half syrup?
# a)      1 / 3
#
# b)      1 / 4
#
# c)      1 / 5
#
# d)      1 / 7