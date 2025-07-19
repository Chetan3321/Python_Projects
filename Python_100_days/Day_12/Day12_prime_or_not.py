def is_prime(num):
    if num <= 1:
        return False  # 0 and 1 are not prime
    for i in range(2, int(num**0.5) + 1):  # Check up to sqrt(num)
        if num % i == 0:
            return False
    return True

print(is_prime(int(input("Enter the number: "))))