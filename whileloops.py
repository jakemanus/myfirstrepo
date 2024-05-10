direction = ""

while direction != 'q':
    direction = input('Do you want to go (N)orth, (S)outh, (E)ast, or (W)est?   (Q)uit')
    
    if direction == 'n':
        print('You head north, into the forest.')
    elif direction == 's':
        print('The coast blocks your path south.')
    elif direction == 'e':
        print('You were eaten by a grue.')
    elif direction == 'w':
        print('The western fields are comforting to walk through.')
    elif direction == 'q':
        print('Quitting the game.')    
    else:
        print("I didn't recognize your choice.")