#write a programm to reverse each lines in a file
from re import findall

# f=open("p.txt","r")
# s=f.readlines()
# s.reverse()
#
# g=open("p.txt","w+")
# # for i in s:
# #     f.write(i)
# g.writelines(s)
# g.seek(0,0)
# print(g.readlines())

#write a program to extract valid mobile  numbers from the given data
# s="My mobile numbers are 9906342436 and 8976512345"
# import re
# n=re.findall(r"\b[6789][0-9]{9}\b",s)
# print(n)



#check whether the entered number is valid mobile number
# n=input("enter the mobile number: ")
# import re
# m=re.findall(r"^[6789][0-9]{9}$",n)
# if m:
#     print("mobile number is valid")
# else:
#     print("mobile number is not valid")



# class Category:
#     def __init__(self):
#         self.cname=input("enter category name: ")
#     def showdetails(self):
#         print(self.cname)
# class Product(Category):
#     def __init__(self):
#         super().__init__()
#         self.pname=input("enter the product name: ")
#         self.desc=input("enter the product description: ")
#         self.quan=int(input("enter the quantity: "))
#         self.price=int(input("enter the price: "))
#     def showdetails(self):
#         super().showdetails()
#         print(self.pname,self.desc,self.quan,self.price)
#     def total_price(self):
#         print("total price=",self.quan*self.price)
#
#
# p=Product()
# p.showdetails()
# p.total_price()
