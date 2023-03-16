# bitwise.py

a = 10
b = 5

print("a = ", a, "\tb = ", b)

# Bitwise XOR
# 1010 ^ 0101 = 1111 (decimal 15)
a = a ^ b

# Bitwise XOR
# 1111 ^ 0101 = 1010 (decimal 10)
b = a ^ b

# Bitwise XOR
# 1111 ^ 1010 = 0101 (decimal 5)
a = a ^ b

print("a = ", a, "\t\tb = ", b)
