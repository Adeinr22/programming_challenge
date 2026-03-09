# Prog02: Create a program that ask the user to input a number (0-1000). 
# Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
try:
    user_number = float(input("input a number (0-1000): "))
    if user_number > 1000 or user_number < 0:
        print("only numbers from 0 to 1000 is allowed")
    else:
        print(str(int(user_number)).zfill(6))
except:
    print("Invalid input. Only numbers are allowed")