import math

#1 Enter integer n where n > 5
n = int(input("Enter integer n where n > 5: "))
while n <= 5:
    n = int(input("The number n must be greater than 5. Enter n again: "))

#2 Caculate S1 = 1 + 2 + 3 + ...+n
S1 = sum(range(1, n+1))

#3 Caculate S2 = n!
S2 = math.factorial(n)

#4 Caculate S3 = 1+1/2+1/3+...1/n
S3 = sum([1/i for i in range(1, n+1)])

#5 Re-enter n. Check if n is prime or not.
n = int(input("Re-enter n: "))
if n > 1:
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number.")
