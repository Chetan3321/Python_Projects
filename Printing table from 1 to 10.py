#Loop Syntax
# Print numbers from 1 to 5 using a for loop
#for i in range(1, 6):  # range(start, end) - end is exclusive
#    print(i)

# Generate a multiplication table (1 to 5)

num1 =int(input("Enter the limit = "))
num2 = 10
num2 += 1
for i in range(num1, num2):  # Outer loop: Rows
    for j in range(num1, num2):  # Inner loop: Columns
         print(f"{i} x {j} = {i*j}", end="\t")
    print()  # Move to the next line after each row