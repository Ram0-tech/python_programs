# Daily Task -1

# Coding
#
# 1. Ask user for input about car details
# 	1. Need at least preferably (3 or more) car details. Each car should have the details given below
# 		1. Car Brand
# 		2. Car Model
# 		3. Purchased Year
# 			1. This is fixed to 2020
# 		4. Total KM Travel
# 		5. Mileage
# 2. print the unique car brands
# 3. Print the details as dictionary
# 4. Find and print how much fuel each car have approximately used Total KM/Mileage .
# 	1. The result should be sorted based on the fuel efficiency.
# 		1. Only Need Car Model and the total fuel used should be in result.
# 5. Print the Least fuel efficient car
l = []
count = int(input('Enter the count:'))
for i in range(count):
    brand = input('Enter the car brand')
    model = (input('enter the car model'))
    py = 2020
    tkml = float(input('Enter the km:'))
    mileage = float(input('Enter mileage'))
    l.append( {'Car brand': brand, 'model': model, 'purchased year': py, 'total km traveled': tkml, 'mileage': mileage})

unique = []
for i in l:
    if i['Car brand'] not in unique:
        unique.append(i['Car brand'])
print('Unique car brand:', unique)

for i in l:
    print(i)

least = l[0]['mileage']
a =l[0]
for i in l:
    if i['mileage']<least:
      least=i['mileage']
      a = i
print('least fuel efficient car')
for key,value in a.items():
    print(f'{key}:{value}')



# Aptitude
#
# A can do a work in 15 days and B in 20 days. If they work on it together for 4 days, then the fraction of the work that is left is :
#
# A. 1/4
#
# B. 1/10
#
# C. 7/15
#
# D. 8/15
# A  =1/15
# B = 1/20
# fraction of work left= (60-28)/60 = 8/15