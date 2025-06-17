def prime_number(num):
    if num==0 or num==1:
        print(num," is not prime")
    elif num>1:
        for i in range(2,num):
            if num%i==0:
                print(num," is not a prime number")
                break
        else:
            print(num,"is  prime number")
    else:
        print(num ,"is not prime" )
    return num
n=int(input("enter a number:"))
prime_number(n)