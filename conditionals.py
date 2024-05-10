# Conditionals use the 'IF' statement to allow you to write code that only executes under certain conditons
# If <condition>:
#   Code to run when condition is true
# Else:
#   Code to run when condition is false
# ^^ optional ( the Else statement is an optional statement)
# 
# Conditonal operators | ==     'Are these 2 values equal'
#                      | >,>=   'Is the first value greater than', 'Is the first value greater than or equal to'
#                      | <,<=     ^^ but less than             ,              ^^ but less than or equal to
#                      | <>,!=  'Both these read as not equal to'
#
# Multiple 'IF' statements can be strung together using elif
# If <condition>:
#       True code
# Elif <condition>:
#       True code
# Elif <condition>:
#       True code
# Else:
#       Else code

direction = input('Do you want to go (N)orth, (S)outh, (E)ast, or (W)est?')

if direction == 'n':
    print('You head north, into the forest.')
elif direction == 's':
    print('The coast blocks your path south.')
elif direction == 'e':
    print('You were eaten by a grue.')
elif direction == 'w':
    print('The western fields are comforting to walk through.')    
else:
    print("I didn't recognize your choice.")