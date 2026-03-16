# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same 
# functionality without using islower() function.
user_input = input("enter whatever you want: ")
has_cased = False
all_lower = True

for char in user_input:
    if 'A' <= char <= 'Z':
        all_lower = False
        break
    elif 'a' <= char <= 'z':
        has_cased = True

if has_cased and all_lower:
    print("all characters are lowercase")
else:
    print("not all characters are lowercase")