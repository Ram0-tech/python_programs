# n1=int(input("Enter the number"))
# n2=int(input("Enter the number"))
# d=n1/n2
#
# print('Result',d)

# EXCEPTION
# try:
#     n1=int(input("Enter the number:"))
#     n2=int(input("Enter the number:"))
#     d=n1/n2
#
#
# except:
#     print("Division By zero is not possible")
# else:
#     print('Result:', d)


try:
    n1=int(input("Enter the number"))
    n2=int(input("Enter the number"))
    d=n1/n2

except ZeroDivisionError as e:
    #print("Division By zero is not possible")
    print(e)
except ValueError as s:
    # print("Value Error")
    print(s)
except Exception as s:
    #print("Error")
    print(s)

else:
    print('Result', d)
finally:
    print('hello')  #code will  always execute regardless of whether exception occurs or not