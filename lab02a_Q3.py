def addition(n):
    if n == 0:
        return 0
    else:
        return n + addition(n - 1)

res = addition(10)
print(res)

def display_student(name, age):
    print(name, age)

display_student("Emma", 26)
display_student("Emma", 26)

lst = [i for i in range(1, 29) if i % 2 == 0]
print(lst)
