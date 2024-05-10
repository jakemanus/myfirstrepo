# The following is a list which is an ordered collection of unnamed items
fruits = ['apple', 'banana', 'strawberry', 'orange', 'peach']

print(fruits[4])

fruits[4] = 'nectarine'

print(fruits[4])

# A tuple object, just like a list but 'immutable' The difference is the () are used instead of []

fruits_tuple = ('apple', 'banana', 'strawberry', 'orange', 'peach')

# This line will throw an exception

# fruits_tuple[4] = 'nectarine'

# The following is a dictionary which is an un-ordered collection of named (keyed) items
fruit_locations = {
    'Bin 1' : 'apple',
    'Bin 2' : 'banana',
    'Bin 3' : 'strawberry',
    'Bin 4' : 'orange',
    'Bin 5' : 'peach',
}

print(fruit_locations.get('Bin 3'))