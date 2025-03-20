# Initial values
a = 5
b = 10

print("Before swapping:")
print("a =", a, "& b =", b)

# Swapping using a combination of bitwise and arithmetic operators
a = a ^ b     # Step 1: Start with XOR
b = b ^ a     # Step 2: Apply XOR again
a = a ^ b     # Step 3: Apply XOR again

print("After swapping:")
print("a =", a, "& b =", b)