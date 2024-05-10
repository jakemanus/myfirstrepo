# Functions are named blocks of code that can be invoked at any other point during the execution of the program
# Like a loop a function allows code to be run multiple times over the course of a program
# Functions can both accept data prior to running (parameters) and return data after execution

# The following imports the datetime library
import datetime


# Print is actually a function. It's a built-in function
print("The Print() command is actually a function! The parenthese are a clue.")

# The following defines a function 'def' tells pyton you are defining a function. It just defines or creates the function, It doesnt actually run until you call it later
# dt is a variable storing the current date and time. dt.hour is the hour value of the current date and time
def greet():
    #Get the current time
    dt = datetime.datetime.now()

    if dt.hour <= 11:
        greeting = 'morning'
    elif dt.hour <= 17:
        greeting = 'afternoon'
    else:
        greeting = 'night'

    print("Hello, good " + greeting + ".")


# This is an example of calling the function defined earlier^^^
greet()

# We could then run a bunch of other stuff here
now = datetime.datetime.now()
current_time = now.strftime("%H:%M")

print("The current time is : " + str(current_time))

# And then call the function again
greet()

