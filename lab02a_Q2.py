#1
def showEmployee(name, salary=9000):
    print(f"Name: {name} salary: {salary}")

showEmployee("Ben", 12000)
showEmployee("Jessa")

#2
def outer_fun(a, b):
    def inner_fun(a, b):
        return a + b
    return inner_fun(a, b) + 5

result = outer_fun(5, 10)
print(result)
