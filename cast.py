# cast.py

a = input("Enter a number: ")
b = input("Now enter another number: ")

sum = a + b
print("\nDaty type sum: ", sum, "\t", type(sum))

sum = int(a) + int(b)
print("Data type sum: ", sum, "\t", type(sum))

sum = float(sum)
print("Data type sum: ", sum, "\t", type(sum))

sum = chr(int(sum))
print("Data type sum: ", sum, "\t", type(sum), "\n")
