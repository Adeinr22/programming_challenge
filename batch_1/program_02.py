# Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.
while True:
    try:
        first_number = float(input("enter your first number: "))
        second_number = float(input("enter your second number: "))
        if first_number == second_number:
            print("equal")
        break
    except:
        print("only numbers are allowed")