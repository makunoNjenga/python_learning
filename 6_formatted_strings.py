# useful when you want to generate dynamic texts  from your variable
# in short, CONCATENATIONS
first = 'John'
last = 'Smith'
message = first + " [" + last + "] is a coder"
print("------------METHOD 1 (concatenation)------------")
print(message)

print("------------METHOD 2 (Formatted Strings)------------")
# helps you visualize how the string will look like
# its the recommended method
message = f'{first} [{last}] is a coder'
print(message)
