# Establish variables
a = 5
b = 6
c = 7

# Calculate the permiter
s = (a + b + c) / 2

# Calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print ('The area of the trianble is %0.2f' %area)