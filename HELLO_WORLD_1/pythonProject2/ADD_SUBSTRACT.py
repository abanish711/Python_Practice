def add(first, second):
    return first + second


def subs(first, second):
    return first - second


a = int(input("Enter 1st Number:\n"))
b = int(input("Enter 2nd Number:\n"))

print(f"Sum of the numbers is {add(a, b)}")

print(f"Difference of the numbers is {abs(subs(a, b))}")
