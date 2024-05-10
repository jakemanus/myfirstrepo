# Loops allow us to write code once and execute it multiple times
# "For" loops iterate over a sequence (or list) or even a dictionary
# "While" loops iterate until a <condition> evaltuates to false (while loops are kind of like a loop combined with an if statement)

# The following is just a basic list called states
states = ['New York', 'Michigan', 'California', 'Texas', 'Oregan']

for state in states:
    print(state)


# The following is a dictionary called abbrevs

abbrevs = {
    "New York" : "NY",
    "Michigan" : "MI",
    "California" : "CA",
    "Texas" : "TX",
    "Oregan" : "OR",
}

# The following prints out the key 'key' and also the value based on the key 'abbrevs[key]'
for key in abbrevs:
    print(key + ":" + abbrevs[key])

# The following is a range function. It creates a range of 20 values and iterates through them. prints out 0-19 b/c lists start with 0
for i in range(20):
    print(i)