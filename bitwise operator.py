x = 10
y = 8
print(bin(x))
print(bin(y))
print(x & y, bin(x & y))  # and (&) operator
print(bin(x | y), x | y)  # or (|) operator
print(bin(x ^ y), x ^ y)

# 0b1010
# 0b1000

# & 1000 8
# | 1010 10
# ^ 0010 2
