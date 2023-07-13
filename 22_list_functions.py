numbers = [5, 2, 2, 1, 7, 2, 4]

numbers.append(20)  # insert 20 at the end of the list
print(numbers)

numbers.insert(0, 10)  # insert 10 at index 0
print(numbers)

numbers.remove(5)  # remove a number
print(numbers)

print(numbers.pop())  # print the last number

print(numbers.index(7))  # print the index of the first occurence of 7

print(7 in numbers)  # check if 7 exits in the list

print(numbers.count(2))  # count occurrence of a number in the list

numbers.sort()  # sorting the numbers
print(numbers)

numbers.sort()  # sorting the numbers in reverse
numbers.reverse()
print(numbers)

# copy function
# copies the original value of the list
numbers_2 = numbers.copy()

numbers.clear()  # clear all items in the list
print(numbers)
