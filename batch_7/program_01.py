# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without 
# using rstrip() function.
user_input = input("enter something with spaces at the end: ")
removed_spaces = 0
for i in range(-1, (-len(user_input)-1), -1):
    if user_input[i] == " ":
        removed_spaces += 1
    else:
        break
print(user_input[:len(user_input) - removed_spaces])