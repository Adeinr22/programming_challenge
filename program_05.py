# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point
while True:
    try:
        first_number = float(input("enter your first number: "))
        second_number = float(input("enter your second number: "))
        if second_number != 0:
            print(first_number / second_number)
        else:
            print("can't divide by zero!")
        break
    except:
        print("only numbers are allowed")