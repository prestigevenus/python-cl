# Data Type

number = 67 # int
num =78.98 # float
greting = "Hello there" #str
IsPythonIntresting = True #bool


# A variable storing multiple values
languages = ["python","PHP","JAVA"] # list
fruits = ("banana","apple","pineapple") # tuple
countries = ("china","Kenya","North America") # sets


# Dictionary
details = {
    "firstname":"Brian",
    "age" : 17,
    "course": "MIT",
    "nationality": "USA"
}

print(number)
print(IsPythonIntresting)
print(countries)
print(fruits)
print(details)
print(details["course"])
print(details["nationality"])

#Determining the data type
print(type(details))
print(type(countries))
print(type(languages))


#Typecasting - Converting one data type to another
print(float(number))
print(int(num))

