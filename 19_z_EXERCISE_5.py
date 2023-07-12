# create a string from nested loops that creates an F shaped
# only use nexted loops


# MY SOLUTION
numbers = [5, 2, 5, 2, 2]
for iteration in numbers:
    string_format = ''
    for x in range(iteration):
        string_format += "x"
    print(string_format)

# Easy solution
print("\nEASY SOLUTION")
print("-----------------")
for iteration in numbers:
    print("x" * iteration)
