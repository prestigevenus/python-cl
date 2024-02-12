# Inbuilt functions
number = max(34, 78, 90, 123, 45)
print(number)

y = min(45, 78, 34, 23)
print(y)

z = pow(2, 3)
print(z)


# User_defence function
def name():
    print("prestige")


name()  # calling a function


def details():
    name = "Prestige"
    age = 18
    course = "MIT"
    print(name, age, course)


details()  # calling a function


# Parameters/variables and arguments/valuables
def patients(name, gender, age, MarriageStatus):
    print(name, age, gender, MarriageStatus)


patients("job", "female", "32", "single")
patients("Mary", "female", "67", "married")


def multiply(x, y):
    print(x * y)


multiply(2, 6)
multiply(30, 6)
multiply(21, 16)
multiply(15, 3)


# Create a user_defined function
# Called employees. Display details of
# five employees using the
# following parameters: fullname,age,
# position,salary

def employees(fullname, age, position, salary):
    print(fullname, age, position, salary)


employees("joe tom", 30, "manager", 20000)
employees("billy", 70, "director", 40000)
employees("tom cruise", 40, "steward", 50000)
employees("karan ruthra", 50, "manager", 30000)
employees("marktom", 60, "manager", 70000)


