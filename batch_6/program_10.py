# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. 
# Create a program that do the same functionality without using title() function.
user_input = input("enter whatever you want: ").lower()
capitalized_version = []
for char in user_input:
    if capitalized_version == [] or capitalized_version[-1] == ' ':
        capitalized_version.append(char.upper())
    else:
        capitalized_version.append(char)
 
for i in capitalized_version:
    print(i, end="")