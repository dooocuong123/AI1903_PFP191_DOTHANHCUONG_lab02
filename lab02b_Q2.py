import math

#1 Enter integer m and n:
m = int(input("Enter integer m: "))
n = int(input("Enter integer n: "))

#2 Find all common prime divisors of m and n
gcd = math.gcd(m, n)
print(f"Common prime divisors of {m} and {n} is: ", end="")
for i in range(1, gcd + 1):
    if gcd % i == 0:
        print(i, end=" ")

#3 Find the greatest common divisor (GCD) of m and n
print(f"\nGreatest common divisor of {m} and {n} is {gcd}.")

#4 Find the least common multiple (LCM) of m and n
lcm = m * n // gcd
print(f"Least common multiple of {m} and {n} is {lcm}.")
