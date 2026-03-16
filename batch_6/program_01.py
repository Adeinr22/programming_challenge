# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality 
# without using lstrip() function.
user_input = input("enter something with spaces at the beginning: ")
removed_spaces = 0
for char in user_input:
    if char == " ":
        removed_spaces += 1
    else:
        break
print(user_input[removed_spaces:])