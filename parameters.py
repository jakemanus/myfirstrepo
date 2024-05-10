import datetime

print("Hello there this is being passed into the print() function!")

text = "Hi, this is stored in a string variable."
print(text)

# Here we see a concept of "variable scope" demonstrated. The variable "name" is only available inside the "greet" function. This is also true of the variable "greeting"
def greet(name):
    #Get the current time
    dt = datetime.datetime.now()

    if dt.hour <= 11:
        greeting = 'morning'
    elif dt.hour <= 17:
        greeting = 'afternoon'
    else:
        greeting = 'night'

    print("Hello " + name + ", good " + greeting + ".")

# Creating a variable and calling the input function to prompt for user input
username = input("What is your name? ")

# Here we call the greet function and pass the "username" variable into the function. This gets set as the "name" variable within the function itself.
greet(username)
# Here are some examples of just passing str values into the greet function that then set the value of the "name" variable within the function to the str value.
greet("Joe")
greet("Jane")

# This demonstrates that the name variable is not defined because it's scope is within the above function
print(name)