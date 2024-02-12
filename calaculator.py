# Create a calculator code in which i input the first number the second number and the operatorand it gives me the results
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
operator = input("Enter operator: ")
if operator == "+":
      print("Results is: ", x+y)
elif operator == "-":
      print("Results is: ", x-y)
elif operator == "*":
      print("Results is: ", x*y)
elif operator == "/":
      print("Results is: ", x/y)
else:
    print("Invalid operator")