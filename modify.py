# modify.py

string = "python in easy steps"

print("\nOriginal string:", string)
print("\nCapitalized:\t", string.capitalize())
print("\nTitled:\t\t", string.title())
print("\nCentered:\t", string.center(30, '*'))

print("\nUppercase:\t", string.upper())
print("\nJoined:\t\t", string.join('**'))

print("\nJustified:\t", string.rjust(30, '*'))

print("\nReplaced:\t", string.replace('s', '*') + "\n")


