# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality 
# without using lstrip() function.
user_input = input("enter something with spaces at the beginning: ")
removed_spaces = ""
for char in user_input:
    if char != " " and removed_spaces == "":
        removed_spaces += char
    elif removed_spaces != "":
        removed_spaces += char
print(removed_spaces)