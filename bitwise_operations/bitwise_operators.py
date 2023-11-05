n1 = 23477
n2 = 31213

print(bin(n1)[2:])
print(bin(n2)[2:])

# AND
n3 = n1 & n2
print(f"AND is: {bin(n3)[2:]}")
# OR
n4 = n1 | n2
print(f"OR is: {bin(n4)[2:]}")
# XOR (if the two values are different, we get 1) -> 1 XOR 0 is 1
n5 = n1 ^ n2
print(f"XOR is: 0{bin(n5)[2:]}")