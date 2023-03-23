# return.py
# Return the square root of an integer

num = input("Enter an integer:")

def square(num):
    if num.isdigit() != True:   # Check to see if the input is an integer
        print("Invalid entry")
        exit()                  # Exit the program if the input is invalid
    
    num = int(num)
    return num ** 2

print(num, " squared is:", square(num))
