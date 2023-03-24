# yield.py
# A Fibonacci Sequence generator 

def fibonacci_generator():
    # Initialize two variables with an integer value of 0 and 1 respectively
    a = 0
    b = 1

    # Yield the addition of two previous values
    while True:
        yield a
        a, b = b, a + b

# Assign the returned generator object to a variable
fib = fibonacci_generator()

for i in fib:
    if i > 5000:
        break
    else:
        print("Generated: ", i)
