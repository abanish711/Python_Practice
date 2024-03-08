try:
    print("********* WELCOME **********")
    choice = input("Enter a number to find its factorial or press 'Q' to quit: ")
    factorial = 1
    while choice.upper() != 'Q':
        for i in range(1, int(choice)+1):
            factorial = factorial*i
        print(f"Factorial of {int(choice)} = {factorial}")
        factorial = 1
        choice = input("Enter a number to find its factorial or press 'Q' to quit: ")

    print("********* THANK YOU **********")

except Exception as e:
    print("################################################################")
    print("Something was wrong. Only 'numbers' or letter Q is allowed\n------\nError:\n------")
    print(e)
    
