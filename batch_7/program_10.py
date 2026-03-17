# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. 
# Create a program that do the same functionality without using rindex() function.
try:
    user_input = input("Enter whatever you like: ")
    element_input = input("What element are you trying to find? ")
    start_input = input("What index would you like to start finding said element? (optional) ")
    end_input = input("What index would you like to end finding said element? (optional) ")

    start = int(start_input) if start_input != "" else 0
    end = int(end_input) if end_input != "" else len(user_input)

    if start < 0:
        start += len(user_input)
    if end < 0:
        end += len(user_input)

    start = max(0, min(start, len(user_input)))
    end = max(0, min(end, len(user_input)))

    sub_len = len(element_input)
    found_index = -1

    for i in range(end - sub_len, start - 1, -1):
        if user_input[i:i+sub_len] == element_input:
            found_index = i
            break

    if found_index != -1:
        print(f"Element '{element_input}' is at index {found_index}")
    else:
        print("substring not found")

except ValueError as e:
    print("Error:", e)