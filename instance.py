# instance.py

from Bird import *

print("\nClass instances of:\n", Bird.__doc__)

polly = Bird('\"Squawk, squawk!\"')

print("\nNumber of Birds:", polly.count)
print("Polly says:", polly.talk())

harry = Bird('\"Tweet, tweet!\"')

print("\nNumber of Birds:", harry.count)
print("Harry says:", harry.talk(), "\n")

