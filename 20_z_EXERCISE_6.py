# Write a program to print the largest item in a list

numbers = [20, 28, 90, 87, 65, 37, 73, 38, 38, 9, 98, 37, 63, 76, 9, 83]
max_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number

print(f"Max Number: {max_num}")
