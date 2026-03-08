# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
no_duplicates = []
duplicates_checker = []

for i in range(10):
    numbers_input = float(input(f"enter number: "))
    no_duplicates.append(numbers_input)

for i in range(10):
    if no_duplicates.count(no_duplicates[i]) > 1:
        duplicates_checker.append(no_duplicates[i])

for i in duplicates_checker:
    no_duplicates.remove(i)
    
print(no_duplicates)