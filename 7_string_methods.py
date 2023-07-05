course = 'Python for Beginners'

print("---- Character Length ----")
# useful for validation purposes when getting input from the user
print(len(course))

print("---- STRING METHODS ----")
print(f'{course.upper()} (Upper Case)')
print(f'{course.lower()} (Lower Case)')

# find character sequence
# return the index of the occurrence of the character sequence
# returns -1 of no match found
print(course.find("o"))
print(course.find("Beginners"))
print(course.find("O"))

# replace character sequence
# Its case sensitive
print(course.replace("Beginners", "Absolute Beginners"))


print("\n---- in EXPRESSION ----")
# used to check if there is a character sequence in a string
if 'Python' in course:
    print("Python is HISSING")
else:
    print("Python is MiSSING")
