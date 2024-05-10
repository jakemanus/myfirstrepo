# A class is like your own custome data type
# Can represent complex 'objects' or ideas
# A class is like a architectural blueprint for a house, it's not the house itself, it's just a description of how to create a house
# The house in this metaphor would be 'objects' 
#
#       State - Properties/Variables
#       Behavior - Methods/Functions
#

# Here we create a class called circle. It's like a function just has a ":" following the ()
class Circle():
# Here indented inside the class definition, we define the state "radius" and the behavior "calCircumfrence"
    radius = 0;

    def calcCircumfrence(self):
        return 3.141 * 2 * self.radius


# Here we create an instance of the class stored inside a variable "circleA"
circleA = Circle()
# Here we set the state of the class to 15
circleA.radius = 15
print(circleA.calcCircumfrence())

circleB = Circle()
circleB.radius = 11
print(circleB.calcCircumfrence()) 

print("The difference in circumfrence between the two circles is:")
print(circleA.calcCircumfrence() - circleB.calcCircumfrence())