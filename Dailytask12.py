# Daily task 12
# Coding question
# wap to check 'password',
# The user input should have following conditions:
# 1. At least one upper case letter
# 2. At least one lowercase letter
# 3. At least one number
#    4  At least one special character !@#$%^&*
# 5. Minimum 8 characters.
# Please note; if the entered word does not follow any of the above conditions then
# program should show a message what specific error was found.
# e.g.: If uppercase is missing then the message should be("Uppercase missing. Please re-enter")
# similarly lowercase letter, 8 characters etc.

import re

def check_password(password):
    errors = []

    if len(password) < 8:
        errors.append("Minimum 8 characters required.")

    if not any(char.isupper() for char in password):
        errors.append("Uppercase missing. Please re-enter.")

    if not any(char.islower() for char in password):
        errors.append("Lowercase missing. Please re-enter.")

    if not any(char.isdigit() for char in password):
        errors.append("Number missing. Please re-enter.")

    if not re.search(r"[!@#$%^&*]", password):
        errors.append("Special character missing. Please re-enter.")

    if errors:
        for error in errors:
            print(error)
    else:
        print("Password is valid!")
password = input("Enter your password: ")
check_password(password)

#apptitude question
# Given series:
# B2CD, _____, BCD4, B5CD, BC6D

# Answer:B2C3D