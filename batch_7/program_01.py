# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without 
# using rstrip() function.
user_input = input("enter something with spaces at the end: ")
removed_spaces = []
for char in user_input:
    removed_spaces.append(char)
while removed_spaces[-1] == ' ':
    removed_spaces.pop()
for i in removed_spaces:
    print(i, end='')