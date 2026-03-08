# Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.
while True:
    try:
        first_number = float(input("enter your first number: "))
        second_number = float(input("enter your second number: "))
        if first_number != second_number:
            print("Not Equal")
        break
    except:
        print("only numbers are allowed")