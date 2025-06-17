# Daily Task 9
#
# Coding
# Write a Python program to print a butterfly pattern.
N = int(input("number of rows"))
spaces = 2 * N - 1
stars = 0
for i in range(1, 2 * N):
    if i <= N:
        spaces = spaces - 2
        stars += 1
    else:
        spaces = spaces + 2
        stars -= 1
    for j in range(1, stars + 1):
        print("*", end="")
    for j in range(1, spaces + 1):
        print(" ", end="")
    for j in range(1, stars + 1):
        if j != N:
            print("*", end="")

    print()

# Aptitude
# A man buys an old scooter for Rs.4700 and spends Rs.800 on its repairs. If he sells the scooter for Rs 5800,his gain percent is:
#
# a.4  4/7%
# b. 5  5/11%
# c. 10%
# d. 12%
#ans=5*5/11%