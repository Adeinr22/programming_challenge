# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality 
# without using lstrip() function.
user_name = input("enter your full name with spaces at the beginning: ")
removed_spaces = ""
for char in user_name:
    if char != " " and removed_spaces == "":
        removed_spaces += char
    elif removed_spaces != "":
        removed_spaces += char
print(removed_spaces)