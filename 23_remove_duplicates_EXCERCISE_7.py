numbers = [5, 2, 2, 1, 1, 7, 2, 4, 17, 5, 7, 4, 2]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

uniques.sort()
uniques.reverse()

print(uniques)
