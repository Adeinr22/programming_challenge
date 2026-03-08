# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
input_history = []

for i in range(10):
    numbers_input = float(input(f"enter number: "))
    if numbers_input not in input_history:
        input_history.append(numbers_input)
        
print(input_history)