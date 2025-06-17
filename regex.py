# findall()
# s='5623 12345678 9086 3456567 123 45677'
# #find all 3digit ,4 digit or 5 digit numbers
# import re
# a=re.findall(r'\b\d{3,5}\b',s)
# print(a)
from re import search, findall
#
# s='hello world:  _hello_world  2helloworld  :hello:world  hello?world   hello world'
# import re
# a=re.findall(r'\bhello\b',s)
# print(a)

# find all 3 letter ,4 letter or 5 letter words
# s='The quick brown fox jumps over the lazy dog'
# import  re
# a=re.findall(r'\b[a-zA-Z]{3,5}\b',s)
# print(a)

# search()
import re
# s='Hi world Hello python'
# a=re.search(r'Hello',s)
# if a:
    # print('Match found')
    # print(a) #match object reference only
    # print(a.group()) #matching word
    # print(a.span())  #starting and end position of matching word
    # print(a.start()) #starting position
    # print(a.end())   #ending position
# else:
#     print('No match found')

# match()
# s='Hi world Hello python'
# a=re.match(r'Hello',s)
# if a:
#     print('Match found')
# else:
#     print('Match not found')

# sub()
# s='john@abc.com and mike@pqr.com'
# import re
# a=re.sub(r'@[a-z]+','@gmail',s)
# print(a)

# split()
# import re
# s='python is a programming language'
# a=re.split(r'\s',s)
# print(a)
