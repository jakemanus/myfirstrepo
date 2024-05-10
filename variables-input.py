# Establish variables
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# Calculate the permiter
s = (a + b + c) / 2

# Calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print ('The area of the trianble is %0.2f' %area)