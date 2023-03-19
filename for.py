# for.py

# Initialize a list, tuple, and dictionary
chars = ['A', 'B', 'C']
fruit = ('Apple', 'Banana', 'Cherry')
dict = { 'name' : 'Mike', 'ref' : 'Python', 'sys' : 'Win' }

# Display all list element values
print("\nElements:\t", end = ' ')
for item in chars:
    print(item, end = ' ')

# Print list element values and their relative index number
print("\nEnumerated:\t", end = ' ')
for item in enumerate( chars ):
    print(item, end = ' ')

# Print list and tuple elements
print("\nZipped:\t", end = ' ')
for item in zip( chars, fruit):
    print(item, end = ' ')

# Print dictionary key:value pairs
print("\nPaired:")
for key, value in dict.items():
    print(key, '=', value)
