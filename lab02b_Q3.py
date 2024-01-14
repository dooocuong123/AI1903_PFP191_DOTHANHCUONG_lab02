# Function to check prime numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#1 Enter integer n (check input validation)
n = int(input("Enter interger n (n > 0): "))
while n <= 0:
    n = int(input("The number n must be greater than 0. Enter n again:"))

#2 Display n as a binary number
binary_n = bin(n)[2:]
print(f"The number {n} in binary form is {binary_n}.")

#3 Enter n again (no input validation checked). Calculate the sum of the digits of n
n = int(input("Re-enter n: "))
sum_digits = sum(int(digit) for digit in str(n))
print(f"Sum of digits of {n} is {sum_digits}.")

#4 Find the number m that is the inverse of n
if is_prime(n):
    print(f"{n} is a prime number, there is no inverse.")
else:
    m = int(str(n)[::-1])
    print(f"The inverse of {n} is {m}.")
