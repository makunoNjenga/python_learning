# used to store attributes of a certain object
# defined by curly braces
# each key must be unique
# you can add anything including lists on the dictionary
# they are similar to associative array
# key names are case sensitive

customer = {
    "name": "John Smith",
    "age": 27,
    "email": "makuno.biz@gmail.com",
    "is_verified": True
}

# accessing dictionary
print(f"Name = {customer['name']} email = {customer['email']}")

# second way of accessing dictionary
# the best way
# if it fails to find data, it returns null
print(f"Age = {customer.get('age')}")

# access key, if it fails, supply a default value
print(f"Age = {customer.get('ages','30 Yrs Old')}")

# updating dictionary values
customer["name"] = "Simon Njenga"
print(f"Updated name is {customer.get('name')}")

