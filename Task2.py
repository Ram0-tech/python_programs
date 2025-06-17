# Calculate Fare
# Fare Conditions:
# Up to 5 km → ₹10 per km
# 6 to 15 km → ₹8 per km
# 16 to 30 km → ₹6 per km
# Above 30km → ₹5per km
# d = int(input('enter the distance: '))
# if d<=5:
#     print('fare:',d*10,'Rs')
# elif d>=6 and d<=15:
#     print('fare:', 5 *10 +(d - 5) *8,'Rs')
# elif d>=16 and d<=30:
#     print('fare:', 5 *10 + 10*8+(d - 15) *6,'Rs')
# elif d>30:
#     print('fare:', 5 *10+8*10+6*15 +(d - 30) *5,'Rs')
# else:
#     print('Invalid input!!!')
# A toy vendor supplies three types of toys:

# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

# print('Name of Toys: \n 1.Battery based toys', '\n 2.Key-based toys', '\n 3.Electrical charging based toys')
# product_code = int(input('Enter product code:'))
# order_amount = float(input('Enter order amount:'))
# if product_code == 1:
#     if order_amount > 1000:
#         actual_price = order_amount-(order_amount*10/100)
# elif product_code == 2:
#     if order_amount > 100:
#         actual_price = order_amount - (order_amount *5/100)
# elif product_code == 3:
#     if order_amount > 500:
#         actual_price = order_amount-(order_amount*10/100 )
# else:
#     print('Invalid product')
#
# print('Payment after discount:',actual_price)
