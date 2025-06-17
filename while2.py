# *print 'hello world' 10 times
# i = 1
# while i<= 10:
#     print('hello world')
#     i+=1
# print 1,2,3.......100
# i = 1
# while i<= 100:
#     print(i)
#     i+=1
# print 10,11,12,13.....20
# i = 10
# while i<= 20:
#     print(i)
#     i+=1
# print 1,3,5,7,9,11
# i = 1
# while i<= 11:
#     print(i)
#     i+=2
# print 2,4,6,8,10
# i = 2
# while i<= 10:
#     print(i)
#     i+=2
# print  10,20,30,40,50,60,70,80,100*
# i = 10
# while i<= 100:
#     print(i , end=' ')
#     i+=10
# print()


##print the squares of numbers from 100 -200

# i = 100
# while i<=200 :
#     print(i**2)
#     i+=1

#print the cubes of numbers from 1 to 50
# i = 1
# while i<=50 :
#     print(i**3, end=' ')
#     i+=1

# print the series 5,4,3,2,1
# i = 5
# while i>=1:
#     print(i)
#     i-=1

#print the series 4,9,14,19,24,29,34,39
# i = 4
# while i<=39:
#     print(i)
#     i+=5


#print the series 3,12,48,192,768,3072
# i = 3
# while i<=3072 :
#     print(i)
#     i*=4

#print the series 3,4,6,9,13
i = 3
j=1
while i<=13 :
    print(i)
    i = i+j
    j+=1


#print the series 100,200,300,....1000
# i = 100
# while i<=1000 :
#     print(i)
#     i+=100

# print those numbers which are divisible by 3 in the range(200-500)
# i = 200
# while i<=500:
#     if i%3==0:
#        print(i)
#     i+=1


#print thosse numbers which are divisible by 3 and 5 in the range(200-500)
# i = 200
# while i<=500:
#     if i%3==0 and i%5==0:
#        print(i)
#     i+=1

#print thosse numbers which are  divisible by 7 in the range(1-100)
# i = 1
# while i<=100:
#     if i%7==0:
#        print(i)
#     i+=1

#count of numbers which are divisible by 3 in the range (1-100)
# i =1
# count = 0
# while i<=100:
#     if i%3==0:
#        count+=1
#     i=i+1
# print('count:',count)

# count of numbers which are divisible by 7 and 5 in the range (1500-2700)
# i = 1500
# count = 0
# while i<=2700:
#     if i%7==0 and i%5==0:
#         count+=1
#     i+=1
# print('count',count)

# #sum of numbers in the range 1-10
# i = 1
# sum = 0
# while i <= 10:
#     sum += i
#     i += 1
# print('sum=', sum)

#sum of numbers in the range 200-400
# i =200
# s=0
# while i<=400:
#       s+=i
#       i+=1
# print(s)

#sum of squares of numbers from 1-10
# i = 1
# sum = 0
# while i <= 10:
#     sum += i**2
#     i += 1
# print('sum=', sum)

#sum of cubes of numbers from 1-20
# i = 1
# sum = 0
# while i <= 20:
#     sum += i**3
#     i += 1
# print('sum=', sum)

#sum of even  numbers from 1-100
# i = 2
# sum = 0
# while i <= 100:
#
#        sum +=i
#        i += 2
# print('sum=', sum)

#sum  and count of numbers that  are divisible by 3 in range 1-50
# i = 1
# s = 0
# c = 0
# while i<=50:
#     if i%3==0:
#         c+=1
#         s+=i
#     i+=1
# print(c)
# print(s)


#product of numbers from 1-10
# i = 1
# p = 1
# while i <= 10:
#     p *= i
#     i += 1
# print('product=', p)


#factorial
# n = int(input('Enter a number:'))
# i = 1
# fact = 1
# while i <= n:
#     fact *= i
#     i += 1
# print('Factorial=', fact)

#factor
# n = int(input('Enter a number:'))
# i = 1
# while i <= n:
#     if n % i == 0:
#         print(i)
#     i += 1


# print the series -12,-11,....12
# print the sum of even numbers
# print the count of even numbers
# i = -12
# sum =0
# count = 0
# while i<=12:
#     print(i)
#     if i%2==0:
#         sum +=i
#         count+=1
#     i+=1
# print('sum of even numbers',sum)
# print('count',count)

# print  each digit of a number
# n = 123
# s =str(n)
# for i in s:
#
#     print(i)
# OR

# while(n>0):
#     n1=n%10
#     print(n1)
#     n = n//10

# sum of digits in a number
# n = int(input('Enter a numnber'))
# s =0
#
# while n>0:
#     n1= n%10
#
#     s+=n1
#     n//=10
# print(s)