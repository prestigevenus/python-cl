temperature = 34

if temperature > 25 :
    print("it is hot")
else:

    print("it is cold")

#A programme that detemines the largest number among the programme
num1 = 78
num2 = 22
num3 = 65
if num1 >num2 and num1 >num3:
    print(num1 ,"is the largest number")
if num2 >num1 and num2 >num3:
        print(num2 ,"is the largest number")
else:
        print(num3 ,"is t he largest number")


# A programme that checks whether a number :
number = 10

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

#A programme that checks whether a number is prime
num = 13
if num > 1:
    for x in range(2, num):
        if num % x == 0:
            print("Not prime")
        else:
            print("the number is  prime")
            break
    else:
        print("the number is not a prime number")