# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality 
# without using upper() function.
user_input = input("enter whatever you want: ")
upper_version = ""
for char in user_input:
    if char == char.lower():
        upper_version += char.swapcase()
    else:
        upper_version += char
print(upper_version)