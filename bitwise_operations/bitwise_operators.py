n1 = 23477
n2 = 31213

print(f"n1 = {bin(n1)[2:]}")
print(f"n1 = {bin(n2)[2:]}")

# AND
n3 = n1 & n2
print(f"AND: {bin(n3)[2:]}")
# OR
n4 = n1 | n2
print(f"OR: {bin(n4)[2:]}")
# XOR (if the two values are different, we get 1) -> 1 XOR 0 is 1
n5 = n1 ^ n2
print(f"XOR: 0{bin(n5)[2:]}")
# NOT (negation operator: it does not turn all the bits around because we're working with unsigned integers.) 
print(f"NOT: {bin(~n1)[3:]}")
negation_of_n1 = bin(0b111111111111111 - n1)[2:]
print(f"Exact negation of n1: 0{negation_of_n1}")

# Shifts
number = 20
number <<=1
print(number)