# Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
while True:
    try:
        first_number = float(input("enter your first number: "))
        second_number = float(input("enter your second number: "))
        print(first_number ** second_number)
        break
    except:
        print("only numbers are allowed")