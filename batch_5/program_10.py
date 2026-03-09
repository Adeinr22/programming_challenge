# Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
user_name = input("enter your full name in incorrect casing: ")
print((user_name.lower()).replace(" ", "_"))