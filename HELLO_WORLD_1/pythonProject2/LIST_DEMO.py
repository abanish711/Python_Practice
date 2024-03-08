list1 = []
num = input("Please enter a number: \n")
for i in range(1, int(num)+1):
    list1.append(i**2)
print(f"Below are the square of all numbers from 1 to {num}")
print(list1)
