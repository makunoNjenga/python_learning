numbers_to_words = {
    '0': "Zero",
    '1': "One",
    '2': "Two",
    '3': "Three",
    '4': "Four",
    '5': "Five",
    '6': "Six",
    '7': "Seven",
    '8': "Eight",
    '9': "Nine",
}

numbers = input("Phone Numbers: ")
string_numbers = ""

for number in numbers:
    string_numbers += numbers_to_words.get(number, '!') + " "

print(string_numbers)
