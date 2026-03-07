# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
while True:
    try:
        first_number = float(input("enter your first number: "))
        second_number = float(input("enter your second number: "))
        if first_number > second_number:
            print(first_number)
        elif first_number < second_number:
            print(second_number)
        elif first_number == second_number:
            print(f'first number {first_number} and second number {second_number} are the same')
        break
    except:
        print("only numbers are allowed")