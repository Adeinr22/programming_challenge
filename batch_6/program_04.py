# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

user_input = input("enter whatever you want: ")
has_uppercase = False
has_lowercase = False

for char in user_input:
    if 'a' <= char <= 'z':
        has_lowercase = True
        break  
    elif 'A' <= char <= 'Z':
        has_uppercase = True
if has_lowercase:
    print("input contains a lowercase")
elif has_uppercase:
    print("all characters are uppercase")
else:
    print("no uppercase letters")