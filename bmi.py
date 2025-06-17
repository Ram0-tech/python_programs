h = float(input('Enter height in cm:'))
w = float(input('Enter weight in kg:'))
he = h / 100
bmi = w / he ** 2
print(bmi)
if bmi < 18.5:
    print('Underweight')
if 18.5 <= bmi <= 24.9:
    print('Normal')
if 25 <= bmi <= 29.9:
    print('Overweight')
if bmi > 40:
    print("Obesity")
    print('Morbid')
    if 35 <= bmi <= 39.9:
        print("Obesity")
        print('Moderate')
        if 30 <= bmi <= 34.9:
            print("Obesity")
            print('Mild')
else:
    print('Invalid input')
