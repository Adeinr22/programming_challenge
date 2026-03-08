# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
duplicates = []
duplicates_checker = []

for i in range(10):
    numbers_input = float(input(f"enter number: "))
    duplicates.append(numbers_input)

for i in range(10):
    if duplicates.count(duplicates[i]) == 1:
        duplicates_checker.append(duplicates[i])

for i in duplicates_checker:
    duplicates.remove(i)
    
print(duplicates)