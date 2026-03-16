# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. 
# Create a program that do the same functionality without using removeprefix() function.
user_input = input("enter whatever you want: ")
user_remove = input("enter what you want to remove at the beginning: ")
if user_remove == user_input[:len(user_remove)]:
    print(user_input[len(user_remove):])
else:
    print(user_input)