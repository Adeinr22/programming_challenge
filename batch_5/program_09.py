# Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
user_name = input("enter your full name in incorrect casing: ")
print((user_name.title().replace(" ", "")))