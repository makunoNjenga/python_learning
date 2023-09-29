# this function has parameters with default values
def greet_user(first_name="John", last_name="Doe"):
    print(f"Hi {first_name} {last_name}, Welcome aboard")


print("start")
greet_user("Simon", "Njenga")

# the above function calls are positional arguments, meaning the position that you call them matters
# now, we introduce keyboard arguments where you call the specific parameter to be assigned to provided arguments
# Keyboard arguments enhances readability of the code
greet_user(last_name="Njenga", first_name="Simon")

# when mixing the positional arguments and keyboard arguments, enter positional arguments first
# and keyboard arguments last
greet_user("simon", last_name="Njenga")

print("Finish")
