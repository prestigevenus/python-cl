try:
    print(x)
except:
     print("NameError occured")


try:
    num1 = 20
    num2 = 10
    print(num1 / num2)
except:
    print("ZeroDivisionError occured")


# User_defined function
try:
    def sum(first, second):
        return first + second
except:
    print("Exception occured")

finally:
    print("success")
print(sum(10, 20))