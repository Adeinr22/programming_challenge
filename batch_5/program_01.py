# Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. 
# Print the input without the spaces in the beginning.
user_name = input("enter your full name with spaces at the beginning: ")
print(user_name.lstrip())