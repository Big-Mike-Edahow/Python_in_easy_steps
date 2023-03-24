# raise.py

day = 32

try:
    if day > 31:
        raise ValueError("Invalid Day Number")
    
except ValueError as msg:
    print("The program found an", msg)

finally:
    print("But today is a beautiful day anyway.")
