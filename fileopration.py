# read mode
# f=open('k.txt','r') #if file exists it will reference to f, else it will raise an error
# # s=f.read()
# print(f.read())

#  write mode
# f=open('p.txt','w')  #if p.txt exists,it will erase the content inside the file and sends reference to f.  else it will create a new file and sends reference to f
# f.write('hello')

# append mode
# s=open('p.txt','a')
# s.write('\nPython')

# s=open('k.txt','r')
# print(s.read(5))
# print(s.readline())
# # print(s.readlines()) #reads the complete file from beginning to end,but returns list of all lines from the file
# print(len(s.readlines()))  #reads the no of lines
# f=open('p.txt','a')
# a=s.read()
# f.write(a)


# s = input('enter a word:')
# f = open('k.txt', 'r')
# a = f.read()
# if s in a:
#     print('word found')
# else:
#     print('not found')

# write program to find no of letters, no of digits, no of space in a file
# c1=0
# c2=0
# c3=0
# f=open('y.txt','r')
# a=f.read()
# for i in a:
#     if i.isalpha() :
#         c1+=1
#     elif i.isdigit() :
#         c2+=1
#     elif i.isspace() :
#         c3+=1
# print('No of letters:',c1)
# print('No of digits:',c2)
# print('No of spaces:',c3)

# f=open('p.txt','a+')
# f.write('\nworld')
# f.seek(0,0)
# print(f.read())

#1.file read
# 2.write
# 3.append
# 4.search
# 5.delete
# while True:
#     print('File operations:\n', '1.File read\n', '2.File write\n', '3.File append\n', '4.File search\n',
    #       '5.File delete\n')
    #
    #
    # def file_read():
    #     try:
    #         x = open(f, 'r')
    #         print(x.read())
    #     except FileNotFoundError:
    #         print('File does not exist!!!')
    #     else:
    #         pass
    #
    #
    # def file_write():
    #     x = open(f, 'w')
    #     s = input('Enter the words:')
    #     x.write(s)
    #
    #
    # def file_append():
    #     x = open(f, 'a')
    #     s = input('Enter the words: ')
    #     x.write(s)
    #
    #
    # def file_search():
    #     try:
    #         s = input('Enter the word:')
    #         x = open(f, 'r')
    #         a = x.read()
    #         if s in a:
    #             print('word found')
    #         else:
    #             print('word not found')
    #     except FileNotFoundError:
    #         print('File does not exist!!!')
    #     else:
    #         pass
    #
    #
    # def file_delete():
    #     try:
    #         import os
    #         os.remove(f)
    #         print('File', f, 'is deleted')
    #     except FileNotFoundError:
    #         print('File does not exist!!!')
    #     else:
    #         pass
    #
    #
    # f = input('Enter the file name:')
    # ch = input('Enter the choice:')
    # if ch == '1':
    #     file_read()
    # elif ch == '2':
    #     file_write()
    # elif ch == '3':
    #     file_append()
    # elif ch == '4':
    #     file_search()
    # elif ch == '5':
    #     file_delete()
    # else:
    #     print('Invalid choice!!!')
    #     exit()

