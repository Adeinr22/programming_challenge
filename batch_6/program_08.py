# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same 
# functionality without using swapcase() function.
user_input = input("enter whatever you want: ")
swap_version = ''
for char in user_input:
    if char == char.upper():
        swap_version += char.lower()
    elif char == char.lower():
        swap_version += char.upper()
print(swap_version)