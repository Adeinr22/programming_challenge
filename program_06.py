# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
numbers_result = 0
for i in range(1,11):
    numbers_input = float(input(f"enter number {i}: "))
    numbers_result -= numbers_input
print(numbers_result)