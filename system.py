# system.py

# import the sys and keyword modules
import sys, keyword

print("Python version: ", sys.version)
print("Python Interpreter location: ", sys.executable)

print("Python Module search path: ")
for dir in sys.path:
    print(dir)

print("Python Keywords: ")
for word in keyword.kwlist:
    print(word)
    