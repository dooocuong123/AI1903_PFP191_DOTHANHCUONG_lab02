
def func1(*args):
    print("Printing values")
    for arg in args:
        print(arg)
    print("\n\n")
#1
func1(20, 40, 60)
func1(80, 100)
#2
def calculation(a, b):
    sum = a + b
    diff = a - b
    return sum, diff

res = calculation(40, 10)
print(res)


