# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
while True:
    try:
        first_number = int(input("enter your first number: "))
        second_number = int(input("enter your second number: "))
        for i in range(first_number + 1, second_number):
            print(i)
        break
    except:
        print("only numbers are allowed")