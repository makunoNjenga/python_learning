course = "Python's course for beginners"
print(course)

course = 'Python course for "beginners"'
print(course)

# string with multilines eg to send to email
print("---------------MULTILINE STRING---------------")
course = '''
Dear Simon,

Am reaching out about python and django project I saw you posted on the web,

Regards, 
Recruiting Team
'''
print(course)

# strings are indexed as arrays
# we cand also have negative index that will start from the end of the string
# negative indexing is only found in python alone
print("---------------STRING INDEXING---------------")
course = 'Python course for beginners'
print(course[0], "(index 0)")
print(course[-2], "(index -2)")
print(course[0:3], "(prints index 0,1,2 --- it excludes the last index)")
print(course[2:], "(prints from given index to end of string)")
print(course[:5], "(first index will be assumed to be zero)")

# This feature [:] clones the exact copy of the string
print(course[:], "(first index will be assumed to be zero and length of string will be assumed as end index)")

name = 'Jeniffer'
print("\n------------EXERCISE------------")
print(name[1:-1])
