# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality 
# without using lower() function.
user_input = input("enter whatever you want: ")
lower_version = ""
for char in user_input:
    if char == char.upper():
        lower_version += char.swapcase()
    else:
        lower_version += char
print(lower_version)